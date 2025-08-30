# Generated from ControlLang.g4 by ANTLR 4.13.2
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
        4,1,24,126,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,39,8,2,5,2,41,8,
        2,10,2,12,2,44,9,2,1,2,1,2,1,2,1,2,1,2,3,2,51,8,2,5,2,53,8,2,10,
        2,12,2,56,9,2,1,2,3,2,59,8,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,4,3,72,8,3,11,3,12,3,73,1,3,1,3,1,3,1,3,1,3,3,3,81,8,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,113,8,
        7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,121,8,7,10,7,12,7,124,9,7,1,7,1,73,
        1,14,8,0,2,4,6,8,10,12,14,0,3,1,0,17,20,1,0,15,16,1,0,13,14,132,
        0,19,1,0,0,0,2,29,1,0,0,0,4,31,1,0,0,0,6,60,1,0,0,0,8,84,1,0,0,0,
        10,97,1,0,0,0,12,101,1,0,0,0,14,112,1,0,0,0,16,17,3,2,1,0,17,18,
        5,21,0,0,18,20,1,0,0,0,19,16,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,
        21,22,1,0,0,0,22,23,1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,30,3,4,
        2,0,26,30,3,6,3,0,27,30,3,8,4,0,28,30,3,12,6,0,29,25,1,0,0,0,29,
        26,1,0,0,0,29,27,1,0,0,0,29,28,1,0,0,0,30,3,1,0,0,0,31,32,5,1,0,
        0,32,33,5,8,0,0,33,34,3,10,5,0,34,35,5,9,0,0,35,42,5,10,0,0,36,38,
        3,2,1,0,37,39,5,21,0,0,38,37,1,0,0,0,38,39,1,0,0,0,39,41,1,0,0,0,
        40,36,1,0,0,0,41,44,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,45,1,
        0,0,0,44,42,1,0,0,0,45,58,5,11,0,0,46,47,5,2,0,0,47,54,5,10,0,0,
        48,50,3,2,1,0,49,51,5,21,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,53,1,
        0,0,0,52,48,1,0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,
        57,1,0,0,0,56,54,1,0,0,0,57,59,5,11,0,0,58,46,1,0,0,0,58,59,1,0,
        0,0,59,5,1,0,0,0,60,61,5,4,0,0,61,62,5,8,0,0,62,63,5,22,0,0,63,64,
        5,9,0,0,64,71,5,10,0,0,65,66,5,5,0,0,66,67,5,23,0,0,67,68,5,6,0,
        0,68,69,3,2,1,0,69,70,5,21,0,0,70,72,1,0,0,0,71,65,1,0,0,0,72,73,
        1,0,0,0,73,74,1,0,0,0,73,71,1,0,0,0,74,80,1,0,0,0,75,76,5,7,0,0,
        76,77,5,6,0,0,77,78,3,2,1,0,78,79,5,21,0,0,79,81,1,0,0,0,80,75,1,
        0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,83,5,11,0,0,83,7,1,0,0,0,84,
        85,5,3,0,0,85,86,5,8,0,0,86,87,3,12,6,0,87,88,5,21,0,0,88,89,3,10,
        5,0,89,90,5,21,0,0,90,91,3,12,6,0,91,92,5,9,0,0,92,93,5,10,0,0,93,
        94,3,2,1,0,94,95,5,21,0,0,95,96,5,11,0,0,96,9,1,0,0,0,97,98,5,22,
        0,0,98,99,7,0,0,0,99,100,5,23,0,0,100,11,1,0,0,0,101,102,5,22,0,
        0,102,103,5,12,0,0,103,104,3,14,7,0,104,13,1,0,0,0,105,106,6,7,-1,
        0,106,113,5,23,0,0,107,113,5,22,0,0,108,109,5,8,0,0,109,110,3,14,
        7,0,110,111,5,9,0,0,111,113,1,0,0,0,112,105,1,0,0,0,112,107,1,0,
        0,0,112,108,1,0,0,0,113,122,1,0,0,0,114,115,10,5,0,0,115,116,7,1,
        0,0,116,121,3,14,7,6,117,118,10,4,0,0,118,119,7,2,0,0,119,121,3,
        14,7,5,120,114,1,0,0,0,120,117,1,0,0,0,121,124,1,0,0,0,122,120,1,
        0,0,0,122,123,1,0,0,0,123,15,1,0,0,0,124,122,1,0,0,0,12,21,29,38,
        42,50,54,58,73,80,112,120,122
    ]

