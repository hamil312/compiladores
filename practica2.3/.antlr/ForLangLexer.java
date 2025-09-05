// Generated from /workspaces/compiladores/practica2.3/ForLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class ForLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		FOR=1, COLON=2, DEFAULT=3, LPAREN=4, RPAREN=5, LBRACE=6, RBRACE=7, ASSIGN=8, 
		PLUS=9, MINUS=10, MUL=11, DIV=12, GT=13, LT=14, EQ=15, NEQ=16, SEMI=17, 
		ID=18, INT=19, WS=20;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"FOR", "COLON", "DEFAULT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "ASSIGN", 
			"PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "EQ", "NEQ", "SEMI", "ID", 
			"INT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'for'", "':'", "'default'", "'('", "')'", "'{'", "'}'", "'='", 
			"'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'=='", "'!='", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "FOR", "COLON", "DEFAULT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
			"ASSIGN", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "EQ", "NEQ", "SEMI", 
			"ID", "INT", "WS"
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


	public ForLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "ForLang.g4"; }

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
		"\u0004\u0000\u0014h\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0005\u0011X\b\u0011"+
		"\n\u0011\f\u0011[\t\u0011\u0001\u0012\u0004\u0012^\b\u0012\u000b\u0012"+
		"\f\u0012_\u0001\u0013\u0004\u0013c\b\u0013\u000b\u0013\f\u0013d\u0001"+
		"\u0013\u0001\u0013\u0000\u0000\u0014\u0001\u0001\u0003\u0002\u0005\u0003"+
		"\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015"+
		"\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012"+
		"%\u0013\'\u0014\u0001\u0000\u0004\u0003\u0000AZ__az\u0004\u000009AZ__"+
		"az\u0001\u000009\u0003\u0000\t\n\r\r  j\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000"+
		"\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000"+
		"\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001"+
		"\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000"+
		"\u0000\u0000\u0001)\u0001\u0000\u0000\u0000\u0003-\u0001\u0000\u0000\u0000"+
		"\u0005/\u0001\u0000\u0000\u0000\u00077\u0001\u0000\u0000\u0000\t9\u0001"+
		"\u0000\u0000\u0000\u000b;\u0001\u0000\u0000\u0000\r=\u0001\u0000\u0000"+
		"\u0000\u000f?\u0001\u0000\u0000\u0000\u0011A\u0001\u0000\u0000\u0000\u0013"+
		"C\u0001\u0000\u0000\u0000\u0015E\u0001\u0000\u0000\u0000\u0017G\u0001"+
		"\u0000\u0000\u0000\u0019I\u0001\u0000\u0000\u0000\u001bK\u0001\u0000\u0000"+
		"\u0000\u001dM\u0001\u0000\u0000\u0000\u001fP\u0001\u0000\u0000\u0000!"+
		"S\u0001\u0000\u0000\u0000#U\u0001\u0000\u0000\u0000%]\u0001\u0000\u0000"+
		"\u0000\'b\u0001\u0000\u0000\u0000)*\u0005f\u0000\u0000*+\u0005o\u0000"+
		"\u0000+,\u0005r\u0000\u0000,\u0002\u0001\u0000\u0000\u0000-.\u0005:\u0000"+
		"\u0000.\u0004\u0001\u0000\u0000\u0000/0\u0005d\u0000\u000001\u0005e\u0000"+
		"\u000012\u0005f\u0000\u000023\u0005a\u0000\u000034\u0005u\u0000\u0000"+
		"45\u0005l\u0000\u000056\u0005t\u0000\u00006\u0006\u0001\u0000\u0000\u0000"+
		"78\u0005(\u0000\u00008\b\u0001\u0000\u0000\u00009:\u0005)\u0000\u0000"+
		":\n\u0001\u0000\u0000\u0000;<\u0005{\u0000\u0000<\f\u0001\u0000\u0000"+
		"\u0000=>\u0005}\u0000\u0000>\u000e\u0001\u0000\u0000\u0000?@\u0005=\u0000"+
		"\u0000@\u0010\u0001\u0000\u0000\u0000AB\u0005+\u0000\u0000B\u0012\u0001"+
		"\u0000\u0000\u0000CD\u0005-\u0000\u0000D\u0014\u0001\u0000\u0000\u0000"+
		"EF\u0005*\u0000\u0000F\u0016\u0001\u0000\u0000\u0000GH\u0005/\u0000\u0000"+
		"H\u0018\u0001\u0000\u0000\u0000IJ\u0005>\u0000\u0000J\u001a\u0001\u0000"+
		"\u0000\u0000KL\u0005<\u0000\u0000L\u001c\u0001\u0000\u0000\u0000MN\u0005"+
		"=\u0000\u0000NO\u0005=\u0000\u0000O\u001e\u0001\u0000\u0000\u0000PQ\u0005"+
		"!\u0000\u0000QR\u0005=\u0000\u0000R \u0001\u0000\u0000\u0000ST\u0005;"+
		"\u0000\u0000T\"\u0001\u0000\u0000\u0000UY\u0007\u0000\u0000\u0000VX\u0007"+
		"\u0001\u0000\u0000WV\u0001\u0000\u0000\u0000X[\u0001\u0000\u0000\u0000"+
		"YW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z$\u0001\u0000\u0000"+
		"\u0000[Y\u0001\u0000\u0000\u0000\\^\u0007\u0002\u0000\u0000]\\\u0001\u0000"+
		"\u0000\u0000^_\u0001\u0000\u0000\u0000_]\u0001\u0000\u0000\u0000_`\u0001"+
		"\u0000\u0000\u0000`&\u0001\u0000\u0000\u0000ac\u0007\u0003\u0000\u0000"+
		"ba\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000db\u0001\u0000\u0000"+
		"\u0000de\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000fg\u0006\u0013"+
		"\u0000\u0000g(\u0001\u0000\u0000\u0000\u0004\u0000Y_d\u0001\u0006\u0000"+
		"\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}