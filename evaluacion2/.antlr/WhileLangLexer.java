// Generated from /workspaces/compiladores/evaluacion2/WhileLang.g4 by ANTLR 4.13.1
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
		OP=1, WHILE=2, IF=3, ELSE=4, BREAK=5, CONTINUE=6, LPAREN=7, RPAREN=8, 
		LBRACE=9, RBRACE=10, SEMI=11, ASSIGN=12, GT=13, LT=14, EQ=15, NE=16, PLUS=17, 
		MINUS=18, MULT=19, DIV=20, ID=21, NUMBER=22, WS=23;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"OP", "WHILE", "IF", "ELSE", "BREAK", "CONTINUE", "LPAREN", "RPAREN", 
			"LBRACE", "RBRACE", "SEMI", "ASSIGN", "GT", "LT", "EQ", "NE", "PLUS", 
			"MINUS", "MULT", "DIV", "ID", "NUMBER", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'while'", "'if'", "'else'", "'break'", "'continue'", "'('", 
			"')'", "'{'", "'}'", "';'", "'='", "'>'", "'<'", "'=='", "'!='", "'+'", 
			"'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "OP", "WHILE", "IF", "ELSE", "BREAK", "CONTINUE", "LPAREN", "RPAREN", 
			"LBRACE", "RBRACE", "SEMI", "ASSIGN", "GT", "LT", "EQ", "NE", "PLUS", 
			"MINUS", "MULT", "DIV", "ID", "NUMBER", "WS"
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
		"\u0004\u0000\u0017\u0083\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0003\u00004\b\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001"+
		"\u0014\u0001\u0014\u0005\u0014s\b\u0014\n\u0014\f\u0014v\t\u0014\u0001"+
		"\u0015\u0004\u0015y\b\u0015\u000b\u0015\f\u0015z\u0001\u0016\u0004\u0016"+
		"~\b\u0016\u000b\u0016\f\u0016\u007f\u0001\u0016\u0001\u0016\u0000\u0000"+
		"\u0017\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006"+
		"\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017"+
		"\u0001\u0000\u0004\u0003\u0000AZ__az\u0004\u000009AZ__az\u0001\u00000"+
		"9\u0003\u0000\t\n\r\r  \u0088\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001"+
		"\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001"+
		"\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001"+
		"\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000"+
		"\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000"+
		"\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-"+
		"\u0001\u0000\u0000\u0000\u00013\u0001\u0000\u0000\u0000\u00035\u0001\u0000"+
		"\u0000\u0000\u0005;\u0001\u0000\u0000\u0000\u0007>\u0001\u0000\u0000\u0000"+
		"\tC\u0001\u0000\u0000\u0000\u000bI\u0001\u0000\u0000\u0000\rR\u0001\u0000"+
		"\u0000\u0000\u000fT\u0001\u0000\u0000\u0000\u0011V\u0001\u0000\u0000\u0000"+
		"\u0013X\u0001\u0000\u0000\u0000\u0015Z\u0001\u0000\u0000\u0000\u0017\\"+
		"\u0001\u0000\u0000\u0000\u0019^\u0001\u0000\u0000\u0000\u001b`\u0001\u0000"+
		"\u0000\u0000\u001db\u0001\u0000\u0000\u0000\u001fe\u0001\u0000\u0000\u0000"+
		"!h\u0001\u0000\u0000\u0000#j\u0001\u0000\u0000\u0000%l\u0001\u0000\u0000"+
		"\u0000\'n\u0001\u0000\u0000\u0000)p\u0001\u0000\u0000\u0000+x\u0001\u0000"+
		"\u0000\u0000-}\u0001\u0000\u0000\u0000/4\u0003#\u0011\u000004\u0003!\u0010"+
		"\u000014\u0003%\u0012\u000024\u0003\'\u0013\u00003/\u0001\u0000\u0000"+
		"\u000030\u0001\u0000\u0000\u000031\u0001\u0000\u0000\u000032\u0001\u0000"+
		"\u0000\u00004\u0002\u0001\u0000\u0000\u000056\u0005w\u0000\u000067\u0005"+
		"h\u0000\u000078\u0005i\u0000\u000089\u0005l\u0000\u00009:\u0005e\u0000"+
		"\u0000:\u0004\u0001\u0000\u0000\u0000;<\u0005i\u0000\u0000<=\u0005f\u0000"+
		"\u0000=\u0006\u0001\u0000\u0000\u0000>?\u0005e\u0000\u0000?@\u0005l\u0000"+
		"\u0000@A\u0005s\u0000\u0000AB\u0005e\u0000\u0000B\b\u0001\u0000\u0000"+
		"\u0000CD\u0005b\u0000\u0000DE\u0005r\u0000\u0000EF\u0005e\u0000\u0000"+
		"FG\u0005a\u0000\u0000GH\u0005k\u0000\u0000H\n\u0001\u0000\u0000\u0000"+
		"IJ\u0005c\u0000\u0000JK\u0005o\u0000\u0000KL\u0005n\u0000\u0000LM\u0005"+
		"t\u0000\u0000MN\u0005i\u0000\u0000NO\u0005n\u0000\u0000OP\u0005u\u0000"+
		"\u0000PQ\u0005e\u0000\u0000Q\f\u0001\u0000\u0000\u0000RS\u0005(\u0000"+
		"\u0000S\u000e\u0001\u0000\u0000\u0000TU\u0005)\u0000\u0000U\u0010\u0001"+
		"\u0000\u0000\u0000VW\u0005{\u0000\u0000W\u0012\u0001\u0000\u0000\u0000"+
		"XY\u0005}\u0000\u0000Y\u0014\u0001\u0000\u0000\u0000Z[\u0005;\u0000\u0000"+
		"[\u0016\u0001\u0000\u0000\u0000\\]\u0005=\u0000\u0000]\u0018\u0001\u0000"+
		"\u0000\u0000^_\u0005>\u0000\u0000_\u001a\u0001\u0000\u0000\u0000`a\u0005"+
		"<\u0000\u0000a\u001c\u0001\u0000\u0000\u0000bc\u0005=\u0000\u0000cd\u0005"+
		"=\u0000\u0000d\u001e\u0001\u0000\u0000\u0000ef\u0005!\u0000\u0000fg\u0005"+
		"=\u0000\u0000g \u0001\u0000\u0000\u0000hi\u0005+\u0000\u0000i\"\u0001"+
		"\u0000\u0000\u0000jk\u0005-\u0000\u0000k$\u0001\u0000\u0000\u0000lm\u0005"+
		"*\u0000\u0000m&\u0001\u0000\u0000\u0000no\u0005/\u0000\u0000o(\u0001\u0000"+
		"\u0000\u0000pt\u0007\u0000\u0000\u0000qs\u0007\u0001\u0000\u0000rq\u0001"+
		"\u0000\u0000\u0000sv\u0001\u0000\u0000\u0000tr\u0001\u0000\u0000\u0000"+
		"tu\u0001\u0000\u0000\u0000u*\u0001\u0000\u0000\u0000vt\u0001\u0000\u0000"+
		"\u0000wy\u0007\u0002\u0000\u0000xw\u0001\u0000\u0000\u0000yz\u0001\u0000"+
		"\u0000\u0000zx\u0001\u0000\u0000\u0000z{\u0001\u0000\u0000\u0000{,\u0001"+
		"\u0000\u0000\u0000|~\u0007\u0003\u0000\u0000}|\u0001\u0000\u0000\u0000"+
		"~\u007f\u0001\u0000\u0000\u0000\u007f}\u0001\u0000\u0000\u0000\u007f\u0080"+
		"\u0001\u0000\u0000\u0000\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u0082"+
		"\u0006\u0016\u0000\u0000\u0082.\u0001\u0000\u0000\u0000\u0005\u00003t"+
		"z\u007f\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}