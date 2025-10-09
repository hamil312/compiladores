# Generated from CSV.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,5,41,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        1,3,1,15,8,1,1,1,1,1,1,2,4,2,20,8,2,11,2,12,2,21,1,3,1,3,1,3,1,3,
        5,3,28,8,3,10,3,12,3,31,9,3,1,3,1,3,1,4,4,4,36,8,4,11,4,12,4,37,
        1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,3,4,0,10,10,13,13,34,34,44,
        44,1,0,34,34,2,0,9,9,32,32,45,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,
        0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,14,1,0,0,0,5,19,1,0,0,0,
        7,23,1,0,0,0,9,35,1,0,0,0,11,12,5,44,0,0,12,2,1,0,0,0,13,15,5,13,
        0,0,14,13,1,0,0,0,14,15,1,0,0,0,15,16,1,0,0,0,16,17,5,10,0,0,17,
        4,1,0,0,0,18,20,8,0,0,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,
        0,21,22,1,0,0,0,22,6,1,0,0,0,23,29,5,34,0,0,24,25,5,34,0,0,25,28,
        5,34,0,0,26,28,8,1,0,0,27,24,1,0,0,0,27,26,1,0,0,0,28,31,1,0,0,0,
        29,27,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,31,29,1,0,0,0,32,33,5,
        34,0,0,33,8,1,0,0,0,34,36,7,2,0,0,35,34,1,0,0,0,36,37,1,0,0,0,37,
        35,1,0,0,0,37,38,1,0,0,0,38,39,1,0,0,0,39,40,6,4,0,0,40,10,1,0,0,
        0,6,0,14,21,27,29,37,1,6,0,0
    ]

class CSVLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    NL = 2
    TEXT = 3
    STRING = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','" ]

    symbolicNames = [ "<INVALID>",
            "NL", "TEXT", "STRING", "WS" ]

    ruleNames = [ "T__0", "NL", "TEXT", "STRING", "WS" ]

    grammarFileName = "CSV.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


