// Generated from /workspaces/compiladores/actividad2/WhileLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class WhileLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, IF=3, ELSE=4, WHILE=5, LPAREN=6, RPAREN=7, LBRACE=8, RBRACE=9, 
		SEMI=10, ASSIGN=11, LT=12, GT=13, GE=14, LE=15, EQ=16, NE=17, PLUS=18, 
		MINUS=19, MUL=20, DIV=21, BREAK=22, CONTINUE=23, ID=24, NUMBER=25, STRING=26, 
		COMMENT=27, WS=28;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "IF", "ELSE", "WHILE", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "SEMI", "ASSIGN", "LT", "GT", "GE", "LE", "EQ", "NE", "PLUS", 
			"MINUS", "MUL", "DIV", "BREAK", "CONTINUE", "ID", "NUMBER", "STRING", 
			"COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'int'", "'string'", "'if'", "'else'", "'while'", "'('", "')'", 
			"'{'", "'}'", "';'", "'='", "'<'", "'>'", "'>='", "'<='", "'=='", "'!='", 
			"'+'", "'-'", "'*'", "'/'", "'break'", "'continue'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "IF", "ELSE", "WHILE", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "SEMI", "ASSIGN", "LT", "GT", "GE", "LE", "EQ", "NE", "PLUS", 
			"MINUS", "MUL", "DIV", "BREAK", "CONTINUE", "ID", "NUMBER", "STRING", 
			"COMMENT", "WS"
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


	public WhileLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "WhileLang.g4"; }

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
		"\u0004\u0000\u001c\u00ae\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a"+
		"\u0002\u001b\u0007\u001b\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016\u0001\u0016"+
		"\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0005\u0017\u0088\b\u0017"+
		"\n\u0017\f\u0017\u008b\t\u0017\u0001\u0018\u0004\u0018\u008e\b\u0018\u000b"+
		"\u0018\f\u0018\u008f\u0001\u0019\u0001\u0019\u0005\u0019\u0094\b\u0019"+
		"\n\u0019\f\u0019\u0097\t\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001"+
		"\u001a\u0001\u001a\u0001\u001a\u0005\u001a\u009f\b\u001a\n\u001a\f\u001a"+
		"\u00a2\t\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001b"+
		"\u0004\u001b\u00a9\b\u001b\u000b\u001b\f\u001b\u00aa\u0001\u001b\u0001"+
		"\u001b\u0001\u00a0\u0000\u001c\u0001\u0001\u0003\u0002\u0005\u0003\u0007"+
		"\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b"+
		"\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013"+
		"\'\u0014)\u0015+\u0016-\u0017/\u00181\u00193\u001a5\u001b7\u001c\u0001"+
		"\u0000\u0005\u0003\u0000AZ__az\u0004\u000009AZ__az\u0001\u000009\u0003"+
		"\u0000\n\n\r\r\"\"\u0003\u0000\t\n\r\r  \u00b2\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000"+
		"#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001"+
		"\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000"+
		"\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/\u0001\u0000\u0000\u0000\u0000"+
		"1\u0001\u0000\u0000\u0000\u00003\u0001\u0000\u0000\u0000\u00005\u0001"+
		"\u0000\u0000\u0000\u00007\u0001\u0000\u0000\u0000\u00019\u0001\u0000\u0000"+
		"\u0000\u0003=\u0001\u0000\u0000\u0000\u0005D\u0001\u0000\u0000\u0000\u0007"+
		"G\u0001\u0000\u0000\u0000\tL\u0001\u0000\u0000\u0000\u000bR\u0001\u0000"+
		"\u0000\u0000\rT\u0001\u0000\u0000\u0000\u000fV\u0001\u0000\u0000\u0000"+
		"\u0011X\u0001\u0000\u0000\u0000\u0013Z\u0001\u0000\u0000\u0000\u0015\\"+
		"\u0001\u0000\u0000\u0000\u0017^\u0001\u0000\u0000\u0000\u0019`\u0001\u0000"+
		"\u0000\u0000\u001bb\u0001\u0000\u0000\u0000\u001de\u0001\u0000\u0000\u0000"+
		"\u001fh\u0001\u0000\u0000\u0000!k\u0001\u0000\u0000\u0000#n\u0001\u0000"+
		"\u0000\u0000%p\u0001\u0000\u0000\u0000\'r\u0001\u0000\u0000\u0000)t\u0001"+
		"\u0000\u0000\u0000+v\u0001\u0000\u0000\u0000-|\u0001\u0000\u0000\u0000"+
		"/\u0085\u0001\u0000\u0000\u00001\u008d\u0001\u0000\u0000\u00003\u0091"+
		"\u0001\u0000\u0000\u00005\u009a\u0001\u0000\u0000\u00007\u00a8\u0001\u0000"+
		"\u0000\u00009:\u0005i\u0000\u0000:;\u0005n\u0000\u0000;<\u0005t\u0000"+
		"\u0000<\u0002\u0001\u0000\u0000\u0000=>\u0005s\u0000\u0000>?\u0005t\u0000"+
		"\u0000?@\u0005r\u0000\u0000@A\u0005i\u0000\u0000AB\u0005n\u0000\u0000"+
		"BC\u0005g\u0000\u0000C\u0004\u0001\u0000\u0000\u0000DE\u0005i\u0000\u0000"+
		"EF\u0005f\u0000\u0000F\u0006\u0001\u0000\u0000\u0000GH\u0005e\u0000\u0000"+
		"HI\u0005l\u0000\u0000IJ\u0005s\u0000\u0000JK\u0005e\u0000\u0000K\b\u0001"+
		"\u0000\u0000\u0000LM\u0005w\u0000\u0000MN\u0005h\u0000\u0000NO\u0005i"+
		"\u0000\u0000OP\u0005l\u0000\u0000PQ\u0005e\u0000\u0000Q\n\u0001\u0000"+
		"\u0000\u0000RS\u0005(\u0000\u0000S\f\u0001\u0000\u0000\u0000TU\u0005)"+
		"\u0000\u0000U\u000e\u0001\u0000\u0000\u0000VW\u0005{\u0000\u0000W\u0010"+
		"\u0001\u0000\u0000\u0000XY\u0005}\u0000\u0000Y\u0012\u0001\u0000\u0000"+
		"\u0000Z[\u0005;\u0000\u0000[\u0014\u0001\u0000\u0000\u0000\\]\u0005=\u0000"+
		"\u0000]\u0016\u0001\u0000\u0000\u0000^_\u0005<\u0000\u0000_\u0018\u0001"+
		"\u0000\u0000\u0000`a\u0005>\u0000\u0000a\u001a\u0001\u0000\u0000\u0000"+
		"bc\u0005>\u0000\u0000cd\u0005=\u0000\u0000d\u001c\u0001\u0000\u0000\u0000"+
		"ef\u0005<\u0000\u0000fg\u0005=\u0000\u0000g\u001e\u0001\u0000\u0000\u0000"+
		"hi\u0005=\u0000\u0000ij\u0005=\u0000\u0000j \u0001\u0000\u0000\u0000k"+
		"l\u0005!\u0000\u0000lm\u0005=\u0000\u0000m\"\u0001\u0000\u0000\u0000n"+
		"o\u0005+\u0000\u0000o$\u0001\u0000\u0000\u0000pq\u0005-\u0000\u0000q&"+
		"\u0001\u0000\u0000\u0000rs\u0005*\u0000\u0000s(\u0001\u0000\u0000\u0000"+
		"tu\u0005/\u0000\u0000u*\u0001\u0000\u0000\u0000vw\u0005b\u0000\u0000w"+
		"x\u0005r\u0000\u0000xy\u0005e\u0000\u0000yz\u0005a\u0000\u0000z{\u0005"+
		"k\u0000\u0000{,\u0001\u0000\u0000\u0000|}\u0005c\u0000\u0000}~\u0005o"+
		"\u0000\u0000~\u007f\u0005n\u0000\u0000\u007f\u0080\u0005t\u0000\u0000"+
		"\u0080\u0081\u0005i\u0000\u0000\u0081\u0082\u0005n\u0000\u0000\u0082\u0083"+
		"\u0005u\u0000\u0000\u0083\u0084\u0005e\u0000\u0000\u0084.\u0001\u0000"+
		"\u0000\u0000\u0085\u0089\u0007\u0000\u0000\u0000\u0086\u0088\u0007\u0001"+
		"\u0000\u0000\u0087\u0086\u0001\u0000\u0000\u0000\u0088\u008b\u0001\u0000"+
		"\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u0089\u008a\u0001\u0000"+
		"\u0000\u0000\u008a0\u0001\u0000\u0000\u0000\u008b\u0089\u0001\u0000\u0000"+
		"\u0000\u008c\u008e\u0007\u0002\u0000\u0000\u008d\u008c\u0001\u0000\u0000"+
		"\u0000\u008e\u008f\u0001\u0000\u0000\u0000\u008f\u008d\u0001\u0000\u0000"+
		"\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u00902\u0001\u0000\u0000\u0000"+
		"\u0091\u0095\u0005\"\u0000\u0000\u0092\u0094\b\u0003\u0000\u0000\u0093"+
		"\u0092\u0001\u0000\u0000\u0000\u0094\u0097\u0001\u0000\u0000\u0000\u0095"+
		"\u0093\u0001\u0000\u0000\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096"+
		"\u0098\u0001\u0000\u0000\u0000\u0097\u0095\u0001\u0000\u0000\u0000\u0098"+
		"\u0099\u0005\"\u0000\u0000\u00994\u0001\u0000\u0000\u0000\u009a\u009b"+
		"\u0005/\u0000\u0000\u009b\u009c\u0005/\u0000\u0000\u009c\u00a0\u0001\u0000"+
		"\u0000\u0000\u009d\u009f\t\u0000\u0000\u0000\u009e\u009d\u0001\u0000\u0000"+
		"\u0000\u009f\u00a2\u0001\u0000\u0000\u0000\u00a0\u00a1\u0001\u0000\u0000"+
		"\u0000\u00a0\u009e\u0001\u0000\u0000\u0000\u00a1\u00a3\u0001\u0000\u0000"+
		"\u0000\u00a2\u00a0\u0001\u0000\u0000\u0000\u00a3\u00a4\u0005\n\u0000\u0000"+
		"\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5\u00a6\u0006\u001a\u0000\u0000"+
		"\u00a66\u0001\u0000\u0000\u0000\u00a7\u00a9\u0007\u0004\u0000\u0000\u00a8"+
		"\u00a7\u0001\u0000\u0000\u0000\u00a9\u00aa\u0001\u0000\u0000\u0000\u00aa"+
		"\u00a8\u0001\u0000\u0000\u0000\u00aa\u00ab\u0001\u0000\u0000\u0000\u00ab"+
		"\u00ac\u0001\u0000\u0000\u0000\u00ac\u00ad\u0006\u001b\u0000\u0000\u00ad"+
		"8\u0001\u0000\u0000\u0000\u0006\u0000\u0089\u008f\u0095\u00a0\u00aa\u0001"+
		"\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}