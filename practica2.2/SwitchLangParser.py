# Generated from SwitchLang.g4 by ANTLR 4.13.2
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
        4,1,21,78,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,4,2,37,8,2,11,2,12,2,38,1,2,
        1,2,1,2,1,2,1,2,3,2,46,8,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,65,8,5,1,5,1,5,1,5,1,5,1,5,1,5,
        5,5,73,8,5,10,5,12,5,76,9,5,1,5,1,38,1,10,6,0,2,4,6,8,10,0,3,1,0,
        14,17,1,0,12,13,1,0,10,11,79,0,15,1,0,0,0,2,23,1,0,0,0,4,25,1,0,
        0,0,6,49,1,0,0,0,8,53,1,0,0,0,10,64,1,0,0,0,12,13,3,2,1,0,13,14,
        5,18,0,0,14,16,1,0,0,0,15,12,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,
        17,18,1,0,0,0,18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,24,3,4,
        2,0,22,24,3,8,4,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,
        5,1,0,0,26,27,5,5,0,0,27,28,5,19,0,0,28,29,5,6,0,0,29,36,5,7,0,0,
        30,31,5,2,0,0,31,32,5,20,0,0,32,33,5,3,0,0,33,34,3,8,4,0,34,35,5,
        18,0,0,35,37,1,0,0,0,36,30,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,38,
        36,1,0,0,0,39,45,1,0,0,0,40,41,5,4,0,0,41,42,5,3,0,0,42,43,3,8,4,
        0,43,44,5,18,0,0,44,46,1,0,0,0,45,40,1,0,0,0,45,46,1,0,0,0,46,47,
        1,0,0,0,47,48,5,8,0,0,48,5,1,0,0,0,49,50,5,19,0,0,50,51,7,0,0,0,
        51,52,5,20,0,0,52,7,1,0,0,0,53,54,5,19,0,0,54,55,5,9,0,0,55,56,3,
        10,5,0,56,9,1,0,0,0,57,58,6,5,-1,0,58,65,5,20,0,0,59,65,5,19,0,0,
        60,61,5,5,0,0,61,62,3,10,5,0,62,63,5,6,0,0,63,65,1,0,0,0,64,57,1,
        0,0,0,64,59,1,0,0,0,64,60,1,0,0,0,65,74,1,0,0,0,66,67,10,5,0,0,67,
        68,7,1,0,0,68,73,3,10,5,6,69,70,10,4,0,0,70,71,7,2,0,0,71,73,3,10,
        5,5,72,66,1,0,0,0,72,69,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,
        1,0,0,0,75,11,1,0,0,0,76,74,1,0,0,0,7,17,23,38,45,64,72,74
    ]

