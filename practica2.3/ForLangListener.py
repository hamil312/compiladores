# Generated from ForLang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ForLangParser import ForLangParser
else:
    from ForLangParser import ForLangParser

# This class defines a complete listener for a parse tree produced by ForLangParser.
class ForLangListener(ParseTreeListener):

    # Enter a parse tree produced by ForLangParser#programa.
    def enterPrograma(self, ctx:ForLangParser.ProgramaContext):
        pass

    # Exit a parse tree produced by ForLangParser#programa.
    def exitPrograma(self, ctx:ForLangParser.ProgramaContext):
        pass


    # Enter a parse tree produced by ForLangParser#sentencia.
    def enterSentencia(self, ctx:ForLangParser.SentenciaContext):
        pass

    # Exit a parse tree produced by ForLangParser#sentencia.
    def exitSentencia(self, ctx:ForLangParser.SentenciaContext):
        pass


    # Enter a parse tree produced by ForLangParser#IfElse.
    def enterIfElse(self, ctx:ForLangParser.IfElseContext):
        pass

    # Exit a parse tree produced by ForLangParser#IfElse.
    def exitIfElse(self, ctx:ForLangParser.IfElseContext):
        pass


    # Enter a parse tree produced by ForLangParser#CondicionSimple.
    def enterCondicionSimple(self, ctx:ForLangParser.CondicionSimpleContext):
        pass

    # Exit a parse tree produced by ForLangParser#CondicionSimple.
    def exitCondicionSimple(self, ctx:ForLangParser.CondicionSimpleContext):
        pass


    # Enter a parse tree produced by ForLangParser#Assign.
    def enterAssign(self, ctx:ForLangParser.AssignContext):
        pass

    # Exit a parse tree produced by ForLangParser#Assign.
    def exitAssign(self, ctx:ForLangParser.AssignContext):
        pass


    # Enter a parse tree produced by ForLangParser#Variable.
    def enterVariable(self, ctx:ForLangParser.VariableContext):
        pass

    # Exit a parse tree produced by ForLangParser#Variable.
    def exitVariable(self, ctx:ForLangParser.VariableContext):
        pass


    # Enter a parse tree produced by ForLangParser#MulDiv.
    def enterMulDiv(self, ctx:ForLangParser.MulDivContext):
        pass

    # Exit a parse tree produced by ForLangParser#MulDiv.
    def exitMulDiv(self, ctx:ForLangParser.MulDivContext):
        pass


    # Enter a parse tree produced by ForLangParser#AddSub.
    def enterAddSub(self, ctx:ForLangParser.AddSubContext):
        pass

    # Exit a parse tree produced by ForLangParser#AddSub.
    def exitAddSub(self, ctx:ForLangParser.AddSubContext):
        pass


    # Enter a parse tree produced by ForLangParser#Parens.
    def enterParens(self, ctx:ForLangParser.ParensContext):
        pass

    # Exit a parse tree produced by ForLangParser#Parens.
    def exitParens(self, ctx:ForLangParser.ParensContext):
        pass


    # Enter a parse tree produced by ForLangParser#Int.
    def enterInt(self, ctx:ForLangParser.IntContext):
        pass

    # Exit a parse tree produced by ForLangParser#Int.
    def exitInt(self, ctx:ForLangParser.IntContext):
        pass



del ForLangParser