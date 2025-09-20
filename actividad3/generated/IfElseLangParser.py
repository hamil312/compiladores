# Generated from IfElseLang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,28,152,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,4,0,33,8,0,11,0,12,0,34,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,3,1,46,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,
        57,8,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,72,
        8,5,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,6,1,6,1,7,1,7,1,7,1,7,
        3,7,87,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,9,1,9,1,9,5,9,98,8,9,10,9,12,
        9,101,9,9,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,3,11,111,8,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,121,8,11,1,11,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,135,8,11,
        10,11,12,11,138,9,11,1,12,1,12,1,12,5,12,143,8,12,10,12,12,12,146,
        9,12,1,13,1,13,1,14,1,14,1,14,0,1,22,15,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,28,0,2,1,0,15,19,1,0,3,6,157,0,32,1,0,0,0,2,45,1,0,0,
        0,4,47,1,0,0,0,6,52,1,0,0,0,8,60,1,0,0,0,10,64,1,0,0,0,12,73,1,0,
        0,0,14,82,1,0,0,0,16,91,1,0,0,0,18,94,1,0,0,0,20,102,1,0,0,0,22,
        120,1,0,0,0,24,139,1,0,0,0,26,147,1,0,0,0,28,149,1,0,0,0,30,33,3,
        2,1,0,31,33,3,14,7,0,32,30,1,0,0,0,32,31,1,0,0,0,33,34,1,0,0,0,34,
        32,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,5,0,0,1,37,1,1,0,0,
        0,38,46,3,4,2,0,39,46,3,10,5,0,40,46,3,6,3,0,41,46,3,8,4,0,42,43,
        3,22,11,0,43,44,5,13,0,0,44,46,1,0,0,0,45,38,1,0,0,0,45,39,1,0,0,
        0,45,40,1,0,0,0,45,41,1,0,0,0,45,42,1,0,0,0,46,3,1,0,0,0,47,48,5,
        24,0,0,48,49,5,14,0,0,49,50,3,22,11,0,50,51,5,13,0,0,51,5,1,0,0,
        0,52,53,3,28,14,0,53,56,5,24,0,0,54,55,5,14,0,0,55,57,3,22,11,0,
        56,54,1,0,0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,13,0,0,59,7,1,
        0,0,0,60,61,5,1,0,0,61,62,3,22,11,0,62,63,5,13,0,0,63,9,1,0,0,0,
        64,65,5,7,0,0,65,66,5,9,0,0,66,67,3,20,10,0,67,68,5,10,0,0,68,71,
        3,12,6,0,69,70,5,8,0,0,70,72,3,12,6,0,71,69,1,0,0,0,71,72,1,0,0,
        0,72,11,1,0,0,0,73,77,5,11,0,0,74,76,3,2,1,0,75,74,1,0,0,0,76,79,
        1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,80,1,0,0,0,79,77,1,0,0,0,
        80,81,5,12,0,0,81,13,1,0,0,0,82,83,3,28,14,0,83,84,5,24,0,0,84,86,
        5,9,0,0,85,87,3,18,9,0,86,85,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,
        88,89,5,10,0,0,89,90,3,12,6,0,90,15,1,0,0,0,91,92,3,28,14,0,92,93,
        5,24,0,0,93,17,1,0,0,0,94,99,3,16,8,0,95,96,5,2,0,0,96,98,3,16,8,
        0,97,95,1,0,0,0,98,101,1,0,0,0,99,97,1,0,0,0,99,100,1,0,0,0,100,
        19,1,0,0,0,101,99,1,0,0,0,102,103,3,22,11,0,103,104,3,26,13,0,104,
        105,3,22,11,0,105,21,1,0,0,0,106,107,6,11,-1,0,107,108,5,24,0,0,
        108,110,5,9,0,0,109,111,3,24,12,0,110,109,1,0,0,0,110,111,1,0,0,
        0,111,112,1,0,0,0,112,121,5,10,0,0,113,121,5,24,0,0,114,121,5,25,
        0,0,115,121,5,26,0,0,116,117,5,9,0,0,117,118,3,22,11,0,118,119,5,
        10,0,0,119,121,1,0,0,0,120,106,1,0,0,0,120,113,1,0,0,0,120,114,1,
        0,0,0,120,115,1,0,0,0,120,116,1,0,0,0,121,136,1,0,0,0,122,123,10,
        9,0,0,123,124,5,20,0,0,124,135,3,22,11,10,125,126,10,8,0,0,126,127,
        5,21,0,0,127,135,3,22,11,9,128,129,10,7,0,0,129,130,5,22,0,0,130,
        135,3,22,11,8,131,132,10,6,0,0,132,133,5,23,0,0,133,135,3,22,11,
        7,134,122,1,0,0,0,134,125,1,0,0,0,134,128,1,0,0,0,134,131,1,0,0,
        0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,23,1,0,0,0,
        138,136,1,0,0,0,139,144,3,22,11,0,140,141,5,2,0,0,141,143,3,22,11,
        0,142,140,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,
        0,145,25,1,0,0,0,146,144,1,0,0,0,147,148,7,0,0,0,148,27,1,0,0,0,
        149,150,7,1,0,0,150,29,1,0,0,0,13,32,34,45,56,71,77,86,99,110,120,
        134,136,144
    ]

