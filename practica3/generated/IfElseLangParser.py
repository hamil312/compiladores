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
        4,1,31,175,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        1,0,4,0,30,8,0,11,0,12,0,31,1,0,1,0,1,1,1,1,1,1,1,1,3,1,40,8,1,1,
        1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,3,3,51,8,3,1,4,1,4,1,4,1,4,1,4,
        3,4,58,8,4,1,4,1,4,1,4,3,4,63,8,4,1,4,1,4,1,4,5,4,68,8,4,10,4,12,
        4,71,9,4,1,4,1,4,1,5,1,5,1,5,1,5,3,5,79,8,5,1,6,1,6,1,6,1,6,1,7,
        1,7,1,7,1,7,1,7,1,7,4,7,91,8,7,11,7,12,7,92,1,7,3,7,96,8,7,1,7,1,
        7,1,8,1,8,1,8,1,8,5,8,104,8,8,10,8,12,8,107,9,8,1,8,1,8,1,8,1,9,
        1,9,1,9,5,9,115,8,9,10,9,12,9,118,9,9,1,9,1,9,3,9,122,8,9,1,10,1,
        10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,135,8,11,10,
        11,12,11,138,9,11,1,11,1,11,1,11,1,11,5,11,144,8,11,10,11,12,11,
        147,9,11,1,11,3,11,150,8,11,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,3,13,162,8,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,170,
        8,13,10,13,12,13,173,9,13,1,13,0,1,26,14,0,2,4,6,8,10,12,14,16,18,
        20,22,24,26,0,3,1,0,1,2,1,0,11,16,1,0,17,20,184,0,29,1,0,0,0,2,35,
        1,0,0,0,4,43,1,0,0,0,6,50,1,0,0,0,8,52,1,0,0,0,10,74,1,0,0,0,12,
        80,1,0,0,0,14,84,1,0,0,0,16,99,1,0,0,0,18,111,1,0,0,0,20,123,1,0,
        0,0,22,128,1,0,0,0,24,151,1,0,0,0,26,161,1,0,0,0,28,30,3,6,3,0,29,
        28,1,0,0,0,30,31,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,32,33,1,0,0,
        0,33,34,5,0,0,1,34,1,1,0,0,0,35,36,3,4,2,0,36,39,5,27,0,0,37,38,
        5,10,0,0,38,40,3,26,13,0,39,37,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,
        0,41,42,5,9,0,0,42,3,1,0,0,0,43,44,7,0,0,0,44,5,1,0,0,0,45,51,3,
        20,10,0,46,51,3,22,11,0,47,51,3,2,1,0,48,51,3,8,4,0,49,51,3,14,7,
        0,50,45,1,0,0,0,50,46,1,0,0,0,50,47,1,0,0,0,50,48,1,0,0,0,50,49,
        1,0,0,0,51,7,1,0,0,0,52,53,5,21,0,0,53,57,5,5,0,0,54,58,3,10,5,0,
        55,58,3,12,6,0,56,58,5,9,0,0,57,54,1,0,0,0,57,55,1,0,0,0,57,56,1,
        0,0,0,58,59,1,0,0,0,59,60,3,24,12,0,60,62,5,9,0,0,61,63,3,12,6,0,
        62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,64,65,5,6,0,0,65,69,5,
        7,0,0,66,68,3,6,3,0,67,66,1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,
        70,1,0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,5,8,0,0,73,9,1,0,0,
        0,74,75,3,4,2,0,75,78,5,27,0,0,76,77,5,10,0,0,77,79,3,26,13,0,78,
        76,1,0,0,0,78,79,1,0,0,0,79,11,1,0,0,0,80,81,5,27,0,0,81,82,5,10,
        0,0,82,83,3,26,13,0,83,13,1,0,0,0,84,85,5,22,0,0,85,86,5,5,0,0,86,
        87,3,26,13,0,87,88,5,6,0,0,88,90,5,7,0,0,89,91,3,16,8,0,90,89,1,
        0,0,0,91,92,1,0,0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,95,1,0,0,0,94,
        96,3,18,9,0,95,94,1,0,0,0,95,96,1,0,0,0,96,97,1,0,0,0,97,98,5,8,
        0,0,98,15,1,0,0,0,99,100,5,23,0,0,100,101,3,26,13,0,101,105,5,25,
        0,0,102,104,3,6,3,0,103,102,1,0,0,0,104,107,1,0,0,0,105,103,1,0,
        0,0,105,106,1,0,0,0,106,108,1,0,0,0,107,105,1,0,0,0,108,109,5,26,
        0,0,109,110,5,9,0,0,110,17,1,0,0,0,111,112,5,24,0,0,112,116,5,25,
        0,0,113,115,3,6,3,0,114,113,1,0,0,0,115,118,1,0,0,0,116,114,1,0,
        0,0,116,117,1,0,0,0,117,121,1,0,0,0,118,116,1,0,0,0,119,120,5,26,
        0,0,120,122,5,9,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,19,1,0,0,
        0,123,124,5,27,0,0,124,125,5,10,0,0,125,126,3,26,13,0,126,127,5,
        9,0,0,127,21,1,0,0,0,128,129,5,3,0,0,129,130,5,5,0,0,130,131,3,24,
        12,0,131,132,5,6,0,0,132,136,5,7,0,0,133,135,3,6,3,0,134,133,1,0,
        0,0,135,138,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,139,1,0,
        0,0,138,136,1,0,0,0,139,149,5,8,0,0,140,141,5,4,0,0,141,145,5,7,
        0,0,142,144,3,6,3,0,143,142,1,0,0,0,144,147,1,0,0,0,145,143,1,0,
        0,0,145,146,1,0,0,0,146,148,1,0,0,0,147,145,1,0,0,0,148,150,5,8,
        0,0,149,140,1,0,0,0,149,150,1,0,0,0,150,23,1,0,0,0,151,152,3,26,
        13,0,152,25,1,0,0,0,153,154,6,13,-1,0,154,162,5,27,0,0,155,162,5,
        28,0,0,156,162,5,29,0,0,157,158,5,5,0,0,158,159,3,26,13,0,159,160,
        5,6,0,0,160,162,1,0,0,0,161,153,1,0,0,0,161,155,1,0,0,0,161,156,
        1,0,0,0,161,157,1,0,0,0,162,171,1,0,0,0,163,164,10,3,0,0,164,165,
        7,1,0,0,165,170,3,26,13,4,166,167,10,2,0,0,167,168,7,2,0,0,168,170,
        3,26,13,3,169,163,1,0,0,0,169,166,1,0,0,0,170,173,1,0,0,0,171,169,
        1,0,0,0,171,172,1,0,0,0,172,27,1,0,0,0,173,171,1,0,0,0,18,31,39,
        50,57,62,69,78,92,95,105,116,121,136,145,149,161,169,171
    ]

