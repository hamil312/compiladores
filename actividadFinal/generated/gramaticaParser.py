# Generated from gramatica.g4 by ANTLR 4.13.2
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
        4,1,30,161,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,3,1,43,8,1,1,2,1,2,1,2,1,2,3,2,49,8,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,66,8,4,1,5,1,5,1,5,1,5,1,
        5,1,5,1,6,1,6,5,6,76,8,6,10,6,12,6,79,9,6,1,6,1,6,1,7,1,7,1,7,1,
        7,1,7,1,7,5,7,89,8,7,10,7,12,7,92,9,7,1,8,1,8,1,8,1,8,1,8,1,8,5,
        8,100,8,8,10,8,12,8,103,9,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,3,9,115,8,9,1,10,1,10,1,10,1,10,1,11,1,11,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,5,12,132,8,12,10,12,12,12,135,9,12,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,146,8,13,10,13,12,13,
        149,9,13,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,159,8,14,1,
        14,0,4,14,16,24,26,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,
        1,1,0,20,25,167,0,31,1,0,0,0,2,42,1,0,0,0,4,44,1,0,0,0,6,52,1,0,
        0,0,8,58,1,0,0,0,10,67,1,0,0,0,12,73,1,0,0,0,14,82,1,0,0,0,16,93,
        1,0,0,0,18,114,1,0,0,0,20,116,1,0,0,0,22,120,1,0,0,0,24,122,1,0,
        0,0,26,136,1,0,0,0,28,158,1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,
        33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,35,36,5,0,0,
        1,36,1,1,0,0,0,37,43,3,4,2,0,38,43,3,6,3,0,39,43,3,8,4,0,40,43,3,
        10,5,0,41,43,3,12,6,0,42,37,1,0,0,0,42,38,1,0,0,0,42,39,1,0,0,0,
        42,40,1,0,0,0,42,41,1,0,0,0,43,3,1,0,0,0,44,45,5,26,0,0,45,48,5,
        10,0,0,46,49,3,14,7,0,47,49,3,24,12,0,48,46,1,0,0,0,48,47,1,0,0,
        0,49,50,1,0,0,0,50,51,5,11,0,0,51,5,1,0,0,0,52,53,5,7,0,0,53,54,
        5,12,0,0,54,55,5,26,0,0,55,56,5,13,0,0,56,57,5,11,0,0,57,7,1,0,0,
        0,58,59,5,4,0,0,59,60,5,12,0,0,60,61,3,14,7,0,61,62,5,13,0,0,62,
        65,3,12,6,0,63,64,5,5,0,0,64,66,3,12,6,0,65,63,1,0,0,0,65,66,1,0,
        0,0,66,9,1,0,0,0,67,68,5,6,0,0,68,69,5,12,0,0,69,70,3,14,7,0,70,
        71,5,13,0,0,71,72,3,12,6,0,72,11,1,0,0,0,73,77,5,14,0,0,74,76,3,
        2,1,0,75,74,1,0,0,0,76,79,1,0,0,0,77,75,1,0,0,0,77,78,1,0,0,0,78,
        80,1,0,0,0,79,77,1,0,0,0,80,81,5,15,0,0,81,13,1,0,0,0,82,83,6,7,
        -1,0,83,84,3,16,8,0,84,90,1,0,0,0,85,86,10,2,0,0,86,87,5,2,0,0,87,
        89,3,16,8,0,88,85,1,0,0,0,89,92,1,0,0,0,90,88,1,0,0,0,90,91,1,0,
        0,0,91,15,1,0,0,0,92,90,1,0,0,0,93,94,6,8,-1,0,94,95,3,18,9,0,95,
        101,1,0,0,0,96,97,10,2,0,0,97,98,5,1,0,0,98,100,3,18,9,0,99,96,1,
        0,0,0,100,103,1,0,0,0,101,99,1,0,0,0,101,102,1,0,0,0,102,17,1,0,
        0,0,103,101,1,0,0,0,104,105,5,3,0,0,105,115,3,18,9,0,106,107,5,12,
        0,0,107,108,3,14,7,0,108,109,5,13,0,0,109,115,1,0,0,0,110,115,5,
        8,0,0,111,115,5,9,0,0,112,115,5,26,0,0,113,115,3,20,10,0,114,104,
        1,0,0,0,114,106,1,0,0,0,114,110,1,0,0,0,114,111,1,0,0,0,114,112,
        1,0,0,0,114,113,1,0,0,0,115,19,1,0,0,0,116,117,3,24,12,0,117,118,
        3,22,11,0,118,119,3,24,12,0,119,21,1,0,0,0,120,121,7,0,0,0,121,23,
        1,0,0,0,122,123,6,12,-1,0,123,124,3,26,13,0,124,133,1,0,0,0,125,
        126,10,3,0,0,126,127,5,16,0,0,127,132,3,26,13,0,128,129,10,2,0,0,
        129,130,5,17,0,0,130,132,3,26,13,0,131,125,1,0,0,0,131,128,1,0,0,
        0,132,135,1,0,0,0,133,131,1,0,0,0,133,134,1,0,0,0,134,25,1,0,0,0,
        135,133,1,0,0,0,136,137,6,13,-1,0,137,138,3,28,14,0,138,147,1,0,
        0,0,139,140,10,3,0,0,140,141,5,18,0,0,141,146,3,28,14,0,142,143,
        10,2,0,0,143,144,5,19,0,0,144,146,3,28,14,0,145,139,1,0,0,0,145,
        142,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,
        27,1,0,0,0,149,147,1,0,0,0,150,151,5,17,0,0,151,159,3,28,14,0,152,
        153,5,12,0,0,153,154,3,24,12,0,154,155,5,13,0,0,155,159,1,0,0,0,
        156,159,5,27,0,0,157,159,5,26,0,0,158,150,1,0,0,0,158,152,1,0,0,
        0,158,156,1,0,0,0,158,157,1,0,0,0,159,29,1,0,0,0,13,33,42,48,65,
        77,90,101,114,131,133,145,147,158
    ]

