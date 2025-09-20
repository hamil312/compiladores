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
		MINUS=19, MUL=20, DIV=21, ID=22, NUMBER=23, STRING=24, COMMENT=25, WS=26;
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
			"MINUS", "MUL", "DIV", "ID", "NUMBER", "STRING", "COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'int'", "'string'", "'if'", "'else'", "'while'", "'('", "')'", 
			"'{'", "'}'", "';'", "'='", "'<'", "'>'", "'>='", "'<='", "'=='", "'!='", 
			"'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, "IF", "ELSE", "WHILE", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "SEMI", "ASSIGN", "LT", "GT", "GE", "LE", "EQ", "NE", "PLUS", 
			"MINUS", "MUL", "DIV", "ID", "NUMBER", "STRING", "COMMENT", "WS"
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
		"\u0004\u0000\u001a\u009b\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014"+
		"\u0001\u0014\u0001\u0015\u0001\u0015\u0005\u0015u\b\u0015\n\u0015\f\u0015"+
		"x\t\u0015\u0001\u0016\u0004\u0016{\b\u0016\u000b\u0016\f\u0016|\u0001"+
		"\u0017\u0001\u0017\u0005\u0017\u0081\b\u0017\n\u0017\f\u0017\u0084\t\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0018\u0001\u0018"+
		"\u0005\u0018\u008c\b\u0018\n\u0018\f\u0018\u008f\t\u0018\u0001\u0018\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0004\u0019\u0096\b\u0019\u000b"+
		"\u0019\f\u0019\u0097\u0001\u0019\u0001\u0019\u0001\u008d\u0000\u001a\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017/"+
		"\u00181\u00193\u001a\u0001\u0000\u0005\u0003\u0000AZ__az\u0004\u00000"+
		"9AZ__az\u0001\u000009\u0003\u0000\n\n\r\r\"\"\u0003\u0000\t\n\r\r  \u009f"+
		"\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000"+
		"\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000"+
		"\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000\u0000\u0000/"+
		"\u0001\u0000\u0000\u0000\u00001\u0001\u0000\u0000\u0000\u00003\u0001\u0000"+
		"\u0000\u0000\u00015\u0001\u0000\u0000\u0000\u00039\u0001\u0000\u0000\u0000"+
		"\u0005@\u0001\u0000\u0000\u0000\u0007C\u0001\u0000\u0000\u0000\tH\u0001"+
		"\u0000\u0000\u0000\u000bN\u0001\u0000\u0000\u0000\rP\u0001\u0000\u0000"+
		"\u0000\u000fR\u0001\u0000\u0000\u0000\u0011T\u0001\u0000\u0000\u0000\u0013"+
		"V\u0001\u0000\u0000\u0000\u0015X\u0001\u0000\u0000\u0000\u0017Z\u0001"+
		"\u0000\u0000\u0000\u0019\\\u0001\u0000\u0000\u0000\u001b^\u0001\u0000"+
		"\u0000\u0000\u001da\u0001\u0000\u0000\u0000\u001fd\u0001\u0000\u0000\u0000"+
		"!g\u0001\u0000\u0000\u0000#j\u0001\u0000\u0000\u0000%l\u0001\u0000\u0000"+
		"\u0000\'n\u0001\u0000\u0000\u0000)p\u0001\u0000\u0000\u0000+r\u0001\u0000"+
		"\u0000\u0000-z\u0001\u0000\u0000\u0000/~\u0001\u0000\u0000\u00001\u0087"+
		"\u0001\u0000\u0000\u00003\u0095\u0001\u0000\u0000\u000056\u0005i\u0000"+
		"\u000067\u0005n\u0000\u000078\u0005t\u0000\u00008\u0002\u0001\u0000\u0000"+
		"\u00009:\u0005s\u0000\u0000:;\u0005t\u0000\u0000;<\u0005r\u0000\u0000"+
		"<=\u0005i\u0000\u0000=>\u0005n\u0000\u0000>?\u0005g\u0000\u0000?\u0004"+
		"\u0001\u0000\u0000\u0000@A\u0005i\u0000\u0000AB\u0005f\u0000\u0000B\u0006"+
		"\u0001\u0000\u0000\u0000CD\u0005e\u0000\u0000DE\u0005l\u0000\u0000EF\u0005"+
		"s\u0000\u0000FG\u0005e\u0000\u0000G\b\u0001\u0000\u0000\u0000HI\u0005"+
		"w\u0000\u0000IJ\u0005h\u0000\u0000JK\u0005i\u0000\u0000KL\u0005l\u0000"+
		"\u0000LM\u0005e\u0000\u0000M\n\u0001\u0000\u0000\u0000NO\u0005(\u0000"+
		"\u0000O\f\u0001\u0000\u0000\u0000PQ\u0005)\u0000\u0000Q\u000e\u0001\u0000"+
		"\u0000\u0000RS\u0005{\u0000\u0000S\u0010\u0001\u0000\u0000\u0000TU\u0005"+
		"}\u0000\u0000U\u0012\u0001\u0000\u0000\u0000VW\u0005;\u0000\u0000W\u0014"+
		"\u0001\u0000\u0000\u0000XY\u0005=\u0000\u0000Y\u0016\u0001\u0000\u0000"+
		"\u0000Z[\u0005<\u0000\u0000[\u0018\u0001\u0000\u0000\u0000\\]\u0005>\u0000"+
		"\u0000]\u001a\u0001\u0000\u0000\u0000^_\u0005>\u0000\u0000_`\u0005=\u0000"+
		"\u0000`\u001c\u0001\u0000\u0000\u0000ab\u0005<\u0000\u0000bc\u0005=\u0000"+
		"\u0000c\u001e\u0001\u0000\u0000\u0000de\u0005=\u0000\u0000ef\u0005=\u0000"+
		"\u0000f \u0001\u0000\u0000\u0000gh\u0005!\u0000\u0000hi\u0005=\u0000\u0000"+
		"i\"\u0001\u0000\u0000\u0000jk\u0005+\u0000\u0000k$\u0001\u0000\u0000\u0000"+
		"lm\u0005-\u0000\u0000m&\u0001\u0000\u0000\u0000no\u0005*\u0000\u0000o"+
		"(\u0001\u0000\u0000\u0000pq\u0005/\u0000\u0000q*\u0001\u0000\u0000\u0000"+
		"rv\u0007\u0000\u0000\u0000su\u0007\u0001\u0000\u0000ts\u0001\u0000\u0000"+
		"\u0000ux\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000\u0000vw\u0001\u0000"+
		"\u0000\u0000w,\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000y{\u0007"+
		"\u0002\u0000\u0000zy\u0001\u0000\u0000\u0000{|\u0001\u0000\u0000\u0000"+
		"|z\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000\u0000}.\u0001\u0000\u0000"+
		"\u0000~\u0082\u0005\"\u0000\u0000\u007f\u0081\b\u0003\u0000\u0000\u0080"+
		"\u007f\u0001\u0000\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000\u0082"+
		"\u0080\u0001\u0000\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083"+
		"\u0085\u0001\u0000\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085"+
		"\u0086\u0005\"\u0000\u0000\u00860\u0001\u0000\u0000\u0000\u0087\u0088"+
		"\u0005/\u0000\u0000\u0088\u0089\u0005/\u0000\u0000\u0089\u008d\u0001\u0000"+
		"\u0000\u0000\u008a\u008c\t\u0000\u0000\u0000\u008b\u008a\u0001\u0000\u0000"+
		"\u0000\u008c\u008f\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000"+
		"\u0000\u008d\u008b\u0001\u0000\u0000\u0000\u008e\u0090\u0001\u0000\u0000"+
		"\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u0090\u0091\u0005\n\u0000\u0000"+
		"\u0091\u0092\u0001\u0000\u0000\u0000\u0092\u0093\u0006\u0018\u0000\u0000"+
		"\u00932\u0001\u0000\u0000\u0000\u0094\u0096\u0007\u0004\u0000\u0000\u0095"+
		"\u0094\u0001\u0000\u0000\u0000\u0096\u0097\u0001\u0000\u0000\u0000\u0097"+
		"\u0095\u0001\u0000\u0000\u0000\u0097\u0098\u0001\u0000\u0000\u0000\u0098"+
		"\u0099\u0001\u0000\u0000\u0000\u0099\u009a\u0006\u0019\u0000\u0000\u009a"+
		"4\u0001\u0000\u0000\u0000\u0006\u0000v|\u0082\u008d\u0097\u0001\u0006"+
		"\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}