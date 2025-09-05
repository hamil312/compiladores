# Generated from SwitchLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .SwitchLangParser import SwitchLangParser
else:
    from SwitchLangParser import SwitchLangParser

# This class defines a complete listener for a parse tree produced by SwitchLangParser.
class SwitchLangListener(ParseTreeListener):

    # Enter a parse tree produced by SwitchLangParser#programa.
    def enterPrograma(self, ctx:SwitchLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#programa.
    def exitPrograma(self, ctx:SwitchLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#sentencia.
    def enterSentencia(self, ctx:SwitchLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#sentencia.
    def exitSentencia(self, ctx:SwitchLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#IfElse.
    def enterIfElse(self, ctx:SwitchLangParser.IfElseContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#IfElse.
    def exitIfElse(self, ctx:SwitchLangParser.IfElseContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#CondicionSimple.
    def enterCondicionSimple(self, ctx:SwitchLangParser.CondicionSimpleContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#CondicionSimple.
    def exitCondicionSimple(self, ctx:SwitchLangParser.CondicionSimpleContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#Assign.
    def enterAssign(self, ctx:SwitchLangParser.AssignContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#Assign.
    def exitAssign(self, ctx:SwitchLangParser.AssignContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#Variable.
    def enterVariable(self, ctx:SwitchLangParser.VariableContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#Variable.
    def exitVariable(self, ctx:SwitchLangParser.VariableContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#MulDiv.
    def enterMulDiv(self, ctx:SwitchLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#MulDiv.
    def exitMulDiv(self, ctx:SwitchLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#AddSub.
    def enterAddSub(self, ctx:SwitchLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#AddSub.
    def exitAddSub(self, ctx:SwitchLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#Parens.
    def enterParens(self, ctx:SwitchLangParser.ParensContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#Parens.
    def exitParens(self, ctx:SwitchLangParser.ParensContext):
        pass


    # Enter a parse tree produced by SwitchLangParser#Int.
    def enterInt(self, ctx:SwitchLangParser.IntContext):
        pass

    # Exit a parse tree produced by SwitchLangParser#Int.
    def exitInt(self, ctx:SwitchLangParser.IntContext):
        pass



del SwitchLangParser