class ControlLangParser ( Parser ):

    grammarFileName = "ControlLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'else'", "'for'", "'switch'", 
                     "'case'", "':'", "'default'", "'('", "')'", "'{'", 
                     "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", 
                     "'=='", "'!='", "';'" ]

    symbolicNames = [ "<INVALID>", "IF", "ELSE", "FOR", "SWITCH", "CASE", 
                      "COLON", "DEFAULT", "LPAREN", "RPAREN", "LBRACE", 
                      "RBRACE", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
                      "GT", "LT", "EQ", "NEQ", "SEMI", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_ifElseStmt = 2
    RULE_switchStmt = 3
    RULE_forStmt = 4
    RULE_condicion = 5
    RULE_asignacion = 6
    RULE_expresion = 7

    ruleNames =  [ "programa", "sentencia", "ifElseStmt", "switchStmt", 
                   "forStmt", "condicion", "asignacion", "expresion" ]

    EOF = Token.EOF
    IF=1
    ELSE=2
    FOR=3
    SWITCH=4
    CASE=5
    COLON=6
    DEFAULT=7
    LPAREN=8
    RPAREN=9
    LBRACE=10
    RBRACE=11
    ASSIGN=12
    PLUS=13
    MINUS=14
    MUL=15
    DIV=16
    GT=17
    LT=18
    EQ=19
    NEQ=20
    SEMI=21
    ID=22
    INT=23
    WS=24

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ControlLangParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ControlLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ControlLangParser.SentenciaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ControlLangParser.SEMI)
            else:
                return self.getToken(ControlLangParser.SEMI, i)

        def getRuleIndex(self):
            return ControlLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = ControlLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.sentencia()
                self.state = 17
                self.match(ControlLangParser.SEMI)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194330) != 0)):
                    break

            self.state = 23
            self.match(ControlLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifElseStmt(self):
            return self.getTypedRuleContext(ControlLangParser.IfElseStmtContext,0)


        def switchStmt(self):
            return self.getTypedRuleContext(ControlLangParser.SwitchStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(ControlLangParser.ForStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(ControlLangParser.AsignacionContext,0)


        def getRuleIndex(self):
            return ControlLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = ControlLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.ifElseStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.switchStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.forStmt()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 28
                self.asignacion()
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


    class IfElseStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ControlLangParser.RULE_ifElseStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfElseContext(IfElseStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.IfElseStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IF(self):
            return self.getToken(ControlLangParser.IF, 0)
        def LPAREN(self):
            return self.getToken(ControlLangParser.LPAREN, 0)
        def condicion(self):
            return self.getTypedRuleContext(ControlLangParser.CondicionContext,0)

        def RPAREN(self):
            return self.getToken(ControlLangParser.RPAREN, 0)
        def LBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ControlLangParser.LBRACE)
            else:
                return self.getToken(ControlLangParser.LBRACE, i)
        def RBRACE(self, i:int=None):
            if i is None:
                return self.getTokens(ControlLangParser.RBRACE)
            else:
                return self.getToken(ControlLangParser.RBRACE, i)
        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ControlLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ControlLangParser.SentenciaContext,i)

        def ELSE(self):
            return self.getToken(ControlLangParser.ELSE, 0)
        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ControlLangParser.SEMI)
            else:
                return self.getToken(ControlLangParser.SEMI, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)



    def ifElseStmt(self):

        localctx = ControlLangParser.IfElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_ifElseStmt)
        self._la = 0 # Token type
        try:
            localctx = ControlLangParser.IfElseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ControlLangParser.IF)
            self.state = 32
            self.match(ControlLangParser.LPAREN)
            self.state = 33
            self.condicion()
            self.state = 34
            self.match(ControlLangParser.RPAREN)
            self.state = 35
            self.match(ControlLangParser.LBRACE)
            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4194330) != 0):
                self.state = 36
                self.sentencia()
                self.state = 38
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==21:
                    self.state = 37
                    self.match(ControlLangParser.SEMI)


                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(ControlLangParser.RBRACE)
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 46
                self.match(ControlLangParser.ELSE)
                self.state = 47
                self.match(ControlLangParser.LBRACE)
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4194330) != 0):
                    self.state = 48
                    self.sentencia()
                    self.state = 50
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==21:
                        self.state = 49
                        self.match(ControlLangParser.SEMI)


                    self.state = 56
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 57
                self.match(ControlLangParser.RBRACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ControlLangParser.RULE_switchStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ForContext(SwitchStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.SwitchStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SWITCH(self):
            return self.getToken(ControlLangParser.SWITCH, 0)
        def LPAREN(self):
            return self.getToken(ControlLangParser.LPAREN, 0)
        def ID(self):
            return self.getToken(ControlLangParser.ID, 0)
        def RPAREN(self):
            return self.getToken(ControlLangParser.RPAREN, 0)
        def LBRACE(self):
            return self.getToken(ControlLangParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(ControlLangParser.RBRACE, 0)
        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(ControlLangParser.CASE)
            else:
                return self.getToken(ControlLangParser.CASE, i)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(ControlLangParser.INT)
            else:
                return self.getToken(ControlLangParser.INT, i)
        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(ControlLangParser.COLON)
            else:
                return self.getToken(ControlLangParser.COLON, i)
        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ControlLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ControlLangParser.SentenciaContext,i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ControlLangParser.SEMI)
            else:
                return self.getToken(ControlLangParser.SEMI, i)
        def DEFAULT(self):
            return self.getToken(ControlLangParser.DEFAULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFor" ):
                listener.enterFor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFor" ):
                listener.exitFor(self)



    def switchStmt(self):

        localctx = ControlLangParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            localctx = ControlLangParser.ForContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(ControlLangParser.SWITCH)
            self.state = 61
            self.match(ControlLangParser.LPAREN)
            self.state = 62
            self.match(ControlLangParser.ID)
            self.state = 63
            self.match(ControlLangParser.RPAREN)
            self.state = 64
            self.match(ControlLangParser.LBRACE)
            self.state = 71 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 65
                    self.match(ControlLangParser.CASE)
                    self.state = 66
                    self.match(ControlLangParser.INT)
                    self.state = 67
                    self.match(ControlLangParser.COLON)
                    self.state = 68
                    self.sentencia()
                    self.state = 69
                    self.match(ControlLangParser.SEMI)

                else:
                    raise NoViableAltException(self)
                self.state = 73 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 75
                self.match(ControlLangParser.DEFAULT)
                self.state = 76
                self.match(ControlLangParser.COLON)
                self.state = 77
                self.sentencia()
                self.state = 78
                self.match(ControlLangParser.SEMI)


            self.state = 82
            self.match(ControlLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ControlLangParser.RULE_forStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SwitchContext(ForStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.ForStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(ControlLangParser.FOR, 0)
        def LPAREN(self):
            return self.getToken(ControlLangParser.LPAREN, 0)
        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ControlLangParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(ControlLangParser.AsignacionContext,i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ControlLangParser.SEMI)
            else:
                return self.getToken(ControlLangParser.SEMI, i)
        def condicion(self):
            return self.getTypedRuleContext(ControlLangParser.CondicionContext,0)

        def RPAREN(self):
            return self.getToken(ControlLangParser.RPAREN, 0)
        def LBRACE(self):
            return self.getToken(ControlLangParser.LBRACE, 0)
        def sentencia(self):
            return self.getTypedRuleContext(ControlLangParser.SentenciaContext,0)

        def RBRACE(self):
            return self.getToken(ControlLangParser.RBRACE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSwitch" ):
                listener.enterSwitch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSwitch" ):
                listener.exitSwitch(self)



    def forStmt(self):

        localctx = ControlLangParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_forStmt)
        try:
            localctx = ControlLangParser.SwitchContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(ControlLangParser.FOR)
            self.state = 85
            self.match(ControlLangParser.LPAREN)
            self.state = 86
            self.asignacion()
            self.state = 87
            self.match(ControlLangParser.SEMI)
            self.state = 88
            self.condicion()
            self.state = 89
            self.match(ControlLangParser.SEMI)
            self.state = 90
            self.asignacion()
            self.state = 91
            self.match(ControlLangParser.RPAREN)
            self.state = 92
            self.match(ControlLangParser.LBRACE)
            self.state = 93
            self.sentencia()
            self.state = 94
            self.match(ControlLangParser.SEMI)
            self.state = 95
            self.match(ControlLangParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ControlLangParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondicionSimpleContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.CondicionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ControlLangParser.ID, 0)
        def INT(self):
            return self.getToken(ControlLangParser.INT, 0)
        def GT(self):
            return self.getToken(ControlLangParser.GT, 0)
        def LT(self):
            return self.getToken(ControlLangParser.LT, 0)
        def EQ(self):
            return self.getToken(ControlLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(ControlLangParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicionSimple" ):
                listener.enterCondicionSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicionSimple" ):
                listener.exitCondicionSimple(self)



    def condicion(self):

        localctx = ControlLangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            localctx = ControlLangParser.CondicionSimpleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ControlLangParser.ID)
            self.state = 98
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1966080) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 99
            self.match(ControlLangParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ControlLangParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ControlLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(ControlLangParser.ASSIGN, 0)
        def expresion(self):
            return self.getTypedRuleContext(ControlLangParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def asignacion(self):

        localctx = ControlLangParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            localctx = ControlLangParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(ControlLangParser.ID)
            self.state = 102
            self.match(ControlLangParser.ASSIGN)
            self.state = 103
            self.expresion(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ControlLangParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ControlLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class MulDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ControlLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(ControlLangParser.ExpresionContext,i)

        def MUL(self):
            return self.getToken(ControlLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(ControlLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ControlLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(ControlLangParser.ExpresionContext,i)

        def PLUS(self):
            return self.getToken(ControlLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ControlLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ControlLangParser.LPAREN, 0)
        def expresion(self):
            return self.getTypedRuleContext(ControlLangParser.ExpresionContext,0)

        def RPAREN(self):
            return self.getToken(ControlLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ControlLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ControlLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ControlLangParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                localctx = ControlLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 106
                self.match(ControlLangParser.INT)
                pass
            elif token in [22]:
                localctx = ControlLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.match(ControlLangParser.ID)
                pass
            elif token in [8]:
                localctx = ControlLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(ControlLangParser.LPAREN)
                self.state = 109
                self.expresion(0)
                self.state = 110
                self.match(ControlLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 122
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 120
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = ControlLangParser.MulDivContext(self, ControlLangParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 114
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 115
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==15 or _la==16):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 116
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = ControlLangParser.AddSubContext(self, ControlLangParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 117
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 118
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==13 or _la==14):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 119
                        self.expresion(5)
                        pass

             
                self.state = 124
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self._predicates[7] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




