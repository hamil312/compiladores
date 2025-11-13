# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete generic visitor for a parse tree produced by gramaticaParser.

class gramaticaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticaParser#program.
    def visitProgram(self, ctx:gramaticaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#functionDef.
    def visitFunctionDef(self, ctx:gramaticaParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#paramList.
    def visitParamList(self, ctx:gramaticaParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#param.
    def visitParam(self, ctx:gramaticaParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#paramType.
    def visitParamType(self, ctx:gramaticaParser.ParamTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#returnType.
    def visitReturnType(self, ctx:gramaticaParser.ReturnTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#returnStmt.
    def visitReturnStmt(self, ctx:gramaticaParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#statement.
    def visitStatement(self, ctx:gramaticaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#varDecl.
    def visitVarDecl(self, ctx:gramaticaParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#varType.
    def visitVarType(self, ctx:gramaticaParser.VarTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#assignment.
    def visitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#printStmt.
    def visitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#ifStmt.
    def visitIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#whileStmt.
    def visitWhileStmt(self, ctx:gramaticaParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#block.
    def visitBlock(self, ctx:gramaticaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#boolExpr.
    def visitBoolExpr(self, ctx:gramaticaParser.BoolExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#boolTerm.
    def visitBoolTerm(self, ctx:gramaticaParser.BoolTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#boolFactor.
    def visitBoolFactor(self, ctx:gramaticaParser.BoolFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#comparison.
    def visitComparison(self, ctx:gramaticaParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#compOp.
    def visitCompOp(self, ctx:gramaticaParser.CompOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#arithExpr.
    def visitArithExpr(self, ctx:gramaticaParser.ArithExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#arithTerm.
    def visitArithTerm(self, ctx:gramaticaParser.ArithTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#arithFactor.
    def visitArithFactor(self, ctx:gramaticaParser.ArithFactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#functionCall.
    def visitFunctionCall(self, ctx:gramaticaParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticaParser#argList.
    def visitArgList(self, ctx:gramaticaParser.ArgListContext):
        return self.visitChildren(ctx)



del gramaticaParser