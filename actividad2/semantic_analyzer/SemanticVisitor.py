from generated.WhileLangVisitor import WhileLangVisitor
from generated.WhileLangParser import WhileLangParser
from .SymbolTable import SymbolTable, Symbol

class SemanticVisitor(WhileLangVisitor):
    def __init__(self):
        self.table = SymbolTable()
        self.loop_stack = []

    # Declaración de variables
    def visitDeclaration(self, ctx:WhileLangParser.DeclarationContext):
        var_name = ctx.ID().getText()
        type_name = ctx.type_().getText()
        self.table.insert(var_name, Symbol(var_name, type_name))
        return self.visitChildren(ctx)

    # Asignación
    def visitAssignment(self, ctx:WhileLangParser.AssignmentContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)

        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' a la que se intenta asignar no ha sido declarada.")
            return None

        expr_type = self.visit(ctx.expr())

        if expr_type != 'error_type' and expr_type is not None and symbol.type != expr_type:
            print(f"Error Semántico: No se puede asignar tipo '{expr_type}' a variable '{var_name}' de tipo '{symbol.type}'.")
        return None

    # Expresión: identificador
    def visitIdExpr(self, ctx:WhileLangParser.IdExprContext):
        var_name = ctx.ID().getText()
        symbol = self.table.lookup(var_name)
        if symbol is None:
            print(f"Error Semántico: La variable '{var_name}' no ha sido declarada.")
            return 'error_type'
        return symbol.type

    # Expresión: número
    def visitNumberExpr(self, ctx:WhileLangParser.NumberExprContext):
        return 'int'

    # Expresión: comparación
    def visitComparisonExpr(self, ctx:WhileLangParser.ComparisonExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'

        if left_type != right_type:
            print(f"Error Semántico: Comparación entre tipos incompatibles ({left_type} vs {right_type}).")
            return 'error_type'

        if op in ('<', '>', '<=', '>='):
            if left_type != 'int':
                print(f"Error Semántico: Operador '{op}' no soportado para tipo '{left_type}'.")
                return 'error_type'

        elif op in ('==', '!='):
            if left_type not in ('int', 'string'):
                print(f"Error Semántico: Operador '{op}' no soportado para tipo '{left_type}'.")
                return 'error_type'

        return 'int'  # tratamos el booleano como int simple

    # Expresión: aritmética
    def visitArithmeticExpr(self, ctx:WhileLangParser.ArithmeticExprContext):
        left_type = self.visit(ctx.expr(0))
        right_type = self.visit(ctx.expr(1))
        op = ctx.getChild(1).getText()

        if left_type == 'error_type' or right_type == 'error_type':
            return 'error_type'
        
        if left_type == 'string' and right_type == 'string' and op == '+':
            return 'string'

        if left_type != 'int' or right_type != 'int':
            print(f"Error Semántico: Operación aritmética solo permitida con enteros, no con {left_type} y {right_type}.")
            return 'error_type'

        return 'int'

    # Expresión: paréntesis
    def visitParenExpr(self, ctx:WhileLangParser.ParenExprContext):
        return self.visit(ctx.expr())

    # If con scopes separados
    def visitIfStatement(self, ctx:WhileLangParser.IfStatementContext):
        cond_type = self.visit(ctx.condition())

        if cond_type == 'error_type':
            pass
        elif cond_type not in ('int', 'string'):
            print(f"Error Semántico: Condición inválida de tipo '{cond_type}'.")

        # THEN
        self.table.enter_scope()
        for stmt in ctx.statement()[:len(ctx.statement()) // (2 if ctx.ELSE() else 1)]:
            self.visit(stmt)
        self.table.exit_scope()

        # ELSE
        if ctx.ELSE():
            self.table.enter_scope()
            for stmt in ctx.statement()[len(ctx.statement()) // 2:]:
                self.visit(stmt)
            self.table.exit_scope()
    
    def visitWhileStatement(self, ctx:WhileLangParser.WhileStatementContext):
        cond_type = self.visit(ctx.condition())

        if cond_type == 'error_type':
            pass
        elif cond_type not in ('int', 'string'):
            print(f"Error Semántico: Condición inválida de tipo '{cond_type}'.")

        self.loop_stack.append(True)

        # Nuevo ámbito para el cuerpo del while
        self.table.enter_scope()
        for stmt in ctx.statement():
            self.visit(stmt)
        self.table.exit_scope()

        self.loop_stack.pop()

    
    def visitStringExpr(self, ctx:WhileLangParser.StringExprContext):
        return 'string'
    
    def visitExprCondition(self, ctx:WhileLangParser.ConditionContext):
        expr_type = self.visit(ctx.expr())
        if expr_type not in ('int', 'string'):
            print(f"Error Semántico: La condición solo puede ser int o string, pero se encontró '{expr_type}'.")
            return 'error_type'
        return expr_type
    
    def visitBreakStatement(self, ctx:WhileLangParser.BreakStatementContext):
        if not self.loop_stack:
            print("Error Semántico: 'break' solo puede usarse dentro de un bucle.")
        return None

    def visitContinueStatement(self, ctx:WhileLangParser.ContinueStatementContext):
        if not self.loop_stack:
            print("Error Semántico: 'continue' solo puede usarse dentro de un bucle.")
        return None