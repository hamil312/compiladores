// Generated from /workspaces/compiladores/evaluacion1/IfElseLang.g4 by ANTLR 4.13.1
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
		IF=1, ELSE=2, LPAREN=3, RPAREN=4, LBRACE=5, RBRACE=6, SEMI=7, ASSIGN=8, 
		LT=9, GT=10, GE=11, LE=12, NE=13, EQ=14, ID=15, NUMBER=16, WS=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"IF", "ELSE", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "ASSIGN", 
			"LT", "GT", "GE", "LE", "NE", "EQ", "ID", "NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'else'", "'('", "')'", "'{'", "'}'", "';'", "'='", "'<'", 
			"'>'", "'>='", "'<='", "'!='", "'=='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "ELSE", "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMI", "ASSIGN", 
			"LT", "GT", "GE", "LE", "NE", "EQ", "ID", "NUMBER", "WS"
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
		"\u0004\u0000\u0011Z\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0005\u000eJ\b\u000e\n\u000e\f\u000eM\t\u000e\u0001\u000f"+
		"\u0004\u000fP\b\u000f\u000b\u000f\f\u000fQ\u0001\u0010\u0004\u0010U\b"+
		"\u0010\u000b\u0010\f\u0010V\u0001\u0010\u0001\u0010\u0000\u0000\u0011"+
		"\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r"+
		"\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011\u0001\u0000\u0004\u0003\u0000AZ__az\u0004"+
		"\u000009AZ__az\u0001\u000009\u0003\u0000\t\n\r\r  \\\u0000\u0001\u0001"+
		"\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001"+
		"\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000"+
		"\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000"+
		"\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000"+
		"\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000"+
		"\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000"+
		"\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000"+
		"\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000"+
		"\u0001#\u0001\u0000\u0000\u0000\u0003&\u0001\u0000\u0000\u0000\u0005+"+
		"\u0001\u0000\u0000\u0000\u0007-\u0001\u0000\u0000\u0000\t/\u0001\u0000"+
		"\u0000\u0000\u000b1\u0001\u0000\u0000\u0000\r3\u0001\u0000\u0000\u0000"+
		"\u000f5\u0001\u0000\u0000\u0000\u00117\u0001\u0000\u0000\u0000\u00139"+
		"\u0001\u0000\u0000\u0000\u0015;\u0001\u0000\u0000\u0000\u0017>\u0001\u0000"+
		"\u0000\u0000\u0019A\u0001\u0000\u0000\u0000\u001bD\u0001\u0000\u0000\u0000"+
		"\u001dG\u0001\u0000\u0000\u0000\u001fO\u0001\u0000\u0000\u0000!T\u0001"+
		"\u0000\u0000\u0000#$\u0005i\u0000\u0000$%\u0005f\u0000\u0000%\u0002\u0001"+
		"\u0000\u0000\u0000&\'\u0005e\u0000\u0000\'(\u0005l\u0000\u0000()\u0005"+
		"s\u0000\u0000)*\u0005e\u0000\u0000*\u0004\u0001\u0000\u0000\u0000+,\u0005"+
		"(\u0000\u0000,\u0006\u0001\u0000\u0000\u0000-.\u0005)\u0000\u0000.\b\u0001"+
		"\u0000\u0000\u0000/0\u0005{\u0000\u00000\n\u0001\u0000\u0000\u000012\u0005"+
		"}\u0000\u00002\f\u0001\u0000\u0000\u000034\u0005;\u0000\u00004\u000e\u0001"+
		"\u0000\u0000\u000056\u0005=\u0000\u00006\u0010\u0001\u0000\u0000\u0000"+
		"78\u0005<\u0000\u00008\u0012\u0001\u0000\u0000\u00009:\u0005>\u0000\u0000"+
		":\u0014\u0001\u0000\u0000\u0000;<\u0005>\u0000\u0000<=\u0005=\u0000\u0000"+
		"=\u0016\u0001\u0000\u0000\u0000>?\u0005<\u0000\u0000?@\u0005=\u0000\u0000"+
		"@\u0018\u0001\u0000\u0000\u0000AB\u0005!\u0000\u0000BC\u0005=\u0000\u0000"+
		"C\u001a\u0001\u0000\u0000\u0000DE\u0005=\u0000\u0000EF\u0005=\u0000\u0000"+
		"F\u001c\u0001\u0000\u0000\u0000GK\u0007\u0000\u0000\u0000HJ\u0007\u0001"+
		"\u0000\u0000IH\u0001\u0000\u0000\u0000JM\u0001\u0000\u0000\u0000KI\u0001"+
		"\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000L\u001e\u0001\u0000\u0000"+
		"\u0000MK\u0001\u0000\u0000\u0000NP\u0007\u0002\u0000\u0000ON\u0001\u0000"+
		"\u0000\u0000PQ\u0001\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001"+
		"\u0000\u0000\u0000R \u0001\u0000\u0000\u0000SU\u0007\u0003\u0000\u0000"+
		"TS\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000VT\u0001\u0000\u0000"+
		"\u0000VW\u0001\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000XY\u0006\u0010"+
		"\u0000\u0000Y\"\u0001\u0000\u0000\u0000\u0004\u0000KQV\u0001\u0006\u0000"+
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