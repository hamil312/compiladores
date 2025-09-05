# Generated from ForLang.g4 by ANTLR 4.13.2
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
        4,1,20,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,3,1,24,8,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,
        1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,54,8,5,1,5,1,5,1,5,1,
        5,1,5,1,5,5,5,62,8,5,10,5,12,5,65,9,5,1,5,0,1,10,6,0,2,4,6,8,10,
        0,3,1,0,13,16,1,0,11,12,1,0,9,10,66,0,15,1,0,0,0,2,23,1,0,0,0,4,
        25,1,0,0,0,6,38,1,0,0,0,8,42,1,0,0,0,10,53,1,0,0,0,12,13,3,2,1,0,
        13,14,5,17,0,0,14,16,1,0,0,0,15,12,1,0,0,0,16,17,1,0,0,0,17,15,1,
        0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,20,5,0,0,1,20,1,1,0,0,0,21,
        24,3,4,2,0,22,24,3,8,4,0,23,21,1,0,0,0,23,22,1,0,0,0,24,3,1,0,0,
        0,25,26,5,1,0,0,26,27,5,4,0,0,27,28,3,8,4,0,28,29,5,17,0,0,29,30,
        3,6,3,0,30,31,5,17,0,0,31,32,3,8,4,0,32,33,5,5,0,0,33,34,5,6,0,0,
        34,35,3,2,1,0,35,36,5,17,0,0,36,37,5,7,0,0,37,5,1,0,0,0,38,39,5,
        18,0,0,39,40,7,0,0,0,40,41,5,19,0,0,41,7,1,0,0,0,42,43,5,18,0,0,
        43,44,5,8,0,0,44,45,3,10,5,0,45,9,1,0,0,0,46,47,6,5,-1,0,47,54,5,
        19,0,0,48,54,5,18,0,0,49,50,5,4,0,0,50,51,3,10,5,0,51,52,5,5,0,0,
        52,54,1,0,0,0,53,46,1,0,0,0,53,48,1,0,0,0,53,49,1,0,0,0,54,63,1,
        0,0,0,55,56,10,5,0,0,56,57,7,1,0,0,57,62,3,10,5,6,58,59,10,4,0,0,
        59,60,7,2,0,0,60,62,3,10,5,5,61,55,1,0,0,0,61,58,1,0,0,0,62,65,1,
        0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,11,1,0,0,0,65,63,1,0,0,0,5,
        17,23,53,61,63
    ]

