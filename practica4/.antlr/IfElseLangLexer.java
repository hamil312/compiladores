// Generated from /workspaces/compiladores/practica4/IfElseLang.g4 by ANTLR 4.13.1
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
		T__0=1, T__1=2, T__2=3, T__3=4, IF=5, ELSE=6, LPAREN=7, RPAREN=8, LBRACE=9, 
		RBRACE=10, SEMI=11, ASSIGN=12, LT=13, GT=14, GE=15, LE=16, EQ=17, NE=18, 
		PLUS=19, MINUS=20, MUL=21, DIV=22, ID=23, NUMBER=24, STRING=25, COMMENT=26, 
		WS=27;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "IF", "ELSE", "LPAREN", "RPAREN", "LBRACE", 
			"RBRACE", "SEMI", "ASSIGN", "LT", "GT", "GE", "LE", "EQ", "NE", "PLUS", 
			"MINUS", "MUL", "DIV", "ID", "NUMBER", "STRING", "COMMENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "','", "'int'", "'string'", "'return'", "'if'", "'else'", "'('", 
			"')'", "'{'", "'}'", "';'", "'='", "'<'", "'>'", "'>='", "'<='", "'=='", 
			"'!='", "'+'", "'-'", "'*'", "'/'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, "IF", "ELSE", "LPAREN", "RPAREN", "LBRACE", 
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
		"\u0004\u0000\u001b\u00a0\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017"+
		"\u0002\u0018\u0007\u0018\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a"+
		"\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e"+
		"\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0001\u0015\u0001\u0016\u0001\u0016\u0005\u0016z\b\u0016\n\u0016\f\u0016"+
		"}\t\u0016\u0001\u0017\u0004\u0017\u0080\b\u0017\u000b\u0017\f\u0017\u0081"+
		"\u0001\u0018\u0001\u0018\u0005\u0018\u0086\b\u0018\n\u0018\f\u0018\u0089"+
		"\t\u0018\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001"+
		"\u0019\u0005\u0019\u0091\b\u0019\n\u0019\f\u0019\u0094\t\u0019\u0001\u0019"+
		"\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0004\u001a\u009b\b\u001a"+
		"\u000b\u001a\f\u001a\u009c\u0001\u001a\u0001\u001a\u0001\u0092\u0000\u001b"+
		"\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r"+
		"\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016-\u0017"+
		"/\u00181\u00193\u001a5\u001b\u0001\u0000\u0005\u0003\u0000AZ__az\u0004"+
		"\u000009AZ__az\u0001\u000009\u0003\u0000\n\n\r\r\"\"\u0003\u0000\t\n\r"+
		"\r  \u00a4\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
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
		"3\u0001\u0000\u0000\u0000\u00005\u0001\u0000\u0000\u0000\u00017\u0001"+
		"\u0000\u0000\u0000\u00039\u0001\u0000\u0000\u0000\u0005=\u0001\u0000\u0000"+
		"\u0000\u0007D\u0001\u0000\u0000\u0000\tK\u0001\u0000\u0000\u0000\u000b"+
		"N\u0001\u0000\u0000\u0000\rS\u0001\u0000\u0000\u0000\u000fU\u0001\u0000"+
		"\u0000\u0000\u0011W\u0001\u0000\u0000\u0000\u0013Y\u0001\u0000\u0000\u0000"+
		"\u0015[\u0001\u0000\u0000\u0000\u0017]\u0001\u0000\u0000\u0000\u0019_"+
		"\u0001\u0000\u0000\u0000\u001ba\u0001\u0000\u0000\u0000\u001dc\u0001\u0000"+
		"\u0000\u0000\u001ff\u0001\u0000\u0000\u0000!i\u0001\u0000\u0000\u0000"+
		"#l\u0001\u0000\u0000\u0000%o\u0001\u0000\u0000\u0000\'q\u0001\u0000\u0000"+
		"\u0000)s\u0001\u0000\u0000\u0000+u\u0001\u0000\u0000\u0000-w\u0001\u0000"+
		"\u0000\u0000/\u007f\u0001\u0000\u0000\u00001\u0083\u0001\u0000\u0000\u0000"+
		"3\u008c\u0001\u0000\u0000\u00005\u009a\u0001\u0000\u0000\u000078\u0005"+
		",\u0000\u00008\u0002\u0001\u0000\u0000\u00009:\u0005i\u0000\u0000:;\u0005"+
		"n\u0000\u0000;<\u0005t\u0000\u0000<\u0004\u0001\u0000\u0000\u0000=>\u0005"+
		"s\u0000\u0000>?\u0005t\u0000\u0000?@\u0005r\u0000\u0000@A\u0005i\u0000"+
		"\u0000AB\u0005n\u0000\u0000BC\u0005g\u0000\u0000C\u0006\u0001\u0000\u0000"+
		"\u0000DE\u0005r\u0000\u0000EF\u0005e\u0000\u0000FG\u0005t\u0000\u0000"+
		"GH\u0005u\u0000\u0000HI\u0005r\u0000\u0000IJ\u0005n\u0000\u0000J\b\u0001"+
		"\u0000\u0000\u0000KL\u0005i\u0000\u0000LM\u0005f\u0000\u0000M\n\u0001"+
		"\u0000\u0000\u0000NO\u0005e\u0000\u0000OP\u0005l\u0000\u0000PQ\u0005s"+
		"\u0000\u0000QR\u0005e\u0000\u0000R\f\u0001\u0000\u0000\u0000ST\u0005("+
		"\u0000\u0000T\u000e\u0001\u0000\u0000\u0000UV\u0005)\u0000\u0000V\u0010"+
		"\u0001\u0000\u0000\u0000WX\u0005{\u0000\u0000X\u0012\u0001\u0000\u0000"+
		"\u0000YZ\u0005}\u0000\u0000Z\u0014\u0001\u0000\u0000\u0000[\\\u0005;\u0000"+
		"\u0000\\\u0016\u0001\u0000\u0000\u0000]^\u0005=\u0000\u0000^\u0018\u0001"+
		"\u0000\u0000\u0000_`\u0005<\u0000\u0000`\u001a\u0001\u0000\u0000\u0000"+
		"ab\u0005>\u0000\u0000b\u001c\u0001\u0000\u0000\u0000cd\u0005>\u0000\u0000"+
		"de\u0005=\u0000\u0000e\u001e\u0001\u0000\u0000\u0000fg\u0005<\u0000\u0000"+
		"gh\u0005=\u0000\u0000h \u0001\u0000\u0000\u0000ij\u0005=\u0000\u0000j"+
		"k\u0005=\u0000\u0000k\"\u0001\u0000\u0000\u0000lm\u0005!\u0000\u0000m"+
		"n\u0005=\u0000\u0000n$\u0001\u0000\u0000\u0000op\u0005+\u0000\u0000p&"+
		"\u0001\u0000\u0000\u0000qr\u0005-\u0000\u0000r(\u0001\u0000\u0000\u0000"+
		"st\u0005*\u0000\u0000t*\u0001\u0000\u0000\u0000uv\u0005/\u0000\u0000v"+
		",\u0001\u0000\u0000\u0000w{\u0007\u0000\u0000\u0000xz\u0007\u0001\u0000"+
		"\u0000yx\u0001\u0000\u0000\u0000z}\u0001\u0000\u0000\u0000{y\u0001\u0000"+
		"\u0000\u0000{|\u0001\u0000\u0000\u0000|.\u0001\u0000\u0000\u0000}{\u0001"+
		"\u0000\u0000\u0000~\u0080\u0007\u0002\u0000\u0000\u007f~\u0001\u0000\u0000"+
		"\u0000\u0080\u0081\u0001\u0000\u0000\u0000\u0081\u007f\u0001\u0000\u0000"+
		"\u0000\u0081\u0082\u0001\u0000\u0000\u0000\u00820\u0001\u0000\u0000\u0000"+
		"\u0083\u0087\u0005\"\u0000\u0000\u0084\u0086\b\u0003\u0000\u0000\u0085"+
		"\u0084\u0001\u0000\u0000\u0000\u0086\u0089\u0001\u0000\u0000\u0000\u0087"+
		"\u0085\u0001\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088"+
		"\u008a\u0001\u0000\u0000\u0000\u0089\u0087\u0001\u0000\u0000\u0000\u008a"+
		"\u008b\u0005\"\u0000\u0000\u008b2\u0001\u0000\u0000\u0000\u008c\u008d"+
		"\u0005/\u0000\u0000\u008d\u008e\u0005/\u0000\u0000\u008e\u0092\u0001\u0000"+
		"\u0000\u0000\u008f\u0091\t\u0000\u0000\u0000\u0090\u008f\u0001\u0000\u0000"+
		"\u0000\u0091\u0094\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000"+
		"\u0000\u0092\u0090\u0001\u0000\u0000\u0000\u0093\u0095\u0001\u0000\u0000"+
		"\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0095\u0096\u0005\n\u0000\u0000"+
		"\u0096\u0097\u0001\u0000\u0000\u0000\u0097\u0098\u0006\u0019\u0000\u0000"+
		"\u00984\u0001\u0000\u0000\u0000\u0099\u009b\u0007\u0004\u0000\u0000\u009a"+
		"\u0099\u0001\u0000\u0000\u0000\u009b\u009c\u0001\u0000\u0000\u0000\u009c"+
		"\u009a\u0001\u0000\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d"+
		"\u009e\u0001\u0000\u0000\u0000\u009e\u009f\u0006\u001a\u0000\u0000\u009f"+
		"6\u0001\u0000\u0000\u0000\u0006\u0000{\u0081\u0087\u0092\u009c\u0001\u0006"+
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