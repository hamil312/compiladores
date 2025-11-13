class IR_Generator:
    def __init__(self):
        self.instructions = []  # Lista para guardar las instrucciones TAC
        self.temp_count = 0     # Contador para variables temporales (t0, t1, t2...)
        self.label_count = 0    # Contador para etiquetas (L0, L1, L2...)
        self.current_function_end_label = None  # usado cuando generamos returns dentro de una función

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
        # Primero generar funciones (si las hay), luego statements globales
        if hasattr(ctx, "functionDef"):
            for f in ctx.functionDef():
                self.gen_function_def(f)
        # statements globales
        for child in ctx.statement():
            self.gen_statement(child)

    def gen_statement(self, ctx):
        # ctx puede ser assignment, printStmt, ifStmt, whileStmt, block, varDecl
        if ctx.assignment():
            self.gen_assignment(ctx.assignment())
            return
        if ctx.printStmt():
            self.gen_print(ctx.printStmt())
            return
        if ctx.ifStmt():
            self.gen_if(ctx.ifStmt())
            return
        if ctx.whileStmt():
            self.gen_while(ctx.whileStmt())
            return
        if ctx.block():
            self.gen_block(ctx.block())
            return
        if ctx.varDecl():
            self.gen_var_decl(ctx.varDecl())
            return
        # fallback: intentar procesar primer hijo como statement
        node = ctx.getChild(0)
        # intentar dispatch por texto (compatibilidad con versiones anteriores)
        text = node.getText()
        if text.startswith("print"):
            self.gen_print(node)
        elif text.startswith("if"):
            self.gen_if(node)
        elif text.startswith("while"):
            self.gen_while(node)
        elif text.startswith("{"):
            self.gen_block(node)
        else:
            self.gen_assignment(node)

    def gen_var_decl(self, ctx):
        # varDecl : VAR ID (COLON varType)? (ASSIGN (boolExpr | arithExpr))? SEMI
        var_name = ctx.ID().getText()
        # buscar token '=' entre children
        for i in range(ctx.getChildCount()):
            child = ctx.getChild(i)
            if child.getText() == '=':
                rhs_ctx = ctx.getChild(i + 1)
                rhs = self.gen_any_expr(rhs_ctx)
                self.add_instruction('=', arg1=rhs, result=var_name)
                return
        # si no hay asignación, no emitimos nada (declaración sin inicializar)

    def gen_function_def(self, ctx):
        # functionDef : FUNCTION ID LPAREN paramList? RPAREN COLON returnType LBRACE statement* returnStmt RBRACE
        name = ctx.ID().getText()
        start_label = f"func_{name}"
        end_label = f"end_func_{name}"
        self.emit_label(start_label)

        # guardar y establecer current_function_end_label para returns internos
        old_end = self.current_function_end_label
        self.current_function_end_label = end_label

        # Generar statements del cuerpo (ctx.statement() recoge statements dentro)
        for st in ctx.statement():
            self.gen_statement(st)

        # generar returnStmt
        if hasattr(ctx, "returnStmt") and ctx.returnStmt():
            # normalmente hay exactamente una returnStmt según la gramática
            self.gen_return(ctx.returnStmt())
        # asegurar etiqueta final de la función
        self.emit_label(end_label)

        # restaurar
        self.current_function_end_label = old_end

    def gen_return(self, ctx):
        # returnStmt : RETURN (boolExpr | arithExpr) SEMI
        # child 1 es la expresión
        expr_ctx = ctx.getChild(1)
        val = self.gen_any_expr(expr_ctx)
        # emitir retorno
        self.add_instruction('ret', arg1=val)
        # saltar al final de la función (si tenemos etiqueta)
        if self.current_function_end_label:
            self.add_instruction('goto', result=self.current_function_end_label)

    def gen_assignment(self, ctx):
        # assignment : ID ASSIGN (boolExpr | arithExpr) SEMI
        var_name = ctx.ID().getText()
        rhs_ctx = ctx.getChild(2)
        rhs = self.gen_any_expr(rhs_ctx)
        self.add_instruction('=', arg1=rhs, result=var_name)

    def gen_print(self, ctx):
        # printStmt : PRINT LPAREN ID RPAREN SEMI
        id_name = ctx.ID().getText()
        self.add_instruction('print', arg1=id_name)

    def gen_if(self, ctx):
        # IF LPAREN boolExpr RPAREN block (ELSE block)?
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
        # WHILE LPAREN boolExpr RPAREN block
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
        # LBRACE statement* RBRACE
        for i in range(1, ctx.getChildCount() - 1):
            child = ctx.getChild(i)
            # child es un statement context
            self.gen_statement(child)

    # ------------------------------------------------------------------
    # Generadores para expresiones (aritméticas y booleanas).
    # Devuelven un operando usable (temp o literal).
    # ------------------------------------------------------------------

    def gen_any_expr(self, ctx):
        # heurística: si contiene booleanos/operadores comparadores => boolean, sino aritmética
        txt = ctx.getText()
        if any(k in txt.lower() for k in ('true', 'false', 'and', 'or', 'not', '&&', '||', '==', '!=', '<', '>', '<=', '>=')):
            return self.gen_bool_expr(ctx)
        else:
            return self.gen_arith_expr(ctx)

    # Arith
    def gen_arith_expr(self, ctx):
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
        # arithFactor : SUB arithFactor | LPAREN arithExpr RPAREN | INT | ID | functionCall
        if ctx.getChildCount() == 2:
            # unary minus
            inner = self.gen_arith_factor(ctx.getChild(1))
            res = self.new_temp()
            self.add_instruction('-', arg1='0', arg2=inner, result=res)
            return res
        elif ctx.getChildCount() == 3:
            # parenthesis
            return self.gen_arith_expr(ctx.getChild(1))
        else:
            child = ctx.getChild(0)
            # INT literal
            if child.getText().isdigit():
                return child.getText()
            # function call detection: child tiene subchildren y sigue patrón ID '(' ... ')'
            if child.getChildCount() >= 2 and child.getChild(1).getText() == '(':
                return self.gen_function_call(child)
            # ID variable
            return child.getText()

    # Boolean
    def gen_bool_expr(self, ctx):
        if ctx.getChildCount() == 3:
            left = self.gen_bool_expr(ctx.getChild(0))
            op = ctx.getChild(1).getText().lower()
            right = self.gen_bool_term(ctx.getChild(2))
            res = self.new_temp()
            if op in ('or', '||'):
                self.add_instruction('or', arg1=left, arg2=right, result=res)
            else:
                self.add_instruction(op, arg1=left, arg2=right, result=res)
            return res
        else:
            return self.gen_bool_term(ctx.getChild(0))

    def gen_bool_term(self, ctx):
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
        # NOT boolFactor | LPAREN boolExpr RPAREN | TRUE | FALSE | ID | comparison | functionCall
        if ctx.getChildCount() == 2:
            # NOT
            inner = self.gen_bool_factor(ctx.getChild(1))
            res = self.new_temp()
            self.add_instruction('==', arg1=inner, arg2='0', result=res)
            return res
        elif ctx.getChildCount() == 3:
            # parentesis
            return self.gen_bool_expr(ctx.getChild(1))
        else:
            child = ctx.getChild(0)
            txt = child.getText()
            if txt.lower() in ('true', 'false'):
                return '1' if txt.lower() == 'true' else '0'
            # comparison (node con 3 hijos)
            if child.getChildCount() == 3 and child.getChild(1).getText() in ('==', '!=', '<', '<=', '>', '>='):
                return self.gen_comparison(child)
            # function call detection
            if child.getChildCount() >= 2 and child.getChild(1).getText() == '(':
                return self.gen_function_call(child)
            # ID variable
            return child.getText()

    def gen_comparison(self, ctx):
        left = self.gen_arith_expr(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right = self.gen_arith_expr(ctx.getChild(2))
        res = self.new_temp()
        self.add_instruction(op, arg1=left, arg2=right, result=res)
        return res

    def gen_function_call(self, ctx):
        # functionCall : ID LPAREN argList? RPAREN
        func_name = ctx.getChild(0).getText()
        args = []
        # children: ID, LPAREN, argExpr, (COMMA,argExpr)*, RPAREN
        if ctx.getChildCount() > 3:
            # arg positions 2,4,6,...
            for i in range(2, ctx.getChildCount() - 1, 2):
                arg_ctx = ctx.getChild(i)
                arg_operand = self.gen_any_expr(arg_ctx)
                args.append(arg_operand)
        res = self.new_temp()
        # arg2 guarda la lista de operandos (lista de strings o temps)
        self.add_instruction('call', arg1=func_name, arg2=args, result=res)
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
            elif op == 'ret':
                output += f"  ret {inst['arg1']}\n"
            elif op == 'call':
                args_repr = ", ".join(map(str, inst['arg2'] or []))
                output += f"  {inst['result']} = call {inst['arg1']}({args_repr})\n"
            elif isinstance(op, str) and op.endswith(':'):
                output += f"{op}\n"
            else:
                output += f"  {op} {inst.get('arg1', '')} {inst.get('arg2', '')} {inst.get('result', '')}\n"
        return output