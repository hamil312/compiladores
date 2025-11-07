class IR_Generator:
    def __init__(self):
        self.instructions = []  # Lista para guardar las instrucciones TAC
        self.temp_count = 0     # Contador para variables temporales (t0, t1, t2...)
        self.label_count = 0    # Contador para etiquetas (L0, L1, L2...)

    def new_temp(self):
        """Crea una nueva variable temporal y la devuelve."""
        temp_name = f"t{self.temp_count}"
        self.temp_count += 1
        return temp_name

    def new_label(self):
        """Crea una nueva etiqueta y la devuelve."""
        label_name = f"L{self.label_count}"
        self.label_count += 1
        return label_name

    def add_instruction(self, op, arg1=None, arg2=None, result=None):
        """Añade una instrucción a la lista."""
        self.instructions.append({'op': op, 'arg1': arg1, 'arg2': arg2, 'result': result})

    def emit_label(self, label):
        self.add_instruction(f"{label}:", None, None, None)

    # ------------------------------------------------------------------
    # Helpers para generar TAC a partir del parse tree (contextos ANTLR).
    # Se asume que se llamarán estos métodos con los contextos
    # correspondientes (por ejemplo desde un Visitor/Listener).
    # Cada método de expresión devuelve un operando: nombre de temp o literal.
    # ------------------------------------------------------------------

    def gen_program(self, ctx):
        # ctx: program context (program : statement+ EOF)
        for child in ctx.statement():
            self.gen_statement(child)

    def gen_statement(self, ctx):
        # ctx puede ser assignment, printStmt, ifStmt, whileStmt, block
        node = ctx.getChild(0)
        tname = node.__class__.__name__
        text = node.getText()
        # Distinguimos por nombre de regla (más robusto desde Visitor).
        rule = node.getPayload().__class__.__name__ if hasattr(node, "getPayload") else None
        # Simpler: mirar el número de hijos/tokens para decidir según la forma
        first = node.getText()
        # Intentar dispatch por tipo de regla textual:
        if node.getText().startswith("print"):
            self.gen_print(node)
        elif node.getText().startswith("if"):
            self.gen_if(node)
        elif node.getText().startswith("while"):
            self.gen_while(node)
        elif node.getText().startswith("{"):
            self.gen_block(node)
        else:
            # Asumimos assignment por defecto
            self.gen_assignment(node)

    def gen_assignment(self, ctx):
        # ctx: assignment : ID ASSIGN (boolExpr | arithExpr) SEMI
        # Forma simple: child0 = ID, child2 = expresion
        var_name = ctx.getChild(0).getText()
        rhs_ctx = ctx.getChild(2)
        # Determinar si es boolean or arith: por la clase del contexto no siempre fácil,
        # así intentamos generar con los generadores y confiar en que recursión funciona.
        if hasattr(rhs_ctx, "getText"):
            # Si la expresión es arithExpr o boolExpr o alike:
            rhs = self.gen_any_expr(rhs_ctx)
        else:
            rhs = rhs_ctx.getText()
        # resultado asignado a la variable
        self.add_instruction('=', arg1=rhs, result=var_name)

    def gen_print(self, ctx):
        # ctx: printStmt : PRINT LPAREN ID RPAREN SEMI
        # El ID está en child 2
        id_name = ctx.getChild(2).getText()
        self.add_instruction('print', arg1=id_name)

    def gen_if(self, ctx):
        # ctx: IF LPAREN boolExpr RPAREN block (ELSE block)?
        bool_ctx = ctx.getChild(2)
        then_block = ctx.getChild(4)
        has_else = (len(ctx.getChildren()) > 5)
        else_block = ctx.getChild(6) if has_else else None

        cond = self.gen_bool_expr(bool_ctx)
        else_label = self.new_label()
        end_label = self.new_label()

        self.add_instruction('if_false_goto', arg1=cond, result=else_label)
        # then
        self.gen_block(then_block)
        self.add_instruction('goto', result=end_label)
        # else
        self.emit_label(else_label)
        if else_block is not None:
            self.gen_block(else_block)
        # end
        self.emit_label(end_label)

    def gen_while(self, ctx):
        # ctx: WHILE LPAREN boolExpr RPAREN block
        bool_ctx = ctx.getChild(2)
        body = ctx.getChild(4)

        start = self.new_label()
        end = self.new_label()

        self.emit_label(start)
        cond = self.gen_bool_expr(bool_ctx)
        self.add_instruction('if_false_goto', arg1=cond, result=end)
        self.gen_block(body)
        self.add_instruction('goto', result=start)
        self.emit_label(end)

    def gen_block(self, ctx):
        # ctx: LBRACE statement* RBRACE
        # Genera código para cada statement dentro del bloque
        for i in range(1, ctx.getChildCount() - 1):
            child = ctx.getChild(i)
            # child es un statement context
            self.gen_statement(child)

    # ------------------------------------------------------------------
    # Generadores para expresiones (aritméticas y booleanas).
    # Devuelven un operando usable (temp o literal).
    # ------------------------------------------------------------------

    def gen_any_expr(self, ctx):
        # Determina si la expresión es booleana o aritmética por la estructura.
        # Si contiene tokens booleanos o comparadores -> boolean; si contiene + - * / o INT/ID -> aritmética.
        txt = ctx.getText()
        # heurística simple: si contiene 'true'/'false'/'and'/'or'/'!'/'=='/'<' etc -> boolean
        if any(k in txt.lower() for k in ('true', 'false', 'and', 'or', 'not', '&&', '||', '==', '!=', '<', '>', '<=', '>=')):
            return self.gen_bool_expr(ctx)
        else:
            return self.gen_arith_expr(ctx)

    # Arith
    def gen_arith_expr(self, ctx):
        # arithExpr : arithExpr ADD arithTerm | arithExpr SUB arithTerm | arithTerm
        if ctx.getChildCount() == 3:
            left = self.gen_arith_expr(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.gen_arith_term(ctx.getChild(2))
            res = self.new_temp()
            self.add_instruction(op, arg1=left, arg2=right, result=res)
            return res
        else:
            return self.gen_arith_term(ctx.getChild(0))

    def gen_arith_term(self, ctx):
        # arithTerm : arithTerm MUL arithFactor | arithTerm DIV arithFactor | arithFactor
        if ctx.getChildCount() == 3:
            left = self.gen_arith_term(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right = self.gen_arith_factor(ctx.getChild(2))
            res = self.new_temp()
            self.add_instruction(op, arg1=left, arg2=right, result=res)
            return res
        else:
            return self.gen_arith_factor(ctx.getChild(0))

    def gen_arith_factor(self, ctx):
        # arithFactor : SUB arithFactor | LPAREN arithExpr RPAREN | INT | ID
        if ctx.getChildCount() == 2:
            # unary minus
            inner = self.gen_arith_factor(ctx.getChild(1))
            res = self.new_temp()
            # representamos negación como 0 - inner
            self.add_instruction('-', arg1='0', arg2=inner, result=res)
            return res
        elif ctx.getChildCount() == 3:
            # paréntesis
            return self.gen_arith_expr(ctx.getChild(1))
        else:
            token = ctx.getChild(0).getText()
            # INT literal o ID variable
            return token

    # Boolean
    def gen_bool_expr(self, ctx):
        # boolExpr : boolExpr OR boolTerm | boolTerm
        if ctx.getChildCount() == 3:
            left = self.gen_bool_expr(ctx.getChild(0))
            op = ctx.getChild(1).getText().lower()
            right = self.gen_bool_term(ctx.getChild(2))
            res = self.new_temp()
            # Usamos OR/AND evaluando ambos operandos como 0/1
            if op in ('or', '||'):
                self.add_instruction('or', arg1=left, arg2=right, result=res)
            else:
                # fallback
                self.add_instruction(op, arg1=left, arg2=right, result=res)
            return res
        else:
            return self.gen_bool_term(ctx.getChild(0))

    def gen_bool_term(self, ctx):
        # boolTerm : boolTerm AND boolFactor | boolFactor
        if ctx.getChildCount() == 3:
            left = self.gen_bool_term(ctx.getChild(0))
            op = ctx.getChild(1).getText().lower()
            right = self.gen_bool_factor(ctx.getChild(2))
            res = self.new_temp()
            if op in ('and', '&&'):
                self.add_instruction('and', arg1=left, arg2=right, result=res)
            else:
                self.add_instruction(op, arg1=left, arg2=right, result=res)
            return res
        else:
            return self.gen_bool_factor(ctx.getChild(0))

    def gen_bool_factor(self, ctx):
        # boolFactor : NOT boolFactor | LPAREN boolExpr RPAREN | TRUE | FALSE | ID | comparison
        if ctx.getChildCount() == 2:
            # NOT
            inner = self.gen_bool_factor(ctx.getChild(1))
            res = self.new_temp()
            # not x => 1 if x==0 else 0 -> implementamos como comparison: x == 0
            self.add_instruction('==', arg1=inner, arg2='0', result=res)
            return res
        elif ctx.getChildCount() == 3:
            # parentesis
            return self.gen_bool_expr(ctx.getChild(1))
        else:
            child = ctx.getChild(0)
            txt = child.getText()
            # Puede ser TRUE/FALSE, ID (variable booleana) o comparison (arithExpr compOp arithExpr)
            if txt.lower() in ('true', 'false'):
                return '1' if txt.lower() == 'true' else '0'
            # Distinguir si es comparación: si el nodo tiene 3 hijos (comparision)
            if child.getChildCount() == 3:
                return self.gen_comparison(child)
            # otherwise ID
            return txt

    def gen_comparison(self, ctx):
        # comparison : arithExpr compOp arithExpr
        left = self.gen_arith_expr(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.gen_arith_expr(ctx.getChild(2))
        res = self.new_temp()
        self.add_instruction(op, arg1=left, arg2=right, result=res)
        return res

    # ------------------------------------------------------------------
    # Representación textual del IR
    # ------------------------------------------------------------------
    def __str__(self):
        """Genera una representación en texto del código IR."""
        output = "## CÓDIGO INTERMEDIO (TAC)\n"
        for inst in self.instructions:
            op = inst['op']
            if op in ['+', '-', '*', '/', '<', '>', '>=', '<=', '==', '!=', 'and', 'or']:
                output += f"  {inst['result']} = {inst['arg1']} {op} {inst['arg2']}\n"
            elif op == '=':
                output += f"  {inst['result']} = {inst['arg1']}\n"
            elif op == 'if_false_goto':
                output += f"  if_false {inst['arg1']} goto {inst['result']}\n"
            elif op == 'goto':
                output += f"  goto {inst['result']}\n"
            elif op == 'print':
                output += f"  print {inst['arg1']}\n"
            elif op.endswith(':'):
                output += f"{op}\n"
            else:
                # fallback genérica
                output += f"  {op} {inst.get('arg1', '')} {inst.get('arg2', '')} {inst.get('result', '')}\n"
        return output