// Generated from /workspaces/compiladores/practica2.2/SwitchLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class SwitchLangLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SWITCH=1, CASE=2, COLON=3, DEFAULT=4, LPAREN=5, RPAREN=6, LBRACE=7, RBRACE=8, 
		ASSIGN=9, PLUS=10, MINUS=11, MUL=12, DIV=13, GT=14, LT=15, EQ=16, NEQ=17, 
		SEMI=18, ID=19, INT=20, WS=21;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SWITCH", "CASE", "COLON", "DEFAULT", "LPAREN", "RPAREN", "LBRACE", "RBRACE", 
			"ASSIGN", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "EQ", "NEQ", "SEMI", 
			"ID", "INT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'switch'", "'case'", "':'", "'default'", "'('", "')'", "'{'", 
			"'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'>'", "'<'", "'=='", "'!='", 
			"';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SWITCH", "CASE", "COLON", "DEFAULT", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", "GT", "LT", "EQ", 
			"NEQ", "SEMI", "ID", "INT", "WS"
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


	public SwitchLangLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "SwitchLang.g4"; }

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
		"\u0004\u0000\u0015r\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001"+
		"\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011"+
		"\u0001\u0012\u0001\u0012\u0005\u0012b\b\u0012\n\u0012\f\u0012e\t\u0012"+
		"\u0001\u0013\u0004\u0013h\b\u0013\u000b\u0013\f\u0013i\u0001\u0014\u0004"+
		"\u0014m\b\u0014\u000b\u0014\f\u0014n\u0001\u0014\u0001\u0014\u0000\u0000"+
		"\u0015\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006"+
		"\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015\u0001\u0000"+
		"\u0004\u0003\u0000AZ__az\u0004\u000009AZ__az\u0001\u000009\u0003\u0000"+
		"\t\n\r\r  t\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0001+\u0001\u0000\u0000\u0000\u00032\u0001\u0000\u0000"+
		"\u0000\u00057\u0001\u0000\u0000\u0000\u00079\u0001\u0000\u0000\u0000\t"+
		"A\u0001\u0000\u0000\u0000\u000bC\u0001\u0000\u0000\u0000\rE\u0001\u0000"+
		"\u0000\u0000\u000fG\u0001\u0000\u0000\u0000\u0011I\u0001\u0000\u0000\u0000"+
		"\u0013K\u0001\u0000\u0000\u0000\u0015M\u0001\u0000\u0000\u0000\u0017O"+
		"\u0001\u0000\u0000\u0000\u0019Q\u0001\u0000\u0000\u0000\u001bS\u0001\u0000"+
		"\u0000\u0000\u001dU\u0001\u0000\u0000\u0000\u001fW\u0001\u0000\u0000\u0000"+
		"!Z\u0001\u0000\u0000\u0000#]\u0001\u0000\u0000\u0000%_\u0001\u0000\u0000"+
		"\u0000\'g\u0001\u0000\u0000\u0000)l\u0001\u0000\u0000\u0000+,\u0005s\u0000"+
		"\u0000,-\u0005w\u0000\u0000-.\u0005i\u0000\u0000./\u0005t\u0000\u0000"+
		"/0\u0005c\u0000\u000001\u0005h\u0000\u00001\u0002\u0001\u0000\u0000\u0000"+
		"23\u0005c\u0000\u000034\u0005a\u0000\u000045\u0005s\u0000\u000056\u0005"+
		"e\u0000\u00006\u0004\u0001\u0000\u0000\u000078\u0005:\u0000\u00008\u0006"+
		"\u0001\u0000\u0000\u00009:\u0005d\u0000\u0000:;\u0005e\u0000\u0000;<\u0005"+
		"f\u0000\u0000<=\u0005a\u0000\u0000=>\u0005u\u0000\u0000>?\u0005l\u0000"+
		"\u0000?@\u0005t\u0000\u0000@\b\u0001\u0000\u0000\u0000AB\u0005(\u0000"+
		"\u0000B\n\u0001\u0000\u0000\u0000CD\u0005)\u0000\u0000D\f\u0001\u0000"+
		"\u0000\u0000EF\u0005{\u0000\u0000F\u000e\u0001\u0000\u0000\u0000GH\u0005"+
		"}\u0000\u0000H\u0010\u0001\u0000\u0000\u0000IJ\u0005=\u0000\u0000J\u0012"+
		"\u0001\u0000\u0000\u0000KL\u0005+\u0000\u0000L\u0014\u0001\u0000\u0000"+
		"\u0000MN\u0005-\u0000\u0000N\u0016\u0001\u0000\u0000\u0000OP\u0005*\u0000"+
		"\u0000P\u0018\u0001\u0000\u0000\u0000QR\u0005/\u0000\u0000R\u001a\u0001"+
		"\u0000\u0000\u0000ST\u0005>\u0000\u0000T\u001c\u0001\u0000\u0000\u0000"+
		"UV\u0005<\u0000\u0000V\u001e\u0001\u0000\u0000\u0000WX\u0005=\u0000\u0000"+
		"XY\u0005=\u0000\u0000Y \u0001\u0000\u0000\u0000Z[\u0005!\u0000\u0000["+
		"\\\u0005=\u0000\u0000\\\"\u0001\u0000\u0000\u0000]^\u0005;\u0000\u0000"+
		"^$\u0001\u0000\u0000\u0000_c\u0007\u0000\u0000\u0000`b\u0007\u0001\u0000"+
		"\u0000a`\u0001\u0000\u0000\u0000be\u0001\u0000\u0000\u0000ca\u0001\u0000"+
		"\u0000\u0000cd\u0001\u0000\u0000\u0000d&\u0001\u0000\u0000\u0000ec\u0001"+
		"\u0000\u0000\u0000fh\u0007\u0002\u0000\u0000gf\u0001\u0000\u0000\u0000"+
		"hi\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000ij\u0001\u0000\u0000"+
		"\u0000j(\u0001\u0000\u0000\u0000km\u0007\u0003\u0000\u0000lk\u0001\u0000"+
		"\u0000\u0000mn\u0001\u0000\u0000\u0000nl\u0001\u0000\u0000\u0000no\u0001"+
		"\u0000\u0000\u0000op\u0001\u0000\u0000\u0000pq\u0006\u0014\u0000\u0000"+
		"q*\u0001\u0000\u0000\u0000\u0004\u0000cin\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}