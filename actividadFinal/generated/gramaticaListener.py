# Generated from gramatica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gramaticaParser import gramaticaParser
else:
    from gramaticaParser import gramaticaParser

# This class defines a complete listener for a parse tree produced by gramaticaParser.
class gramaticaListener(ParseTreeListener):

    # Enter a parse tree produced by gramaticaParser#program.
    def enterProgram(self, ctx:gramaticaParser.ProgramContext):
        pass

    # Exit a parse tree produced by gramaticaParser#program.
    def exitProgram(self, ctx:gramaticaParser.ProgramContext):
        pass


    # Enter a parse tree produced by gramaticaParser#statement.
    def enterStatement(self, ctx:gramaticaParser.StatementContext):
        pass

    # Exit a parse tree produced by gramaticaParser#statement.
    def exitStatement(self, ctx:gramaticaParser.StatementContext):
        pass


    # Enter a parse tree produced by gramaticaParser#assignment.
    def enterAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by gramaticaParser#assignment.
    def exitAssignment(self, ctx:gramaticaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by gramaticaParser#printStmt.
    def enterPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#printStmt.
    def exitPrintStmt(self, ctx:gramaticaParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#ifStmt.
    def enterIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#ifStmt.
    def exitIfStmt(self, ctx:gramaticaParser.IfStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#whileStmt.
    def enterWhileStmt(self, ctx:gramaticaParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by gramaticaParser#whileStmt.
    def exitWhileStmt(self, ctx:gramaticaParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by gramaticaParser#block.
    def enterBlock(self, ctx:gramaticaParser.BlockContext):
        pass

    # Exit a parse tree produced by gramaticaParser#block.
    def exitBlock(self, ctx:gramaticaParser.BlockContext):
        pass


    # Enter a parse tree produced by gramaticaParser#boolExpr.
    def enterBoolExpr(self, ctx:gramaticaParser.BoolExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#boolExpr.
    def exitBoolExpr(self, ctx:gramaticaParser.BoolExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#boolTerm.
    def enterBoolTerm(self, ctx:gramaticaParser.BoolTermContext):
        pass

    # Exit a parse tree produced by gramaticaParser#boolTerm.
    def exitBoolTerm(self, ctx:gramaticaParser.BoolTermContext):
        pass


    # Enter a parse tree produced by gramaticaParser#boolFactor.
    def enterBoolFactor(self, ctx:gramaticaParser.BoolFactorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#boolFactor.
    def exitBoolFactor(self, ctx:gramaticaParser.BoolFactorContext):
        pass


    # Enter a parse tree produced by gramaticaParser#comparison.
    def enterComparison(self, ctx:gramaticaParser.ComparisonContext):
        pass

    # Exit a parse tree produced by gramaticaParser#comparison.
    def exitComparison(self, ctx:gramaticaParser.ComparisonContext):
        pass


    # Enter a parse tree produced by gramaticaParser#compOp.
    def enterCompOp(self, ctx:gramaticaParser.CompOpContext):
        pass

    # Exit a parse tree produced by gramaticaParser#compOp.
    def exitCompOp(self, ctx:gramaticaParser.CompOpContext):
        pass


    # Enter a parse tree produced by gramaticaParser#arithExpr.
    def enterArithExpr(self, ctx:gramaticaParser.ArithExprContext):
        pass

    # Exit a parse tree produced by gramaticaParser#arithExpr.
    def exitArithExpr(self, ctx:gramaticaParser.ArithExprContext):
        pass


    # Enter a parse tree produced by gramaticaParser#arithTerm.
    def enterArithTerm(self, ctx:gramaticaParser.ArithTermContext):
        pass

    # Exit a parse tree produced by gramaticaParser#arithTerm.
    def exitArithTerm(self, ctx:gramaticaParser.ArithTermContext):
        pass


    # Enter a parse tree produced by gramaticaParser#arithFactor.
    def enterArithFactor(self, ctx:gramaticaParser.ArithFactorContext):
        pass

    # Exit a parse tree produced by gramaticaParser#arithFactor.
    def exitArithFactor(self, ctx:gramaticaParser.ArithFactorContext):
        pass



del gramaticaParser