class IfElseLangParser ( Parser ):

    grammarFileName = "IfElseLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'return'", "','", "'int'", "'float'", 
                     "'void'", "'string'", "'if'", "'else'", "'('", "')'", 
                     "'{'", "'}'", "';'", "'='", "'<'", "'>'", "'>='", "'<='", 
                     "'!='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELSE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "ASSIGN", 
                      "LT", "GT", "GE", "LE", "NE", "PLUS", "MINUS", "MULT", 
                      "DIV", "ID", "NUMBER", "STRING", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_declaration = 3
    RULE_returnStatement = 4
    RULE_ifStatement = 5
    RULE_block = 6
    RULE_functionDecl = 7
    RULE_param = 8
    RULE_paramList = 9
    RULE_condition = 10
    RULE_expr = 11
    RULE_argList = 12
    RULE_operator = 13
    RULE_type = 14

    ruleNames =  [ "program", "statement", "assignment", "declaration", 
                   "returnStatement", "ifStatement", "block", "functionDecl", 
                   "param", "paramList", "condition", "expr", "argList", 
                   "operator", "type" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    IF=7
    ELSE=8
    LPAREN=9
    RPAREN=10
    LBRACE=11
    RBRACE=12
    SEMI=13
    ASSIGN=14
    LT=15
    GT=16
    GE=17
    LE=18
    NE=19
    PLUS=20
    MINUS=21
    MULT=22
    DIV=23
    ID=24
    NUMBER=25
    STRING=26
    COMMENT=27
    WS=28

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(IfElseLangParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


        def functionDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.FunctionDeclContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.FunctionDeclContext,i)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = IfElseLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 30
                    self.statement()
                    pass

                elif la_ == 2:
                    self.state = 31
                    self.functionDecl()
                    pass


                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 117441274) != 0)):
                    break

            self.state = 36
            self.match(IfElseLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(IfElseLangParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(IfElseLangParser.IfStatementContext,0)


        def declaration(self):
            return self.getTypedRuleContext(IfElseLangParser.DeclarationContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(IfElseLangParser.ReturnStatementContext,0)


        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(IfElseLangParser.SEMI, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = IfElseLangParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.assignment()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.ifStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40
                self.declaration()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 41
                self.returnStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 42
                self.expr(0)
                self.state = 43
                self.match(IfElseLangParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(IfElseLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(IfElseLangParser.SEMI, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = IfElseLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(IfElseLangParser.ID)
            self.state = 48
            self.match(IfElseLangParser.ASSIGN)
            self.state = 49
            self.expr(0)
            self.state = 50
            self.match(IfElseLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(IfElseLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)

        def SEMI(self):
            return self.getToken(IfElseLangParser.SEMI, 0)

        def ASSIGN(self):
            return self.getToken(IfElseLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = IfElseLangParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.type_()
            self.state = 53
            self.match(IfElseLangParser.ID)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 54
                self.match(IfElseLangParser.ASSIGN)
                self.state = 55
                self.expr(0)


            self.state = 58
            self.match(IfElseLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def SEMI(self):
            return self.getToken(IfElseLangParser.SEMI, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = IfElseLangParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(IfElseLangParser.T__0)
            self.state = 61
            self.expr(0)
            self.state = 62
            self.match(IfElseLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(IfElseLangParser.IF, 0)

        def LPAREN(self):
            return self.getToken(IfElseLangParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(IfElseLangParser.ConditionContext,0)


        def RPAREN(self):
            return self.getToken(IfElseLangParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.BlockContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(IfElseLangParser.ELSE, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = IfElseLangParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(IfElseLangParser.IF)
            self.state = 65
            self.match(IfElseLangParser.LPAREN)
            self.state = 66
            self.condition()
            self.state = 67
            self.match(IfElseLangParser.RPAREN)
            self.state = 68
            self.block()
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 69
                self.match(IfElseLangParser.ELSE)
                self.state = 70
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(IfElseLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(IfElseLangParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = IfElseLangParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(IfElseLangParser.LBRACE)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 117441274) != 0):
                self.state = 74
                self.statement()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(IfElseLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(IfElseLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)

        def LPAREN(self):
            return self.getToken(IfElseLangParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(IfElseLangParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(IfElseLangParser.BlockContext,0)


        def paramList(self):
            return self.getTypedRuleContext(IfElseLangParser.ParamListContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDecl" ):
                return visitor.visitFunctionDecl(self)
            else:
                return visitor.visitChildren(self)




    def functionDecl(self):

        localctx = IfElseLangParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.type_()
            self.state = 83
            self.match(IfElseLangParser.ID)
            self.state = 84
            self.match(IfElseLangParser.LPAREN)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0):
                self.state = 85
                self.paramList()


            self.state = 88
            self.match(IfElseLangParser.RPAREN)
            self.state = 89
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(IfElseLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = IfElseLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.type_()
            self.state = 92
            self.match(IfElseLangParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ParamContext,i)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = IfElseLangParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.param()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 95
                self.match(IfElseLangParser.T__1)
                self.state = 96
                self.param()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ExprContext,i)


        def operator(self):
            return self.getTypedRuleContext(IfElseLangParser.OperatorContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = IfElseLangParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.expr(0)
            self.state = 103
            self.operator()
            self.state = 104
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IfElseLangParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class StringExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(IfElseLangParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStringExpr" ):
                listener.enterStringExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStringExpr" ):
                listener.exitStringExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringExpr" ):
                return visitor.visitStringExpr(self)
            else:
                return visitor.visitChildren(self)


    class AddExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ExprContext,i)

        def PLUS(self):
            return self.getToken(IfElseLangParser.PLUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddExpr" ):
                listener.enterAddExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddExpr" ):
                listener.exitAddExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddExpr" ):
                return visitor.visitAddExpr(self)
            else:
                return visitor.visitChildren(self)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(IfElseLangParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class MulExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ExprContext,i)

        def MULT(self):
            return self.getToken(IfElseLangParser.MULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulExpr" ):
                listener.enterMulExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulExpr" ):
                listener.exitMulExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulExpr" ):
                return visitor.visitMulExpr(self)
            else:
                return visitor.visitChildren(self)


    class DivExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ExprContext,i)

        def DIV(self):
            return self.getToken(IfElseLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDivExpr" ):
                listener.enterDivExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDivExpr" ):
                listener.exitDivExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivExpr" ):
                return visitor.visitDivExpr(self)
            else:
                return visitor.visitChildren(self)


    class FuncCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)
        def LPAREN(self):
            return self.getToken(IfElseLangParser.LPAREN, 0)
        def RPAREN(self):
            return self.getToken(IfElseLangParser.RPAREN, 0)
        def argList(self):
            return self.getTypedRuleContext(IfElseLangParser.ArgListContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncCallExpr" ):
                listener.enterFuncCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncCallExpr" ):
                listener.exitFuncCallExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCallExpr" ):
                return visitor.visitFuncCallExpr(self)
            else:
                return visitor.visitChildren(self)


    class SubExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ExprContext,i)

        def MINUS(self):
            return self.getToken(IfElseLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubExpr" ):
                listener.enterSubExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubExpr" ):
                listener.exitSubExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSubExpr" ):
                return visitor.visitSubExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(IfElseLangParser.LPAREN, 0)
        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)

        def RPAREN(self):
            return self.getToken(IfElseLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class IdExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdExpr" ):
                listener.enterIdExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdExpr" ):
                listener.exitIdExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdExpr" ):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IfElseLangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = IfElseLangParser.FuncCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 107
                self.match(IfElseLangParser.ID)
                self.state = 108
                self.match(IfElseLangParser.LPAREN)
                self.state = 110
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 117441024) != 0):
                    self.state = 109
                    self.argList()


                self.state = 112
                self.match(IfElseLangParser.RPAREN)
                pass

            elif la_ == 2:
                localctx = IfElseLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 113
                self.match(IfElseLangParser.ID)
                pass

            elif la_ == 3:
                localctx = IfElseLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 114
                self.match(IfElseLangParser.NUMBER)
                pass

            elif la_ == 4:
                localctx = IfElseLangParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 115
                self.match(IfElseLangParser.STRING)
                pass

            elif la_ == 5:
                localctx = IfElseLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 116
                self.match(IfElseLangParser.LPAREN)
                self.state = 117
                self.expr(0)
                self.state = 118
                self.match(IfElseLangParser.RPAREN)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 134
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = IfElseLangParser.AddExprContext(self, IfElseLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 122
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 123
                        self.match(IfElseLangParser.PLUS)
                        self.state = 124
                        self.expr(10)
                        pass

                    elif la_ == 2:
                        localctx = IfElseLangParser.SubExprContext(self, IfElseLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 125
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 126
                        self.match(IfElseLangParser.MINUS)
                        self.state = 127
                        self.expr(9)
                        pass

                    elif la_ == 3:
                        localctx = IfElseLangParser.MulExprContext(self, IfElseLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 128
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 129
                        self.match(IfElseLangParser.MULT)
                        self.state = 130
                        self.expr(8)
                        pass

                    elif la_ == 4:
                        localctx = IfElseLangParser.DivExprContext(self, IfElseLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 131
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 132
                        self.match(IfElseLangParser.DIV)
                        self.state = 133
                        self.expr(7)
                        pass

             
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArgListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ExprContext,i)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_argList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgList" ):
                listener.enterArgList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgList" ):
                listener.exitArgList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgList" ):
                return visitor.visitArgList(self)
            else:
                return visitor.visitChildren(self)




    def argList(self):

        localctx = IfElseLangParser.ArgListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_argList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.expr(0)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 140
                self.match(IfElseLangParser.T__1)
                self.state = 141
                self.expr(0)
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LT(self):
            return self.getToken(IfElseLangParser.LT, 0)

        def GT(self):
            return self.getToken(IfElseLangParser.GT, 0)

        def GE(self):
            return self.getToken(IfElseLangParser.GE, 0)

        def LE(self):
            return self.getToken(IfElseLangParser.LE, 0)

        def NE(self):
            return self.getToken(IfElseLangParser.NE, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = IfElseLangParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IfElseLangParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType" ):
                return visitor.visitType(self)
            else:
                return visitor.visitChildren(self)




    def type_(self):

        localctx = IfElseLangParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 6)
         




