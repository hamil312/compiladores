// Generated from /workspaces/compiladores/actividad3/IfElseLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class IfElseLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, IF=7, ELSE=8, LPAREN=9, 
		RPAREN=10, LBRACE=11, RBRACE=12, SEMI=13, ASSIGN=14, LT=15, GT=16, GE=17, 
		LE=18, NE=19, PLUS=20, MINUS=21, MULT=22, DIV=23, ID=24, NUMBER=25, STRING=26, 
		COMMENT=27, WS=28;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "IF", "ELSE", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "SEMI", "ASSIGN", "LT", "GT", "GE", "LE", 
			"NE", "PLUS", "MINUS", "MULT", "DIV", "ID", "NUMBER", "STRING", "COMMENT", 
			"WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'return'", "','", "'int'", "'float'", "'void'", "'string'", "'if'", 
			"'else'", "'('", "')'", "'{'", "'}'", "';'", "'='", "'<'", "'>'", "'>='", 
			"'<='", "'!='", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "IF", "ELSE", "LPAREN", "RPAREN", 
			"LBRACE", "RBRACE", "SEMI", "ASSIGN", "LT", "GT", "GE", "LE", "NE", "PLUS", 
			"MINUS", "MULT", "DIV", "ID", "NUMBER", "STRING", "COMMENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public IfElseLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "IfElseLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u001c\u00aa\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a"+
		"\u0002\u001b\u0007\u001b\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001\u0017\u0001"+
		"\u0017\u0005\u0017\u0084\b\u0017\n\u0017\f\u0017\u0087\t\u0017\u0001\u0018"+
		"\u0004\u0018\u008a\b\u0018\u000b\u0018\f\u0018\u008b\u0001\u0019\u0001"+
		"\u0019\u0005\u0019\u0090\b\u0019\n\u0019\f\u0019\u0093\t\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0005\u001a"+
		"\u009b\b\u001a\n\u001a\f\u001a\u009e\t\u001a\u0001\u001a\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001b\u0004\u001b\u00a5\b\u001b\u000b\u001b\f"+
		"\u001b\u00a6\u0001\u001b\u0001\u001b\u0001\u009c\u0000\u001c\u0001\u0001"+
		"\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f"+
		"\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f"+
		"\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/\u0018"+
		"1\u00193\u001a5\u001b7\u001c\u0001\u0000\u0005\u0003\u0000AZ__az\u0004"+
		"\u000009AZ__az\u0001\u000009\u0003\u0000\n\n\r\r\"\"\u0003\u0000\t\n\r"+
		"\r  \u00ae\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0000/\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u0000"+
		"3\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00007\u0001"+
		"\u0000\u0000\u0000\u00019\u0001\u0000\u0000\u0000\u0003@\u0001\u0000\u0000"+
		"\u0000\u0005B\u0001\u0000\u0000\u0000\u0007F\u0001\u0000\u0000\u0000\t"+
		"L\u0001\u0000\u0000\u0000\u000bQ\u0001\u0000\u0000\u0000\rX\u0001\u0000"+
		"\u0000\u0000\u000f[\u0001\u0000\u0000\u0000\u0011`\u0001\u0000\u0000\u0000"+
		"\u0013b\u0001\u0000\u0000\u0000\u0015d\u0001\u0000\u0000\u0000\u0017f"+
		"\u0001\u0000\u0000\u0000\u0019h\u0001\u0000\u0000\u0000\u001bj\u0001\u0000"+
		"\u0000\u0000\u001dl\u0001\u0000\u0000\u0000\u001fn\u0001\u0000\u0000\u0000"+
		"!p\u0001\u0000\u0000\u0000#s\u0001\u0000\u0000\u0000%v\u0001\u0000\u0000"+
		"\u0000\'y\u0001\u0000\u0000\u0000){\u0001\u0000\u0000\u0000+}\u0001\u0000"+
		"\u0000\u0000-\u007f\u0001\u0000\u0000\u0000/\u0081\u0001\u0000\u0000\u0000"+
		"1\u0089\u0001\u0000\u0000\u00003\u008d\u0001\u0000\u0000\u00005\u0096"+
		"\u0001\u0000\u0000\u00007\u00a4\u0001\u0000\u0000\u00009:\u0005r\u0000"+
		"\u0000:;\u0005e\u0000\u0000;<\u0005t\u0000\u0000<=\u0005u\u0000\u0000"+
		"=>\u0005r\u0000\u0000>?\u0005n\u0000\u0000?\u0002\u0001\u0000\u0000\u0000"+
		"@A\u0005,\u0000\u0000A\u0004\u0001\u0000\u0000\u0000BC\u0005i\u0000\u0000"+
		"CD\u0005n\u0000\u0000DE\u0005t\u0000\u0000E\u0006\u0001\u0000\u0000\u0000"+
		"FG\u0005f\u0000\u0000GH\u0005l\u0000\u0000HI\u0005o\u0000\u0000IJ\u0005"+
		"a\u0000\u0000JK\u0005t\u0000\u0000K\b\u0001\u0000\u0000\u0000LM\u0005"+
		"v\u0000\u0000MN\u0005o\u0000\u0000NO\u0005i\u0000\u0000OP\u0005d\u0000"+
		"\u0000P\n\u0001\u0000\u0000\u0000QR\u0005s\u0000\u0000RS\u0005t\u0000"+
		"\u0000ST\u0005r\u0000\u0000TU\u0005i\u0000\u0000UV\u0005n\u0000\u0000"+
		"VW\u0005g\u0000\u0000W\f\u0001\u0000\u0000\u0000XY\u0005i\u0000\u0000"+
		"YZ\u0005f\u0000\u0000Z\u000e\u0001\u0000\u0000\u0000[\\\u0005e\u0000\u0000"+
		"\\]\u0005l\u0000\u0000]^\u0005s\u0000\u0000^_\u0005e\u0000\u0000_\u0010"+
		"\u0001\u0000\u0000\u0000`a\u0005(\u0000\u0000a\u0012\u0001\u0000\u0000"+
		"\u0000bc\u0005)\u0000\u0000c\u0014\u0001\u0000\u0000\u0000de\u0005{\u0000"+
		"\u0000e\u0016\u0001\u0000\u0000\u0000fg\u0005}\u0000\u0000g\u0018\u0001"+
		"\u0000\u0000\u0000hi\u0005;\u0000\u0000i\u001a\u0001\u0000\u0000\u0000"+
		"jk\u0005=\u0000\u0000k\u001c\u0001\u0000\u0000\u0000lm\u0005<\u0000\u0000"+
		"m\u001e\u0001\u0000\u0000\u0000no\u0005>\u0000\u0000o \u0001\u0000\u0000"+
		"\u0000pq\u0005>\u0000\u0000qr\u0005=\u0000\u0000r\"\u0001\u0000\u0000"+
		"\u0000st\u0005<\u0000\u0000tu\u0005=\u0000\u0000u$\u0001\u0000\u0000\u0000"+
		"vw\u0005!\u0000\u0000wx\u0005=\u0000\u0000x&\u0001\u0000\u0000\u0000y"+
		"z\u0005+\u0000\u0000z(\u0001\u0000\u0000\u0000{|\u0005-\u0000\u0000|*"+
		"\u0001\u0000\u0000\u0000}~\u0005*\u0000\u0000~,\u0001\u0000\u0000\u0000"+
		"\u007f\u0080\u0005/\u0000\u0000\u0080.\u0001\u0000\u0000\u0000\u0081\u0085"+
		"\u0007\u0000\u0000\u0000\u0082\u0084\u0007\u0001\u0000\u0000\u0083\u0082"+
		"\u0001\u0000\u0000\u0000\u0084\u0087\u0001\u0000\u0000\u0000\u0085\u0083"+
		"\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000\u00860\u0001"+
		"\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0088\u008a\u0007"+
		"\u0002\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000\u008a\u008b\u0001"+
		"\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000\u0000\u008b\u008c\u0001"+
		"\u0000\u0000\u0000\u008c2\u0001\u0000\u0000\u0000\u008d\u0091\u0005\""+
		"\u0000\u0000\u008e\u0090\b\u0003\u0000\u0000\u008f\u008e\u0001\u0000\u0000"+
		"\u0000\u0090\u0093\u0001\u0000\u0000\u0000\u0091\u008f\u0001\u0000\u0000"+
		"\u0000\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0094\u0001\u0000\u0000"+
		"\u0000\u0093\u0091\u0001\u0000\u0000\u0000\u0094\u0095\u0005\"\u0000\u0000"+
		"\u00954\u0001\u0000\u0000\u0000\u0096\u0097\u0005/\u0000\u0000\u0097\u0098"+
		"\u0005/\u0000\u0000\u0098\u009c\u0001\u0000\u0000\u0000\u0099\u009b\t"+
		"\u0000\u0000\u0000\u009a\u0099\u0001\u0000\u0000\u0000\u009b\u009e\u0001"+
		"\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009c\u009a\u0001"+
		"\u0000\u0000\u0000\u009d\u009f\u0001\u0000\u0000\u0000\u009e\u009c\u0001"+
		"\u0000\u0000\u0000\u009f\u00a0\u0005\n\u0000\u0000\u00a0\u00a1\u0001\u0000"+
		"\u0000\u0000\u00a1\u00a2\u0006\u001a\u0000\u0000\u00a26\u0001\u0000\u0000"+
		"\u0000\u00a3\u00a5\u0007\u0004\u0000\u0000\u00a4\u00a3\u0001\u0000\u0000"+
		"\u0000\u00a5\u00a6\u0001\u0000\u0000\u0000\u00a6\u00a4\u0001\u0000\u0000"+
		"\u0000\u00a6\u00a7\u0001\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000"+
		"\u0000\u00a8\u00a9\u0006\u001b\u0000\u0000\u00a98\u0001\u0000\u0000\u0000"+
		"\u0006\u0000\u0085\u008b\u0091\u009c\u00a6\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}