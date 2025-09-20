# Generated from IfElseLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IfElseLangParser import IfElseLangParser
else:
    from IfElseLangParser import IfElseLangParser

# This class defines a complete listener for a parse tree produced by IfElseLangParser.
class IfElseLangListener(ParseTreeListener):

    # Enter a parse tree produced by IfElseLangParser#program.
    def enterProgram(self, ctx:IfElseLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#program.
    def exitProgram(self, ctx:IfElseLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#statement.
    def enterStatement(self, ctx:IfElseLangParser.StatementContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#statement.
    def exitStatement(self, ctx:IfElseLangParser.StatementContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#assignment.
    def enterAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#assignment.
    def exitAssignment(self, ctx:IfElseLangParser.AssignmentContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#declaration.
    def enterDeclaration(self, ctx:IfElseLangParser.DeclarationContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#declaration.
    def exitDeclaration(self, ctx:IfElseLangParser.DeclarationContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#returnStatement.
    def enterReturnStatement(self, ctx:IfElseLangParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#returnStatement.
    def exitReturnStatement(self, ctx:IfElseLangParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#ifStatement.
    def enterIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#ifStatement.
    def exitIfStatement(self, ctx:IfElseLangParser.IfStatementContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#block.
    def enterBlock(self, ctx:IfElseLangParser.BlockContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#block.
    def exitBlock(self, ctx:IfElseLangParser.BlockContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#functionDecl.
    def enterFunctionDecl(self, ctx:IfElseLangParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#functionDecl.
    def exitFunctionDecl(self, ctx:IfElseLangParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#param.
    def enterParam(self, ctx:IfElseLangParser.ParamContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#param.
    def exitParam(self, ctx:IfElseLangParser.ParamContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#paramList.
    def enterParamList(self, ctx:IfElseLangParser.ParamListContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#paramList.
    def exitParamList(self, ctx:IfElseLangParser.ParamListContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#condition.
    def enterCondition(self, ctx:IfElseLangParser.ConditionContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#condition.
    def exitCondition(self, ctx:IfElseLangParser.ConditionContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#stringExpr.
    def enterStringExpr(self, ctx:IfElseLangParser.StringExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#stringExpr.
    def exitStringExpr(self, ctx:IfElseLangParser.StringExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#addExpr.
    def enterAddExpr(self, ctx:IfElseLangParser.AddExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#addExpr.
    def exitAddExpr(self, ctx:IfElseLangParser.AddExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#numberExpr.
    def enterNumberExpr(self, ctx:IfElseLangParser.NumberExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#numberExpr.
    def exitNumberExpr(self, ctx:IfElseLangParser.NumberExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#mulExpr.
    def enterMulExpr(self, ctx:IfElseLangParser.MulExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#mulExpr.
    def exitMulExpr(self, ctx:IfElseLangParser.MulExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#divExpr.
    def enterDivExpr(self, ctx:IfElseLangParser.DivExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#divExpr.
    def exitDivExpr(self, ctx:IfElseLangParser.DivExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#funcCallExpr.
    def enterFuncCallExpr(self, ctx:IfElseLangParser.FuncCallExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#funcCallExpr.
    def exitFuncCallExpr(self, ctx:IfElseLangParser.FuncCallExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#subExpr.
    def enterSubExpr(self, ctx:IfElseLangParser.SubExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#subExpr.
    def exitSubExpr(self, ctx:IfElseLangParser.SubExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#parenExpr.
    def enterParenExpr(self, ctx:IfElseLangParser.ParenExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#parenExpr.
    def exitParenExpr(self, ctx:IfElseLangParser.ParenExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#idExpr.
    def enterIdExpr(self, ctx:IfElseLangParser.IdExprContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#idExpr.
    def exitIdExpr(self, ctx:IfElseLangParser.IdExprContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#argList.
    def enterArgList(self, ctx:IfElseLangParser.ArgListContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#argList.
    def exitArgList(self, ctx:IfElseLangParser.ArgListContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#operator.
    def enterOperator(self, ctx:IfElseLangParser.OperatorContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#operator.
    def exitOperator(self, ctx:IfElseLangParser.OperatorContext):
        pass


    # Enter a parse tree produced by IfElseLangParser#type.
    def enterType(self, ctx:IfElseLangParser.TypeContext):
        pass

    # Exit a parse tree produced by IfElseLangParser#type.
    def exitType(self, ctx:IfElseLangParser.TypeContext):
        pass



del IfElseLangParser