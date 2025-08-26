# Generated from Calculadora.g4 by ANTLR 4.13.2
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
        4,1,12,48,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,3,2,32,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,43,8,
        2,10,2,12,2,46,9,2,1,2,0,1,4,3,0,2,4,0,2,1,0,5,6,2,0,3,3,7,7,52,
        0,8,1,0,0,0,2,12,1,0,0,0,4,31,1,0,0,0,6,9,3,2,1,0,7,9,3,4,2,0,8,
        6,1,0,0,0,8,7,1,0,0,0,9,10,1,0,0,0,10,11,5,0,0,1,11,1,1,0,0,0,12,
        13,5,10,0,0,13,14,5,1,0,0,14,15,3,4,2,0,15,16,5,2,0,0,16,3,1,0,0,
        0,17,18,6,2,-1,0,18,19,5,3,0,0,19,32,3,4,2,8,20,21,5,10,0,0,21,22,
        5,8,0,0,22,23,3,4,2,0,23,24,5,9,0,0,24,32,1,0,0,0,25,26,5,8,0,0,
        26,27,3,4,2,0,27,28,5,9,0,0,28,32,1,0,0,0,29,32,5,11,0,0,30,32,5,
        10,0,0,31,17,1,0,0,0,31,20,1,0,0,0,31,25,1,0,0,0,31,29,1,0,0,0,31,
        30,1,0,0,0,32,44,1,0,0,0,33,34,10,7,0,0,34,35,5,4,0,0,35,43,3,4,
        2,8,36,37,10,6,0,0,37,38,7,0,0,0,38,43,3,4,2,7,39,40,10,5,0,0,40,
        41,7,1,0,0,41,43,3,4,2,6,42,33,1,0,0,0,42,36,1,0,0,0,42,39,1,0,0,
        0,43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,5,1,0,0,0,46,44,1,
        0,0,0,4,8,31,42,44
    ]

class CalculadoraParser ( Parser ):

    grammarFileName = "Calculadora.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'-'", "'^'", "'*'", "'/'", 
                     "'+'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "ID", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_asignacion = 1
    RULE_expresion = 2

    ruleNames =  [ "prog", "asignacion", "expresion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    ID=10
    NUMBER=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CalculadoraParser.EOF, 0)

        def asignacion(self):
            return self.getTypedRuleContext(CalculadoraParser.AsignacionContext,0)


        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CalculadoraParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 6
                self.asignacion()
                pass

            elif la_ == 2:
                self.state = 7
                self.expresion(0)
                pass


            self.state = 10
            self.match(CalculadoraParser.EOF)
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

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def getRuleIndex(self):
            return CalculadoraParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = CalculadoraParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.match(CalculadoraParser.ID)
            self.state = 13
            self.match(CalculadoraParser.T__0)
            self.state = 14
            self.expresion(0)
            self.state = 15
            self.match(CalculadoraParser.T__1)
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
            return CalculadoraParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(CalculadoraParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)


    class FuncionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)
        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)


    class VariableContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculadoraParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)


    class PotenciaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotencia" ):
                listener.enterPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotencia" ):
                listener.exitPotencia(self)


    class NegativoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativo" ):
                listener.enterNegativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativo" ):
                listener.exitNegativo(self)


    class MultDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDiv" ):
                listener.enterMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDiv" ):
                listener.exitMultDiv(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculadoraParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CalculadoraParser.NegativoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 18
                self.match(CalculadoraParser.T__2)
                self.state = 19
                self.expresion(8)
                pass

            elif la_ == 2:
                localctx = CalculadoraParser.FuncionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                self.match(CalculadoraParser.ID)
                self.state = 21
                self.match(CalculadoraParser.T__7)
                self.state = 22
                self.expresion(0)
                self.state = 23
                self.match(CalculadoraParser.T__8)
                pass

            elif la_ == 3:
                localctx = CalculadoraParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(CalculadoraParser.T__7)
                self.state = 26
                self.expresion(0)
                self.state = 27
                self.match(CalculadoraParser.T__8)
                pass

            elif la_ == 4:
                localctx = CalculadoraParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(CalculadoraParser.NUMBER)
                pass

            elif la_ == 5:
                localctx = CalculadoraParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(CalculadoraParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 42
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CalculadoraParser.PotenciaContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 33
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 34
                        self.match(CalculadoraParser.T__3)
                        self.state = 35
                        self.expresion(8)
                        pass

                    elif la_ == 2:
                        localctx = CalculadoraParser.MultDivContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 36
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 37
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        self.expresion(7)
                        pass

                    elif la_ == 3:
                        localctx = CalculadoraParser.AddSubContext(self, CalculadoraParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 39
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 40
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==7):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 41
                        self.expresion(6)
                        pass

             
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        self._predicates[2] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         




