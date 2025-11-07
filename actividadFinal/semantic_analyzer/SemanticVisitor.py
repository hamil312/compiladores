from antlr4 import TerminalNode
from generated.gramaticaVisitor import gramaticaVisitor
from generated.gramaticaParser import gramaticaParser
from .SymbolTable import SymbolTable
from .IR_Generator import IR_Generator

class SemanticVisitor(gramaticaVisitor):
    def __init__(self):
        self.table = SymbolTable()
        self.ir = IR_Generator()

    # Programa: visitar statements
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        for st in ctx.statement():
            self.visit(st)
        return None

    # Statement dispatcher
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
        return None

    # assignment : ID ASSIGN (boolExpr | arithExpr) SEMI
    def visitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        var_name = ctx.ID().getText()
        # Determinar si la RHS es boolean o aritmética
        rhs_ctx = ctx.getChild(2)
        result = self.visit(rhs_ctx)
        if result is None:
            # error ya reportado en la visita
            return None
        expr_type, expr_addr = result

        # Registrar/chequear tipo en la tabla (crea implícitamente si no existe)
        self.table.set_var_type(var_name, expr_type)

        # Generar IR de asignación
        self.ir.add_instruction('=', expr_addr, result=var_name)
        return None

    # printStmt : PRINT LPAREN ID RPAREN SEMI
    def visitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        id_name = ctx.ID().getText()
        sym = self.table.lookup(id_name)
        if sym is None:
            self.table.record_error(f"La variable '{id_name}' no ha sido declarada antes de usar en print.")
        self.ir.add_instruction('print', id_name)
        return None

    # ifStmt : IF LPAREN boolExpr RPAREN block (ELSE block)?
    def visitIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        cond_ctx = ctx.getChild(2)
        cond_res = self.visit(cond_ctx)
        if cond_res is None:
            cond_type, cond_addr = ('error_type', None)
        else:
            cond_type, cond_addr = cond_res

        if cond_type != 'bool' and cond_type != 'error_type':
            self.table.record_error("Condición del 'if' debe ser booleana.")

        else_label = self.ir.new_label()
        end_label = self.ir.new_label()
        target_label = else_label if ctx.ELSE() else end_label

        self.ir.add_instruction('if_false_goto', cond_addr, result=target_label)

        # THEN block (block is child 4)
        self.table.enter_scope()
        self.visit(ctx.block(0))
        self.table.exit_scope()

        if ctx.ELSE():
            self.ir.add_instruction('goto', result=end_label)
            self.ir.add_instruction(f"{else_label}:")
            self.table.enter_scope()
            self.visit(ctx.block(1))
            self.table.exit_scope()

        self.ir.add_instruction(f"{end_label}:")
        return None

    # whileStmt : WHILE LPAREN boolExpr RPAREN block
    def visitWhileStmt(self, ctx:gramaticaParser.WhileStmtContext):
        cond_ctx = ctx.getChild(2)
        start = self.ir.new_label()
        end = self.ir.new_label()

        self.ir.add_instruction(f"{start}:")
        cond_res = self.visit(cond_ctx)
        if cond_res is None:
            cond_type, cond_addr = ('error_type', None)
        else:
            cond_type, cond_addr = cond_res

        if cond_type != 'bool' and cond_type != 'error_type':
            self.table.record_error("Condición del 'while' debe ser booleana.")

        self.ir.add_instruction('if_false_goto', cond_addr, result=end)
        self.table.enter_scope()
        self.visit(ctx.block())
        self.table.exit_scope()
        self.ir.add_instruction('goto', result=start)
        self.ir.add_instruction(f"{end}:")
        return None

    # block : LBRACE statement* RBRACE
    def visitBlock(self, ctx:gramaticaParser.BlockContext):
        for st in ctx.statement():
            self.visit(st)
        return None

    # ---------- EXPRESIONES ----------

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

    # boolFactor : NOT boolFactor | LPAREN boolExpr RPAREN | TRUE | FALSE | ID | comparison
    def visitBoolFactor(self, ctx:gramaticaParser.BoolFactorContext):
        # NOT case
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() in ('not', 'NOT', '!'):
            inner_type, inner_addr = self.visit(ctx.getChild(1))
            if inner_type != 'bool' and inner_type != 'error_type':
                self.table.record_error("Operador NOT requiere operando booleano.")
                return ('error_type', None)
            temp = self.ir.new_temp()
            # not x -> x == 0
            self.ir.add_instruction('==', inner_addr, '0', temp)
            return ('bool', temp)

        # parenthesis
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))

        # TRUE / FALSE
        if ctx.TRUE() or ctx.FALSE():
            txt = ctx.getChild(0).getText().lower()
            return ('bool', '1' if txt == 'true' else '0')

        # ID (boolean variable)
        if ctx.ID():
            name = ctx.ID().getText()
            sym = self.table.lookup(name)
            if sym is None:
                self.table.record_error(f"La variable '{name}' no ha sido declarada.")
                return ('error_type', None)
            if sym.category == 'function':
                self.table.record_error(f"El identificador '{name}' es una función, no booleano.")
                return ('error_type', None)
            if sym.type != 'bool' and sym.type is not None:
                self.table.record_error(f"La variable '{name}' no es booleana.")
                return ('error_type', None)
            # si sym.type es None, asumimos boolean por uso en contexto booleano
            if sym.type is None:
                sym.type = 'bool'
            return ('bool', name)

        # comparison
        if ctx.comparison():
            return self.visit(ctx.comparison())

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
            self.ir.add_instruction(op, left_addr, right_addr, temp)
            return ('int', temp)
        else:
            return self.visit(ctx.getChild(0))

    # arithFactor : SUB arithFactor | LPAREN arithExpr RPAREN | INT | ID
    def visitArithFactor(self, ctx:gramaticaParser.ArithFactorContext):
        # unary minus
        if ctx.getChildCount() == 2 and ctx.getChild(0).getText() == '-':
            inner_type, inner_addr = self.visit(ctx.getChild(1))
            if inner_type != 'int' and inner_type != 'error_type':
                self.table.record_error("Operador unary '-' requiere operando int.")
                return ('error_type', None)
            temp = self.ir.new_temp()
            self.ir.add_instruction('-', '0', inner_addr, temp)
            return ('int', temp)

        # parenthesis
        if ctx.getChildCount() == 3 and ctx.getChild(0).getText() == '(':
            return self.visit(ctx.getChild(1))

        # INT literal
        if ctx.INT():
            return ('int', ctx.INT().getText())

        # ID (numeric variable)
        if ctx.ID():
            name = ctx.ID().getText()
            sym = self.table.lookup(name)
            if sym is None:
                self.table.record_error(f"La variable '{name}' no ha sido declarada.")
                return ('error_type', None)
            if sym.category == 'function':
                self.table.record_error(f"El identificador '{name}' es una función, no int.")
                return ('error_type', None)
            if sym.type is None:
                # asumimos int por uso numérico
                sym.type = 'int'
            if sym.type != 'int':
                self.table.record_error(f"La variable '{name}' no es de tipo int.")
                return ('error_type', None)
            return ('int', name)

        return ('error_type', None)