class SwitchLangParser ( Parser ):

    grammarFileName = "SwitchLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'switch'", "'case'", "':'", "'default'", 
                     "'('", "')'", "'{'", "'}'", "'='", "'+'", "'-'", "'*'", 
                     "'/'", "'>'", "'<'", "'=='", "'!='", "';'" ]

    symbolicNames = [ "<INVALID>", "SWITCH", "CASE", "COLON", "DEFAULT", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "ASSIGN", 
                      "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "EQ", "NEQ", 
                      "SEMI", "ID", "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_switchStmt = 2
    RULE_condicion = 3
    RULE_asignacion = 4
    RULE_expresion = 5

    ruleNames =  [ "programa", "sentencia", "switchStmt", "condicion", "asignacion", 
                   "expresion" ]

    EOF = Token.EOF
    SWITCH=1
    CASE=2
    COLON=3
    DEFAULT=4
    LPAREN=5
    RPAREN=6
    LBRACE=7
    RBRACE=8
    ASSIGN=9
    PLUS=10
    MINUS=11
    MUL=12
    DIV=13
    GT=14
    LT=15
    EQ=16
    NEQ=17
    SEMI=18
    ID=19
    INT=20
    WS=21

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
            return self.getToken(SwitchLangParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.SentenciaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.SEMI)
            else:
                return self.getToken(SwitchLangParser.SEMI, i)

        def getRuleIndex(self):
            return SwitchLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = SwitchLangParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.sentencia()
                self.state = 13
                self.match(SwitchLangParser.SEMI)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==19):
                    break

            self.state = 19
            self.match(SwitchLangParser.EOF)
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

        def switchStmt(self):
            return self.getTypedRuleContext(SwitchLangParser.SwitchStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(SwitchLangParser.AsignacionContext,0)


        def getRuleIndex(self):
            return SwitchLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = SwitchLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.switchStmt()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
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


    class SwitchStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SwitchLangParser.RULE_switchStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfElseContext(SwitchStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.SwitchStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SWITCH(self):
            return self.getToken(SwitchLangParser.SWITCH, 0)
        def LPAREN(self):
            return self.getToken(SwitchLangParser.LPAREN, 0)
        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)
        def RPAREN(self):
            return self.getToken(SwitchLangParser.RPAREN, 0)
        def LBRACE(self):
            return self.getToken(SwitchLangParser.LBRACE, 0)
        def RBRACE(self):
            return self.getToken(SwitchLangParser.RBRACE, 0)
        def CASE(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.CASE)
            else:
                return self.getToken(SwitchLangParser.CASE, i)
        def INT(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.INT)
            else:
                return self.getToken(SwitchLangParser.INT, i)
        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.COLON)
            else:
                return self.getToken(SwitchLangParser.COLON, i)
        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.AsignacionContext,i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(SwitchLangParser.SEMI)
            else:
                return self.getToken(SwitchLangParser.SEMI, i)
        def DEFAULT(self):
            return self.getToken(SwitchLangParser.DEFAULT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)



    def switchStmt(self):

        localctx = SwitchLangParser.SwitchStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_switchStmt)
        self._la = 0 # Token type
        try:
            localctx = SwitchLangParser.IfElseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(SwitchLangParser.SWITCH)
            self.state = 26
            self.match(SwitchLangParser.LPAREN)
            self.state = 27
            self.match(SwitchLangParser.ID)
            self.state = 28
            self.match(SwitchLangParser.RPAREN)
            self.state = 29
            self.match(SwitchLangParser.LBRACE)
            self.state = 36 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 30
                    self.match(SwitchLangParser.CASE)
                    self.state = 31
                    self.match(SwitchLangParser.INT)
                    self.state = 32
                    self.match(SwitchLangParser.COLON)
                    self.state = 33
                    self.asignacion()
                    self.state = 34
                    self.match(SwitchLangParser.SEMI)

                else:
                    raise NoViableAltException(self)
                self.state = 38 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 40
                self.match(SwitchLangParser.DEFAULT)
                self.state = 41
                self.match(SwitchLangParser.COLON)
                self.state = 42
                self.asignacion()
                self.state = 43
                self.match(SwitchLangParser.SEMI)


            self.state = 47
            self.match(SwitchLangParser.RBRACE)
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
            return SwitchLangParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondicionSimpleContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.CondicionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)
        def INT(self):
            return self.getToken(SwitchLangParser.INT, 0)
        def GT(self):
            return self.getToken(SwitchLangParser.GT, 0)
        def LT(self):
            return self.getToken(SwitchLangParser.LT, 0)
        def EQ(self):
            return self.getToken(SwitchLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(SwitchLangParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicionSimple" ):
                listener.enterCondicionSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicionSimple" ):
                listener.exitCondicionSimple(self)



    def condicion(self):

        localctx = SwitchLangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            localctx = SwitchLangParser.CondicionSimpleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(SwitchLangParser.ID)
            self.state = 50
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 51
            self.match(SwitchLangParser.INT)
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
            return SwitchLangParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(SwitchLangParser.ASSIGN, 0)
        def expresion(self):
            return self.getTypedRuleContext(SwitchLangParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def asignacion(self):

        localctx = SwitchLangParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            localctx = SwitchLangParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(SwitchLangParser.ID)
            self.state = 54
            self.match(SwitchLangParser.ASSIGN)
            self.state = 55
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
            return SwitchLangParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(SwitchLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class MulDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.ExpresionContext,i)

        def MUL(self):
            return self.getToken(SwitchLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(SwitchLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SwitchLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(SwitchLangParser.ExpresionContext,i)

        def PLUS(self):
            return self.getToken(SwitchLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(SwitchLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(SwitchLangParser.LPAREN, 0)
        def expresion(self):
            return self.getTypedRuleContext(SwitchLangParser.ExpresionContext,0)

        def RPAREN(self):
            return self.getToken(SwitchLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SwitchLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(SwitchLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SwitchLangParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20]:
                localctx = SwitchLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 58
                self.match(SwitchLangParser.INT)
                pass
            elif token in [19]:
                localctx = SwitchLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 59
                self.match(SwitchLangParser.ID)
                pass
            elif token in [5]:
                localctx = SwitchLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 60
                self.match(SwitchLangParser.LPAREN)
                self.state = 61
                self.expresion(0)
                self.state = 62
                self.match(SwitchLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 72
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = SwitchLangParser.MulDivContext(self, SwitchLangParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 66
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 67
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==12 or _la==13):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 68
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = SwitchLangParser.AddSubContext(self, SwitchLangParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 69
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 70
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==10 or _la==11):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 71
                        self.expresion(5)
                        pass

             
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        self._predicates[5] = self.expresion_sempred
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
         




