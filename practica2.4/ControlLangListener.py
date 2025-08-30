# Generated from ControlLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ControlLangParser import ControlLangParser
else:
    from ControlLangParser import ControlLangParser

# This class defines a complete listener for a parse tree produced by ControlLangParser.
class ControlLangListener(ParseTreeListener):

    # Enter a parse tree produced by ControlLangParser#programa.
    def enterPrograma(self, ctx:ControlLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ControlLangParser#programa.
    def exitPrograma(self, ctx:ControlLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ControlLangParser#sentencia.
    def enterSentencia(self, ctx:ControlLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by ControlLangParser#sentencia.
    def exitSentencia(self, ctx:ControlLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by ControlLangParser#IfElse.
    def enterIfElse(self, ctx:ControlLangParser.IfElseContext):
        pass

    # Exit a parse tree produced by ControlLangParser#IfElse.
    def exitIfElse(self, ctx:ControlLangParser.IfElseContext):
        pass


    # Enter a parse tree produced by ControlLangParser#for.
    def enterFor(self, ctx:ControlLangParser.ForContext):
        pass

    # Exit a parse tree produced by ControlLangParser#for.
    def exitFor(self, ctx:ControlLangParser.ForContext):
        pass


    # Enter a parse tree produced by ControlLangParser#switch.
    def enterSwitch(self, ctx:ControlLangParser.SwitchContext):
        pass

    # Exit a parse tree produced by ControlLangParser#switch.
    def exitSwitch(self, ctx:ControlLangParser.SwitchContext):
        pass


    # Enter a parse tree produced by ControlLangParser#CondicionSimple.
    def enterCondicionSimple(self, ctx:ControlLangParser.CondicionSimpleContext):
        pass

    # Exit a parse tree produced by ControlLangParser#CondicionSimple.
    def exitCondicionSimple(self, ctx:ControlLangParser.CondicionSimpleContext):
        pass


    # Enter a parse tree produced by ControlLangParser#Assign.
    def enterAssign(self, ctx:ControlLangParser.AssignContext):
        pass

    # Exit a parse tree produced by ControlLangParser#Assign.
    def exitAssign(self, ctx:ControlLangParser.AssignContext):
        pass


    # Enter a parse tree produced by ControlLangParser#Variable.
    def enterVariable(self, ctx:ControlLangParser.VariableContext):
        pass

    # Exit a parse tree produced by ControlLangParser#Variable.
    def exitVariable(self, ctx:ControlLangParser.VariableContext):
        pass


    # Enter a parse tree produced by ControlLangParser#MulDiv.
    def enterMulDiv(self, ctx:ControlLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by ControlLangParser#MulDiv.
    def exitMulDiv(self, ctx:ControlLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by ControlLangParser#AddSub.
    def enterAddSub(self, ctx:ControlLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by ControlLangParser#AddSub.
    def exitAddSub(self, ctx:ControlLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by ControlLangParser#Parens.
    def enterParens(self, ctx:ControlLangParser.ParensContext):
        pass

    # Exit a parse tree produced by ControlLangParser#Parens.
    def exitParens(self, ctx:ControlLangParser.ParensContext):
        pass


    # Enter a parse tree produced by ControlLangParser#Int.
    def enterInt(self, ctx:ControlLangParser.IntContext):
        pass

    # Exit a parse tree produced by ControlLangParser#Int.
    def exitInt(self, ctx:ControlLangParser.IntContext):
        pass



del ControlLangParser