class gramaticaParser ( Parser ):

    grammarFileName = "gramatica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'='", "';'", "'('", "')'", 
                     "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
                     "'<='", "'>='", "'<'", "'>'" ]

    symbolicNames = [ "<INVALID>", "AND", "OR", "NOT", "IF", "ELSE", "WHILE", 
                      "PRINT", "TRUE", "FALSE", "ASSIGN", "SEMI", "LPAREN", 
                      "RPAREN", "LBRACE", "RBRACE", "ADD", "SUB", "MUL", 
                      "DIV", "EQ", "NEQ", "LTE", "GTE", "LT", "GT", "ID", 
                      "INT", "WS", "LINE_COMMENT", "BLOCK_COMMENT" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_assignment = 2
    RULE_printStmt = 3
    RULE_ifStmt = 4
    RULE_whileStmt = 5
    RULE_block = 6
    RULE_boolExpr = 7
    RULE_boolTerm = 8
    RULE_boolFactor = 9
    RULE_comparison = 10
    RULE_compOp = 11
    RULE_arithExpr = 12
    RULE_arithTerm = 13
    RULE_arithFactor = 14

    ruleNames =  [ "program", "statement", "assignment", "printStmt", "ifStmt", 
                   "whileStmt", "block", "boolExpr", "boolTerm", "boolFactor", 
                   "comparison", "compOp", "arithExpr", "arithTerm", "arithFactor" ]

    EOF = Token.EOF
    AND=1
    OR=2
    NOT=3
    IF=4
    ELSE=5
    WHILE=6
    PRINT=7
    TRUE=8
    FALSE=9
    ASSIGN=10
    SEMI=11
    LPAREN=12
    RPAREN=13
    LBRACE=14
    RBRACE=15
    ADD=16
    SUB=17
    MUL=18
    DIV=19
    EQ=20
    NEQ=21
    LTE=22
    GTE=23
    LT=24
    GT=25
    ID=26
    INT=27
    WS=28
    LINE_COMMENT=29
    BLOCK_COMMENT=30

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
            return self.getToken(gramaticaParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_program

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

        localctx = gramaticaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.statement()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 67125456) != 0)):
                    break

            self.state = 35
            self.match(gramaticaParser.EOF)
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
            return self.getTypedRuleContext(gramaticaParser.AssignmentContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(gramaticaParser.PrintStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(gramaticaParser.IfStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(gramaticaParser.WhileStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(gramaticaParser.BlockContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_statement

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

        localctx = gramaticaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 42
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.assignment()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 38
                self.printStmt()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.ifStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.whileStmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.block()
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


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(gramaticaParser.ASSIGN, 0)

        def SEMI(self):
            return self.getToken(gramaticaParser.SEMI, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(gramaticaParser.BoolExprContext,0)


        def arithExpr(self):
            return self.getTypedRuleContext(gramaticaParser.ArithExprContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_assignment

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

        localctx = gramaticaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(gramaticaParser.ID)
            self.state = 45
            self.match(gramaticaParser.ASSIGN)
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 46
                self.boolExpr(0)
                pass

            elif la_ == 2:
                self.state = 47
                self.arithExpr(0)
                pass


            self.state = 50
            self.match(gramaticaParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(gramaticaParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(gramaticaParser.LPAREN, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def RPAREN(self):
            return self.getToken(gramaticaParser.RPAREN, 0)

        def SEMI(self):
            return self.getToken(gramaticaParser.SEMI, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = gramaticaParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(gramaticaParser.PRINT)
            self.state = 53
            self.match(gramaticaParser.LPAREN)
            self.state = 54
            self.match(gramaticaParser.ID)
            self.state = 55
            self.match(gramaticaParser.RPAREN)
            self.state = 56
            self.match(gramaticaParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(gramaticaParser.IF, 0)

        def LPAREN(self):
            return self.getToken(gramaticaParser.LPAREN, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(gramaticaParser.BoolExprContext,0)


        def RPAREN(self):
            return self.getToken(gramaticaParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.BlockContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(gramaticaParser.ELSE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = gramaticaParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(gramaticaParser.IF)
            self.state = 59
            self.match(gramaticaParser.LPAREN)
            self.state = 60
            self.boolExpr(0)
            self.state = 61
            self.match(gramaticaParser.RPAREN)
            self.state = 62
            self.block()
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 63
                self.match(gramaticaParser.ELSE)
                self.state = 64
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(gramaticaParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(gramaticaParser.LPAREN, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(gramaticaParser.BoolExprContext,0)


        def RPAREN(self):
            return self.getToken(gramaticaParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(gramaticaParser.BlockContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = gramaticaParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.match(gramaticaParser.WHILE)
            self.state = 68
            self.match(gramaticaParser.LPAREN)
            self.state = 69
            self.boolExpr(0)
            self.state = 70
            self.match(gramaticaParser.RPAREN)
            self.state = 71
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
            return self.getToken(gramaticaParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(gramaticaParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.StatementContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.StatementContext,i)


        def getRuleIndex(self):
            return gramaticaParser.RULE_block

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

        localctx = gramaticaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(gramaticaParser.LBRACE)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67125456) != 0):
                self.state = 74
                self.statement()
                self.state = 79
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 80
            self.match(gramaticaParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolTerm(self):
            return self.getTypedRuleContext(gramaticaParser.BoolTermContext,0)


        def boolExpr(self):
            return self.getTypedRuleContext(gramaticaParser.BoolExprContext,0)


        def OR(self):
            return self.getToken(gramaticaParser.OR, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_boolExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolExpr" ):
                listener.enterBoolExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolExpr" ):
                listener.exitBoolExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolExpr" ):
                return visitor.visitBoolExpr(self)
            else:
                return visitor.visitChildren(self)



    def boolExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.BoolExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_boolExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.boolTerm(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 90
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.BoolExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolExpr)
                    self.state = 85
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 86
                    self.match(gramaticaParser.OR)
                    self.state = 87
                    self.boolTerm(0) 
                self.state = 92
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BoolTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def boolFactor(self):
            return self.getTypedRuleContext(gramaticaParser.BoolFactorContext,0)


        def boolTerm(self):
            return self.getTypedRuleContext(gramaticaParser.BoolTermContext,0)


        def AND(self):
            return self.getToken(gramaticaParser.AND, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_boolTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolTerm" ):
                listener.enterBoolTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolTerm" ):
                listener.exitBoolTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolTerm" ):
                return visitor.visitBoolTerm(self)
            else:
                return visitor.visitChildren(self)



    def boolTerm(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.BoolTermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_boolTerm, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.boolFactor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 101
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = gramaticaParser.BoolTermContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_boolTerm)
                    self.state = 96
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 97
                    self.match(gramaticaParser.AND)
                    self.state = 98
                    self.boolFactor() 
                self.state = 103
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BoolFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(gramaticaParser.NOT, 0)

        def boolFactor(self):
            return self.getTypedRuleContext(gramaticaParser.BoolFactorContext,0)


        def LPAREN(self):
            return self.getToken(gramaticaParser.LPAREN, 0)

        def boolExpr(self):
            return self.getTypedRuleContext(gramaticaParser.BoolExprContext,0)


        def RPAREN(self):
            return self.getToken(gramaticaParser.RPAREN, 0)

        def TRUE(self):
            return self.getToken(gramaticaParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(gramaticaParser.FALSE, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def comparison(self):
            return self.getTypedRuleContext(gramaticaParser.ComparisonContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_boolFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolFactor" ):
                listener.enterBoolFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolFactor" ):
                listener.exitBoolFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolFactor" ):
                return visitor.visitBoolFactor(self)
            else:
                return visitor.visitChildren(self)




    def boolFactor(self):

        localctx = gramaticaParser.BoolFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_boolFactor)
        try:
            self.state = 114
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(gramaticaParser.NOT)
                self.state = 105
                self.boolFactor()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.match(gramaticaParser.LPAREN)
                self.state = 107
                self.boolExpr(0)
                self.state = 108
                self.match(gramaticaParser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 110
                self.match(gramaticaParser.TRUE)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 111
                self.match(gramaticaParser.FALSE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 112
                self.match(gramaticaParser.ID)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 113
                self.comparison()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithExpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticaParser.ArithExprContext)
            else:
                return self.getTypedRuleContext(gramaticaParser.ArithExprContext,i)


        def compOp(self):
            return self.getTypedRuleContext(gramaticaParser.CompOpContext,0)


        def getRuleIndex(self):
            return gramaticaParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = gramaticaParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_comparison)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.arithExpr(0)
            self.state = 117
            self.compOp()
            self.state = 118
            self.arithExpr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(gramaticaParser.EQ, 0)

        def NEQ(self):
            return self.getToken(gramaticaParser.NEQ, 0)

        def LT(self):
            return self.getToken(gramaticaParser.LT, 0)

        def LTE(self):
            return self.getToken(gramaticaParser.LTE, 0)

        def GT(self):
            return self.getToken(gramaticaParser.GT, 0)

        def GTE(self):
            return self.getToken(gramaticaParser.GTE, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_compOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompOp" ):
                listener.enterCompOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompOp" ):
                listener.exitCompOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompOp" ):
                return visitor.visitCompOp(self)
            else:
                return visitor.visitChildren(self)




    def compOp(self):

        localctx = gramaticaParser.CompOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_compOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
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


    class ArithExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithTerm(self):
            return self.getTypedRuleContext(gramaticaParser.ArithTermContext,0)


        def arithExpr(self):
            return self.getTypedRuleContext(gramaticaParser.ArithExprContext,0)


        def ADD(self):
            return self.getToken(gramaticaParser.ADD, 0)

        def SUB(self):
            return self.getToken(gramaticaParser.SUB, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_arithExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithExpr" ):
                listener.enterArithExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithExpr" ):
                listener.exitArithExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithExpr" ):
                return visitor.visitArithExpr(self)
            else:
                return visitor.visitChildren(self)



    def arithExpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ArithExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_arithExpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.arithTerm(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 133
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 131
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ArithExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                        self.state = 125
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 126
                        self.match(gramaticaParser.ADD)
                        self.state = 127
                        self.arithTerm(0)
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.ArithExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithExpr)
                        self.state = 128
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 129
                        self.match(gramaticaParser.SUB)
                        self.state = 130
                        self.arithTerm(0)
                        pass

             
                self.state = 135
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithFactor(self):
            return self.getTypedRuleContext(gramaticaParser.ArithFactorContext,0)


        def arithTerm(self):
            return self.getTypedRuleContext(gramaticaParser.ArithTermContext,0)


        def MUL(self):
            return self.getToken(gramaticaParser.MUL, 0)

        def DIV(self):
            return self.getToken(gramaticaParser.DIV, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_arithTerm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithTerm" ):
                listener.enterArithTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithTerm" ):
                listener.exitArithTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithTerm" ):
                return visitor.visitArithTerm(self)
            else:
                return visitor.visitChildren(self)



    def arithTerm(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = gramaticaParser.ArithTermContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_arithTerm, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.arithFactor()
            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 145
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = gramaticaParser.ArithTermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithTerm)
                        self.state = 139
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 140
                        self.match(gramaticaParser.MUL)
                        self.state = 141
                        self.arithFactor()
                        pass

                    elif la_ == 2:
                        localctx = gramaticaParser.ArithTermContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithTerm)
                        self.state = 142
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 143
                        self.match(gramaticaParser.DIV)
                        self.state = 144
                        self.arithFactor()
                        pass

             
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArithFactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUB(self):
            return self.getToken(gramaticaParser.SUB, 0)

        def arithFactor(self):
            return self.getTypedRuleContext(gramaticaParser.ArithFactorContext,0)


        def LPAREN(self):
            return self.getToken(gramaticaParser.LPAREN, 0)

        def arithExpr(self):
            return self.getTypedRuleContext(gramaticaParser.ArithExprContext,0)


        def RPAREN(self):
            return self.getToken(gramaticaParser.RPAREN, 0)

        def INT(self):
            return self.getToken(gramaticaParser.INT, 0)

        def ID(self):
            return self.getToken(gramaticaParser.ID, 0)

        def getRuleIndex(self):
            return gramaticaParser.RULE_arithFactor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithFactor" ):
                listener.enterArithFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithFactor" ):
                listener.exitArithFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithFactor" ):
                return visitor.visitArithFactor(self)
            else:
                return visitor.visitChildren(self)




    def arithFactor(self):

        localctx = gramaticaParser.ArithFactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_arithFactor)
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 150
                self.match(gramaticaParser.SUB)
                self.state = 151
                self.arithFactor()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 152
                self.match(gramaticaParser.LPAREN)
                self.state = 153
                self.arithExpr(0)
                self.state = 154
                self.match(gramaticaParser.RPAREN)
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 3)
                self.state = 156
                self.match(gramaticaParser.INT)
                pass
            elif token in [26]:
                self.enterOuterAlt(localctx, 4)
                self.state = 157
                self.match(gramaticaParser.ID)
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[7] = self.boolExpr_sempred
        self._predicates[8] = self.boolTerm_sempred
        self._predicates[12] = self.arithExpr_sempred
        self._predicates[13] = self.arithTerm_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def boolExpr_sempred(self, localctx:BoolExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def boolTerm_sempred(self, localctx:BoolTermContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def arithExpr_sempred(self, localctx:ArithExprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def arithTerm_sempred(self, localctx:ArithTermContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




