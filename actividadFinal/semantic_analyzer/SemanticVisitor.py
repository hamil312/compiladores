from antlr4 import TerminalNode
from generated.gramaticaVisitor import gramaticaVisitor
from generated.gramaticaParser import gramaticaParser
from .SymbolTable import SymbolTable
from .IR_Generator import IR_Generator

class SemanticVisitor(gramaticaVisitor):
    def __init__(self):
        self.table = SymbolTable()
        self.ir = IR_Generator()

    # Programa: primero registrar/visitar definiciones de función, luego statements globales
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        # registrar/visitar funciones
        for f in ctx.functionDef():
            self.visit(f)
        # luego statements globales
        for st in ctx.statement():
            self.visit(st)
        return None

    # Funciones
    def visitFunctionDef(self, ctx:gramaticaParser.FunctionDefContext):
        name = ctx.ID().getText()
        # returnType text normalizado
        rt_txt = ctx.returnType().getText().lower()
        return_type = 'int' if 'int' in rt_txt else 'bool'

        # parámetros
        params = []
        if ctx.paramList():
            for p in ctx.paramList().param():
                pname = p.ID().getText()
                ptype_txt = p.paramType().getText().lower()
                ptype = 'int' if 'int' in ptype_txt else 'bool'
                params.append((pname, ptype))

        # registrar función en la tabla global
        self.table.define_function(name, return_type=return_type, params=params)

        # preparar scope de función y parámetros
        self.table.enter_scope(name=f"func:{name}", is_function=True, function_name=name)
        self.table.set_expected_return_type(return_type)
        # insertar parámetros como variables del scope de la función
        for pname, ptype in params:
            self.table.define_var(pname, var_type=ptype)

        # emitir etiqueta inicio de función en IR
        self.ir.emit_label(f"func_{name}")

        # visitar cuerpo (statements)
        for st in ctx.statement():
            self.visit(st)

        # visitar returnStmt (si existe)
        if ctx.returnStmt():
            self.visit(ctx.returnStmt())

        # emitir etiqueta fin de función en IR
        self.ir.emit_label(f"end_func_{name}")

        # salir del scope de la función
        self.table.exit_scope()
        return None

    # returnStmt : RETURN (boolExpr | arithExpr) SEMI
    def visitReturnStmt(self, ctx:gramaticaParser.ReturnStmtContext):
        # protección: asegurar que el nodo y su hijo 1 existan
        if ctx is None or ctx.getChildCount() < 2:
            self.table.record_error("Sentencia 'return' inválida o incompleta.")
            return None

        expr_ctx = ctx.getChild(1)
        res = self.visit(expr_ctx)
        if res is None:
            expr_type, expr_addr = ('error_type', None)
        else:
            expr_type, expr_addr = res

        # validar tipo de retorno con la tabla
        self.table.validate_return_type(expr_type)

        # generar IR ret + salto al final de función
        self.ir.add_instruction('ret', arg1=expr_addr)
        # la etiqueta de fin fue emitida por visitFunctionDef; aquí emitimos goto al final
        # asumimos convención end_func_<name>
        if self.table.current_function:
            self.ir.add_instruction('goto', result=f"end_func_{self.table.current_function}")
        return None

    # Statement dispatcher (añadimos varDecl y functionDef handling ya en visitProgram)
    def visitStatement(self, ctx:gramaticaParser.StatementContext):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.printStmt():
            return self.visit(ctx.printStmt())
        if ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        if ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        if ctx.block():
            return self.visit(ctx.block())
        if ctx.varDecl():
            return self.visit(ctx.varDecl())
        return None

    # varDecl : VAR ID (COLON varType)? (ASSIGN (boolExpr | arithExpr))? SEMI
    def visitVarDecl(self, ctx:gramaticaParser.VarDeclContext):
        name = ctx.ID().getText()
        declared_type = None
        if ctx.varType():
            t = ctx.varType().getText().lower()
            declared_type = 'int' if 'int' in t else 'bool'
        # definir variable en scope actual
        self.table.define_var(name, var_type=declared_type)

        # si hay asignación, visitar RHS y chequear tipos
        if ctx.ASSIGN():
            # localizar expresión (la gramática ya garantiza posición pero usamos child search)
            # child after ASSIGN is expression
            for i in range(ctx.getChildCount()):
                if ctx.getChild(i).getText() == '=':
                    rhs_ctx = ctx.getChild(i+1)
                    res = self.visit(rhs_ctx)
                    if res:
                        expr_type, expr_addr = res
                        if declared_type is not None and expr_type != 'error_type' and expr_type != declared_type:
                            self.table.record_error(f"Inicialización de '{name}' espera {declared_type}, pero se obtuvo {expr_type}.")
                        # si no declarado, fijar tipo por inferencia
                        if declared_type is None and expr_type not in (None, 'error_type'):
                            self.table.set_var_type(name, expr_type)
                        # generar IR de asignación
                        self.ir.add_instruction('=', arg1=expr_addr, result=name)
                    break
        return None

    # assignment : ID ASSIGN (boolExpr | arithExpr) SEMI
    def visitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        var_name = ctx.ID().getText()
        # Determinar RHS
        rhs_ctx = ctx.getChild(2)
        result = self.visit(rhs_ctx)
        if result is None:
            return None
        expr_type, expr_addr = result

        # Registrar/chequear tipo en la tabla (crea implícitamente si no existe)
        self.table.set_var_type(var_name, expr_type)

        # Generar IR de asignación
        self.ir.add_instruction('=', expr_addr, result=var_name)
        return None

    # printStmt : PRINT LPAREN ID RPAREN SEMI
    def visitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        # Caso: print(variable)
        if ctx.ID():
            id_name = ctx.ID().getText()
            sym = self.table.lookup(id_name)
            if sym is None:
                self.table.record_error(f"La variable '{id_name}' no ha sido declarada antes de usar en print.")
            self.ir.add_instruction('print', arg1=id_name)
            return None

        # Caso: print(literal int)
        if ctx.INT():
            self.ir.add_instruction('print', arg1=ctx.INT().getText())
            return None

        # Fallback: intentar evaluar la expresión si la gramática cambia
        # (protección contra None)
        if ctx.getChildCount() > 2:
            child = ctx.getChild(2)
            res = self.visit(child)
            if res:
                _, addr = res
                self.ir.add_instruction('print', arg1=addr)
                return None

        self.table.record_error("Argumento inválido en 'print'.")
        return None

    # ifStmt : IF LPAREN boolExpr RPAREN block (ELSE block)?
    def visitIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        cond_res = self.visit(ctx.boolExpr())
        if cond_res is None:
            cond_type, cond_addr = ('error_type', None)
        else:
            cond_type, cond_addr = cond_res

        if cond_type != 'bool' and cond_type != 'error_type':
            self.table.record_error("Condición del 'if' debe ser booleana.")

        else_label = self.ir.new_label()
        end_label = self.ir.new_label()
        target_label = else_label if ctx.ELSE() else end_label

        self.ir.add_instruction('if_false_goto', arg1=cond_addr, result=target_label)

        # THEN block
        self.table.enter_scope()
        self.visit(ctx.block(0))
        self.table.exit_scope()

        if ctx.ELSE():
            self.ir.add_instruction('goto', result=end_label)
            self.ir.emit_label(else_label)
            self.table.enter_scope()
            self.visit(ctx.block(1))
            self.table.exit_scope()

        self.ir.emit_label(end_label)
        return None

    # whileStmt : WHILE LPAREN boolExpr RPAREN block
    def visitWhileStmt(self, ctx:gramaticaParser.WhileStmtContext):
        start = self.ir.new_label()
        end = self.ir.new_label()

        # Emitir etiqueta del inicio del loop
        self.ir.emit_label(start)
        
        # Evaluar condición DENTRO del loop (se re-evalúa cada iteración)
        cond_ctx = ctx.boolExpr()
        cond_res = self.visit(cond_ctx)
        if cond_res is None:
            cond_type, cond_addr = ('error_type', None)
        else:
            cond_type, cond_addr = cond_res

        if cond_type != 'bool' and cond_type != 'error_type':
            self.table.record_error("Condición del 'while' debe ser booleana.")

        # Si condición es falsa, saltar al final
        self.ir.add_instruction('if_false_goto', arg1=cond_addr, result=end)
        
        # Cuerpo del loop
        self.table.enter_scope()
        self.visit(ctx.block())
        self.table.exit_scope()
        
        # Saltar de vuelta al inicio (para re-evaluar condición)
        self.ir.add_instruction('goto', result=start)
        
        # Etiqueta del final
        self.ir.emit_label(end)
        return None

    # block : LBRACE statement* RBRACE
    def visitBlock(self, ctx:gramaticaParser.BlockContext):
        for st in ctx.statement():
            self.visit(st)
        return None

    # ---------- EXPRESIONES ----------
    # visitFunctionCall: devuelve (tipo, operando)
    def visitFunctionCall(self, ctx:gramaticaParser.FunctionCallContext):
        func_name = ctx.ID().getText()
        arg_types = []
        arg_addrs = []
        # si hay argList
        if ctx.argList():
            # argList puede contener boolExpr or arithExpr alternating with commas
            # recorrer children of argList through its visit
            # el parser coloca las expresiones como hijos directos en argList
            for i in range(ctx.argList().getChildCount()):
                child = ctx.argList().getChild(i)
                if child.getText() == ',':
                    continue
                res = self.visit(child)
                if res is None:
                    arg_types.append('error_type')
                    arg_addrs.append(None)
                else:
                    t, a = res
                    arg_types.append(t)
                    arg_addrs.append(a)

        # validar llamada en tabla de símbolos
        ret_type = self.table.validate_function_call(func_name, arg_types)
        # generar IR call
        res_temp = self.ir.new_temp()
        self.ir.add_instruction('call', arg1=func_name, arg2=arg_addrs, result=res_temp)
        return (ret_type, res_temp)

    # boolExpr : boolExpr OR boolTerm | boolTerm
    def visitBoolExpr(self, ctx:gramaticaParser.BoolExprContext):
        if ctx.getChildCount() == 3:
            left_type, left_addr = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText().lower()
            right_type, right_addr = self.visit(ctx.getChild(2))

            if left_type == 'error_type' or right_type == 'error_type':
                return ('error_type', None)
            if left_type != 'bool' or right_type != 'bool':
                self.table.record_error("Operador OR requiere operandos booleanos.")
                return ('error_type', None)

            temp = self.ir.new_temp()
            self.ir.add_instruction('or', left_addr, right_addr, temp)
            return ('bool', temp)
        else:
            return self.visit(ctx.getChild(0))

    # boolTerm : boolTerm AND boolFactor | boolFactor
    def visitBoolTerm(self, ctx:gramaticaParser.BoolTermContext):
        if ctx.getChildCount() == 3:
            left_type, left_addr = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText().lower()
            right_type, right_addr = self.visit(ctx.getChild(2))

            if left_type == 'error_type' or right_type == 'error_type':
                return ('error_type', None)
            if left_type != 'bool' or right_type != 'bool':
                self.table.record_error("Operador AND requiere operandos booleanos.")
                return ('error_type', None)

            temp = self.ir.new_temp()
            self.ir.add_instruction('and', left_addr, right_addr, temp)
            return ('bool', temp)
        else:
            return self.visit(ctx.getChild(0))

    # boolFactor : NOT boolFactor | LPAREN boolExpr RPAREN | TRUE | FALSE | ID | comparison | functionCall
    def visitBoolFactor(self, ctx:gramaticaParser.BoolFactorContext):
        if ctx is None:
            return ('error_type', None)

        # NOT case
        if ctx.getChildCount() >= 2:
            first_child = ctx.getChild(0)
            if first_child is not None and first_child.getText() in ('not', 'NOT', '!'):
                inner = ctx.getChild(1)
                inner_type, inner_addr = self.visit(inner) if inner is not None else ('error_type', None)
                if inner_type != 'bool' and inner_type != 'error_type':
                    self.table.record_error("Operador NOT requiere operando booleano.")
                    return ('error_type', None)
                temp = self.ir.new_temp()
                # not x -> x == 0
                self.ir.add_instruction('==', inner_addr, '0', temp)
                return ('bool', temp)

        # parenthesis
        if ctx.getChildCount() == 3 and ctx.getChild(0) is not None and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))

        # TRUE / FALSE
        if ctx.TRUE() or ctx.FALSE():
            first = ctx.getChild(0)
            txt = first.getText().lower() if first is not None else 'false'
            return ('bool', '1' if txt == 'true' else '0')

        # functionCall
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # comparison
        if ctx.comparison():
            return self.visit(ctx.comparison())

        # ID (variable - puede ser bool o int si viene de función que retorna bool)
        if ctx.ID():
            name = ctx.ID().getText()
            sym = self.table.lookup(name)
            if sym is None:
                self.table.record_error(f"La variable '{name}' no ha sido declarada.")
                return ('error_type', None)
            if sym.category == 'function':
                # si una función sin paréntesis fue usada, error
                self.table.record_error(f"El identificador '{name}' es una función; llámala con paréntesis si quieres usar su valor.")
                return ('error_type', None)
            
            # Si el tipo es desconocido, no forzar bool: devolver el tipo conocido o 'error_type'
            if sym.type is None:
                # no inferir automáticamente; marcar error si se usa en contexto booleano
                self.table.record_error(f"Uso de '{name}' en contexto booleano, tipo no conocido.")
                return ('error_type', None)
            
            return (sym.type, name)

        return ('error_type', None)

    # comparison : arithExpr compOp arithExpr
    def visitComparison(self, ctx:gramaticaParser.ComparisonContext):
        left_type, left_addr = self.visit(ctx.getChild(0))
        op = ctx.getChild(1).getText()
        right_type, right_addr = self.visit(ctx.getChild(2))

        if left_type == 'error_type' or right_type == 'error_type':
            return ('error_type', None)
        if left_type != 'int' or right_type != 'int':
            self.table.record_error("Comparación requiere operandos numéricos (int).")
            return ('error_type', None)

        temp = self.ir.new_temp()
        self.ir.add_instruction(op, left_addr, right_addr, temp)
        return ('bool', temp)

    # arithExpr : arithExpr ADD arithTerm | arithExpr SUB arithTerm | arithTerm
    def visitArithExpr(self, ctx:gramaticaParser.ArithExprContext):
        if ctx.getChildCount() == 3:
            left_type, left_addr = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right_type, right_addr = self.visit(ctx.getChild(2))

            if left_type == 'error_type' or right_type == 'error_type':
                return ('error_type', None)
            if left_type != 'int' or right_type != 'int':
                self.table.record_error(f"Operador '{op}' requiere operandos int.")
                return ('error_type', None)

            temp = self.ir.new_temp()
            self.ir.add_instruction(op, left_addr, right_addr, temp)
            return ('int', temp)
        else:
            return self.visit(ctx.getChild(0))

    # arithTerm : arithTerm MUL arithFactor | arithTerm DIV arithFactor | arithFactor
    def visitArithTerm(self, ctx:gramaticaParser.ArithTermContext):
        if ctx.getChildCount() == 3:
            left_type, left_addr = self.visit(ctx.getChild(0))
            op = ctx.getChild(1).getText()
            right_type, right_addr = self.visit(ctx.getChild(2))

            if left_type == 'error_type' or right_type == 'error_type':
                return ('error_type', None)
            if left_type != 'int' or right_type != 'int':
                self.table.record_error(f"Operador '{op}' requiere operandos int.")
                return ('error_type', None)

            temp = self.ir.new_temp()
            self.ir.add_instruction(op, arg1=left_addr, arg2=right_addr, result=temp)
            return ('int', temp)
        else:
            return self.visit(ctx.getChild(0))

    # arithFactor : SUB arithFactor | LPAREN arithExpr RPAREN | INT | ID | functionCall
    def visitArithFactor(self, ctx:gramaticaParser.ArithFactorContext):
        if ctx is None:
            return ('error_type', None)
            
        child_count = ctx.getChildCount()
        
        # unary minus
        if child_count == 2:
            first = ctx.getChild(0)
            if first is not None and first.getText() == '-':
                inner = ctx.getChild(1)
                inner_type, inner_addr = self.visit(inner) if inner is not None else ('error_type', None)
                if inner_type != 'int' and inner_type != 'error_type':
                    self.table.record_error("Operador unary '-' requiere operando int.")
                    return ('error_type', None)
                temp = self.ir.new_temp()
                self.ir.add_instruction('-', '0', inner_addr, temp)
                return ('int', temp)

        # parenthesis
        if child_count == 3:
            first = ctx.getChild(0)
            if first is not None and first.getText() == '(':
                return self.visit(ctx.getChild(1))

        # INT literal
        if ctx.INT():
            return ('int', ctx.INT().getText())

        # functionCall
        if ctx.functionCall():
            return self.visit(ctx.functionCall())

        # ID (numeric variable)
        if ctx.ID():
            name = ctx.ID().getText()
            sym = self.table.lookup(name)
            if sym is None:
                self.table.record_error(f"La variable '{name}' no ha sido declarada.")
                return ('error_type', None)
            if sym.category == 'function':
                self.table.record_error(f"El identificador '{name}' es una función, use paréntesis para llamarla.")
                return ('error_type', None)
            if sym.type is None:
                sym.type = 'int'
            if sym.type != 'int':
                self.table.record_error(f"La variable '{name}' no es de tipo int.")
                return ('error_type', None)
            return ('int', name)

        return ('error_type', None)