class ForLangParser ( Parser ):

    grammarFileName = "ForLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'for'", "':'", "'default'", "'('", "')'", 
                     "'{'", "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'>'", 
                     "'<'", "'=='", "'!='", "';'" ]

    symbolicNames = [ "<INVALID>", "FOR", "COLON", "DEFAULT", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "ASSIGN", "PLUS", "MINUS", 
                      "MUL", "DIV", "GT", "LT", "EQ", "NEQ", "SEMI", "ID", 
                      "INT", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_forStmt = 2
    RULE_condicion = 3
    RULE_asignacion = 4
    RULE_expresion = 5

    ruleNames =  [ "programa", "sentencia", "forStmt", "condicion", "asignacion", 
                   "expresion" ]

    EOF = Token.EOF
    FOR=1
    COLON=2
    DEFAULT=3
    LPAREN=4
    RPAREN=5
    LBRACE=6
    RBRACE=7
    ASSIGN=8
    PLUS=9
    MINUS=10
    MUL=11
    DIV=12
    GT=13
    LT=14
    EQ=15
    NEQ=16
    SEMI=17
    ID=18
    INT=19
    WS=20

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
            return self.getToken(ForLangParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(ForLangParser.SentenciaContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ForLangParser.SEMI)
            else:
                return self.getToken(ForLangParser.SEMI, i)

        def getRuleIndex(self):
            return ForLangParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = ForLangParser.ProgramaContext(self, self._ctx, self.state)
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
                self.match(ForLangParser.SEMI)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==18):
                    break

            self.state = 19
            self.match(ForLangParser.EOF)
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

        def forStmt(self):
            return self.getTypedRuleContext(ForLangParser.ForStmtContext,0)


        def asignacion(self):
            return self.getTypedRuleContext(ForLangParser.AsignacionContext,0)


        def getRuleIndex(self):
            return ForLangParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)




    def sentencia(self):

        localctx = ForLangParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.forStmt()
                pass
            elif token in [18]:
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


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ForLangParser.RULE_forStmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class IfElseContext(ForStmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ForStmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FOR(self):
            return self.getToken(ForLangParser.FOR, 0)
        def LPAREN(self):
            return self.getToken(ForLangParser.LPAREN, 0)
        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(ForLangParser.AsignacionContext,i)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(ForLangParser.SEMI)
            else:
                return self.getToken(ForLangParser.SEMI, i)
        def condicion(self):
            return self.getTypedRuleContext(ForLangParser.CondicionContext,0)

        def RPAREN(self):
            return self.getToken(ForLangParser.RPAREN, 0)
        def LBRACE(self):
            return self.getToken(ForLangParser.LBRACE, 0)
        def sentencia(self):
            return self.getTypedRuleContext(ForLangParser.SentenciaContext,0)

        def RBRACE(self):
            return self.getToken(ForLangParser.RBRACE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfElse" ):
                listener.enterIfElse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfElse" ):
                listener.exitIfElse(self)



    def forStmt(self):

        localctx = ForLangParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_forStmt)
        try:
            localctx = ForLangParser.IfElseContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(ForLangParser.FOR)
            self.state = 26
            self.match(ForLangParser.LPAREN)
            self.state = 27
            self.asignacion()
            self.state = 28
            self.match(ForLangParser.SEMI)
            self.state = 29
            self.condicion()
            self.state = 30
            self.match(ForLangParser.SEMI)
            self.state = 31
            self.asignacion()
            self.state = 32
            self.match(ForLangParser.RPAREN)
            self.state = 33
            self.match(ForLangParser.LBRACE)
            self.state = 34
            self.sentencia()
            self.state = 35
            self.match(ForLangParser.SEMI)
            self.state = 36
            self.match(ForLangParser.RBRACE)
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
            return ForLangParser.RULE_condicion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CondicionSimpleContext(CondicionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.CondicionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ForLangParser.ID, 0)
        def INT(self):
            return self.getToken(ForLangParser.INT, 0)
        def GT(self):
            return self.getToken(ForLangParser.GT, 0)
        def LT(self):
            return self.getToken(ForLangParser.LT, 0)
        def EQ(self):
            return self.getToken(ForLangParser.EQ, 0)
        def NEQ(self):
            return self.getToken(ForLangParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicionSimple" ):
                listener.enterCondicionSimple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicionSimple" ):
                listener.exitCondicionSimple(self)



    def condicion(self):

        localctx = ForLangParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            localctx = ForLangParser.CondicionSimpleContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ForLangParser.ID)
            self.state = 39
            localctx.op = self._input.LT(1)
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                localctx.op = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 40
            self.match(ForLangParser.INT)
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
            return ForLangParser.RULE_asignacion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignContext(AsignacionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.AsignacionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ForLangParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(ForLangParser.ASSIGN, 0)
        def expresion(self):
            return self.getTypedRuleContext(ForLangParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def asignacion(self):

        localctx = ForLangParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_asignacion)
        try:
            localctx = ForLangParser.AssignContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ForLangParser.ID)
            self.state = 43
            self.match(ForLangParser.ASSIGN)
            self.state = 44
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
            return ForLangParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(ForLangParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class MulDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(ForLangParser.ExpresionContext,i)

        def MUL(self):
            return self.getToken(ForLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(ForLangParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExpresionContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ForLangParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(ForLangParser.ExpresionContext,i)

        def PLUS(self):
            return self.getToken(ForLangParser.PLUS, 0)
        def MINUS(self):
            return self.getToken(ForLangParser.MINUS, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParensContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAREN(self):
            return self.getToken(ForLangParser.LPAREN, 0)
        def expresion(self):
            return self.getTypedRuleContext(ForLangParser.ExpresionContext,0)

        def RPAREN(self):
            return self.getToken(ForLangParser.RPAREN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class IntContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a ForLangParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(ForLangParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ForLangParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = ForLangParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 47
                self.match(ForLangParser.INT)
                pass
            elif token in [18]:
                localctx = ForLangParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 48
                self.match(ForLangParser.ID)
                pass
            elif token in [4]:
                localctx = ForLangParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 49
                self.match(ForLangParser.LPAREN)
                self.state = 50
                self.expresion(0)
                self.state = 51
                self.match(ForLangParser.RPAREN)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 63
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 61
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = ForLangParser.MulDivContext(self, ForLangParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 55
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 56
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==11 or _la==12):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.expresion(6)
                        pass

                    elif la_ == 2:
                        localctx = ForLangParser.AddSubContext(self, ForLangParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 58
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==9 or _la==10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expresion(5)
                        pass

             
                self.state = 65
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

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
         