class IfElseLangParser ( Parser ):

    grammarFileName = "IfElseLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'string'", "'if'", "'else'", 
                     "'('", "')'", "'{'", "'}'", "';'", "'='", "'<'", "'>'", 
                     "'>='", "'<='", "'=='", "'!='", "'+'", "'-'", "'*'", 
                     "'/'", "'for'", "'switch'", "'case'", "'default'", 
                     "':'", "'break'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "IF", "ELSE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "ASSIGN", 
                      "LT", "GT", "GE", "LE", "EQ", "NE", "PLUS", "MINUS", 
                      "MUL", "DIV", "FOR", "SWITCH", "CASE", "DEFAULT", 
                      "COLON", "BREAK", "ID", "NUMBER", "STRING", "COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_type = 2
    RULE_statement = 3
    RULE_forStatement = 4
    RULE_declarationNoSemi = 5
    RULE_assignmentNoSemi = 6
    RULE_switchStatement = 7
    RULE_caseStatement = 8
    RULE_defaultStatement = 9
    RULE_assignment = 10
    RULE_ifStatement = 11
    RULE_condition = 12
    RULE_expr = 13

    ruleNames =  [ "program", "declaration", "type", "statement", "forStatement", 
                   "declarationNoSemi", "assignmentNoSemi", "switchStatement", 
                   "caseStatement", "defaultStatement", "assignment", "ifStatement", 
                   "condition", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    IF=3
    ELSE=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    SEMI=9
    ASSIGN=10
    LT=11
    GT=12
    GE=13
    LE=14
    EQ=15
    NE=16
    PLUS=17
    MINUS=18
    MUL=19
    DIV=20
    FOR=21
    SWITCH=22
    CASE=23
    DEFAULT=24
    COLON=25
    BREAK=26
    ID=27
    NUMBER=28
    STRING=29
    COMMENT=30
    WS=31

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
            self.state = 29 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 28
                self.statement()
                self.state = 31 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 140509198) != 0)):
                    break

            self.state = 33
            self.match(IfElseLangParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.type_()
            self.state = 36
            self.match(IfElseLangParser.ID)
            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 37
                self.match(IfElseLangParser.ASSIGN)
                self.state = 38
                self.expr(0)


            self.state = 41
            self.match(IfElseLangParser.SEMI)
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
        self.enterRule(localctx, 4, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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


        def forStatement(self):
            return self.getTypedRuleContext(IfElseLangParser.ForStatementContext,0)


        def switchStatement(self):
            return self.getTypedRuleContext(IfElseLangParser.SwitchStatementContext,0)


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
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                self.enterOuterAlt(localctx, 1)
                self.state = 45
                self.assignment()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 46
                self.ifStatement()
                pass
            elif token in [1, 2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 47
                self.declaration()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 4)
                self.state = 48
                self.forStatement()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 5)
                self.state = 49
                self.switchStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(IfElseLangParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(IfElseLangParser.LPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(IfElseLangParser.ConditionContext,0)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(IfElseLangParser.SEMI)
            else:
                return self.getToken(IfElseLangParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(IfElseLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(IfElseLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(IfElseLangParser.RBRACE, 0)

        def declarationNoSemi(self):
            return self.getTypedRuleContext(IfElseLangParser.DeclarationNoSemiContext,0)


        def assignmentNoSemi(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.AssignmentNoSemiContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.AssignmentNoSemiContext,i)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = IfElseLangParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_forStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(IfElseLangParser.FOR)
            self.state = 53
            self.match(IfElseLangParser.LPAREN)
            self.state = 57
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.state = 54
                self.declarationNoSemi()
                pass
            elif token in [27]:
                self.state = 55
                self.assignmentNoSemi()
                pass
            elif token in [9]:
                self.state = 56
                self.match(IfElseLangParser.SEMI)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 59
            self.condition()
            self.state = 60
            self.match(IfElseLangParser.SEMI)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 61
                self.assignmentNoSemi()


            self.state = 64
            self.match(IfElseLangParser.RPAREN)
            self.state = 65
            self.match(IfElseLangParser.LBRACE)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140509198) != 0):
                self.state = 66
                self.statement()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(IfElseLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationNoSemiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(IfElseLangParser.TypeContext,0)


        def ID(self):
            return self.getToken(IfElseLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(IfElseLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_declarationNoSemi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationNoSemi" ):
                listener.enterDeclarationNoSemi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationNoSemi" ):
                listener.exitDeclarationNoSemi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationNoSemi" ):
                return visitor.visitDeclarationNoSemi(self)
            else:
                return visitor.visitChildren(self)




    def declarationNoSemi(self):

        localctx = IfElseLangParser.DeclarationNoSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_declarationNoSemi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.type_()
            self.state = 75
            self.match(IfElseLangParser.ID)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 76
                self.match(IfElseLangParser.ASSIGN)
                self.state = 77
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentNoSemiContext(ParserRuleContext):
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


        def getRuleIndex(self):
            return IfElseLangParser.RULE_assignmentNoSemi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentNoSemi" ):
                listener.enterAssignmentNoSemi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentNoSemi" ):
                listener.exitAssignmentNoSemi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentNoSemi" ):
                return visitor.visitAssignmentNoSemi(self)
            else:
                return visitor.visitChildren(self)




    def assignmentNoSemi(self):

        localctx = IfElseLangParser.AssignmentNoSemiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assignmentNoSemi)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(IfElseLangParser.ID)
            self.state = 81
            self.match(IfElseLangParser.ASSIGN)
            self.state = 82
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(IfElseLangParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(IfElseLangParser.LPAREN, 0)

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def RPAREN(self):
            return self.getToken(IfElseLangParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(IfElseLangParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(IfElseLangParser.RBRACE, 0)

        def caseStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.CaseStatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.CaseStatementContext,i)


        def defaultStatement(self):
            return self.getTypedRuleContext(IfElseLangParser.DefaultStatementContext,0)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_switchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitchStatement" ):
                listener.enterSwitchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitchStatement" ):
                listener.exitSwitchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitchStatement" ):
                return visitor.visitSwitchStatement(self)
            else:
                return visitor.visitChildren(self)




    def switchStatement(self):

        localctx = IfElseLangParser.SwitchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_switchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(IfElseLangParser.SWITCH)
            self.state = 85
            self.match(IfElseLangParser.LPAREN)
            self.state = 86
            self.expr(0)
            self.state = 87
            self.match(IfElseLangParser.RPAREN)
            self.state = 88
            self.match(IfElseLangParser.LBRACE)
            self.state = 90 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 89
                self.caseStatement()
                self.state = 92 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==23):
                    break

            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==24:
                self.state = 94
                self.defaultStatement()


            self.state = 97
            self.match(IfElseLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(IfElseLangParser.CASE, 0)

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


        def COLON(self):
            return self.getToken(IfElseLangParser.COLON, 0)

        def BREAK(self):
            return self.getToken(IfElseLangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(IfElseLangParser.SEMI, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


        def getRuleIndex(self):
            return IfElseLangParser.RULE_caseStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseStatement" ):
                listener.enterCaseStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseStatement" ):
                listener.exitCaseStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseStatement" ):
                return visitor.visitCaseStatement(self)
            else:
                return visitor.visitChildren(self)




    def caseStatement(self):

        localctx = IfElseLangParser.CaseStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_caseStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(IfElseLangParser.CASE)
            self.state = 100
            self.expr(0)
            self.state = 101
            self.match(IfElseLangParser.COLON)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140509198) != 0):
                self.state = 102
                self.statement()
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 108
            self.match(IfElseLangParser.BREAK)
            self.state = 109
            self.match(IfElseLangParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DefaultStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(IfElseLangParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(IfElseLangParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


        def BREAK(self):
            return self.getToken(IfElseLangParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(IfElseLangParser.SEMI, 0)

        def getRuleIndex(self):
            return IfElseLangParser.RULE_defaultStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefaultStatement" ):
                listener.enterDefaultStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefaultStatement" ):
                listener.exitDefaultStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefaultStatement" ):
                return visitor.visitDefaultStatement(self)
            else:
                return visitor.visitChildren(self)




    def defaultStatement(self):

        localctx = IfElseLangParser.DefaultStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_defaultStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(IfElseLangParser.DEFAULT)
            self.state = 112
            self.match(IfElseLangParser.COLON)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140509198) != 0):
                self.state = 113
                self.statement()
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==26:
                self.state = 119
                self.match(IfElseLangParser.BREAK)
                self.state = 120
                self.match(IfElseLangParser.SEMI)


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
        self.enterRule(localctx, 20, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(IfElseLangParser.ID)
            self.state = 124
            self.match(IfElseLangParser.ASSIGN)
            self.state = 125
            self.expr(0)
            self.state = 126
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

        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(IfElseLangParser.LBRACE)
            else:
                return self.getToken(IfElseLangParser.LBRACE, i)

        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(IfElseLangParser.RBRACE)
            else:
                return self.getToken(IfElseLangParser.RBRACE, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.StatementContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.StatementContext,i)


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
        self.enterRule(localctx, 22, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(IfElseLangParser.IF)
            self.state = 129
            self.match(IfElseLangParser.LPAREN)
            self.state = 130
            self.condition()
            self.state = 131
            self.match(IfElseLangParser.RPAREN)
            self.state = 132
            self.match(IfElseLangParser.LBRACE)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140509198) != 0):
                self.state = 133
                self.statement()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 139
            self.match(IfElseLangParser.RBRACE)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 140
                self.match(IfElseLangParser.ELSE)
                self.state = 141
                self.match(IfElseLangParser.LBRACE)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140509198) != 0):
                    self.state = 142
                    self.statement()
                    self.state = 147
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 148
                self.match(IfElseLangParser.RBRACE)


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

        def expr(self):
            return self.getTypedRuleContext(IfElseLangParser.ExprContext,0)


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
        self.enterRule(localctx, 24, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
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


    class ComparisonExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a IfElseLangParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IfElseLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(IfElseLangParser.ExprContext,i)

        def LT(self):
            return self.getToken(IfElseLangParser.LT, 0)
        def GT(self):
            return self.getToken(IfElseLangParser.GT, 0)
        def GE(self):
            return self.getToken(IfElseLangParser.GE, 0)
        def LE(self):
            return self.getToken(IfElseLangParser.LE, 0)
        def EQ(self):
            return self.getToken(IfElseLangParser.EQ, 0)
        def NE(self):
            return self.getToken(IfElseLangParser.NE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonExpr" ):
                listener.enterComparisonExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonExpr" ):
                listener.exitComparisonExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonExpr" ):
                return visitor.visitComparisonExpr(self)
            else:
                return visitor.visitChildren(self)


    class ArithmeticExprContext(ExprContext):

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
        def MINUS(self):
            return self.getToken(IfElseLangParser.MINUS, 0)
        def MUL(self):
            return self.getToken(IfElseLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(IfElseLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpr" ):
                listener.enterArithmeticExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpr" ):
                listener.exitArithmeticExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmeticExpr" ):
                return visitor.visitArithmeticExpr(self)
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27]:
                localctx = IfElseLangParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 154
                self.match(IfElseLangParser.ID)
                pass
            elif token in [28]:
                localctx = IfElseLangParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.match(IfElseLangParser.NUMBER)
                pass
            elif token in [29]:
                localctx = IfElseLangParser.StringExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(IfElseLangParser.STRING)
                pass
            elif token in [5]:
                localctx = IfElseLangParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 157
                self.match(IfElseLangParser.LPAREN)
                self.state = 158
                self.expr(0)
                self.state = 159
                self.match(IfElseLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 169
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = IfElseLangParser.ComparisonExprContext(self, IfElseLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 163
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 164
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 129024) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 165
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = IfElseLangParser.ArithmeticExprContext(self, IfElseLangParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 166
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 167
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0)):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 168
                        self.expr(3)
                        pass

             
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[13] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




