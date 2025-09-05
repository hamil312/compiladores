// Generated from /workspaces/compiladores/practica2.1/MiGramatica.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class MiGramaticaLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SELECT=1, FROM=2, WHERE=3, STAR=4, COMMA=5, SEMI=6, GT=7, LT=8, EQ=9, 
		GE=10, LE=11, NE=12, IDENTIFIER=13, NUMBER=14, STRING=15, WS=16;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"SELECT", "FROM", "WHERE", "STAR", "COMMA", "SEMI", "GT", "LT", "EQ", 
			"GE", "LE", "NE", "IDENTIFIER", "NUMBER", "STRING", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'SELECT'", "'FROM'", "'WHERE'", "'*'", "','", "';'", "'>'", "'<'", 
			"'='", "'>='", "'<='", "'!='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "SELECT", "FROM", "WHERE", "STAR", "COMMA", "SEMI", "GT", "LT", 
			"EQ", "GE", "LE", "NE", "IDENTIFIER", "NUMBER", "STRING", "WS"
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


	public MiGramaticaLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "MiGramatica.g4"; }

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
		"\u0004\u0000\u0010l\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0005\fK\b\f\n\f\f\fN\t\f\u0001"+
		"\r\u0004\rQ\b\r\u000b\r\f\rR\u0001\r\u0001\r\u0004\rW\b\r\u000b\r\f\r"+
		"X\u0003\r[\b\r\u0001\u000e\u0001\u000e\u0005\u000e_\b\u000e\n\u000e\f"+
		"\u000eb\t\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0004\u000fg\b\u000f"+
		"\u000b\u000f\f\u000fh\u0001\u000f\u0001\u000f\u0000\u0000\u0010\u0001"+
		"\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007"+
		"\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d"+
		"\u000f\u001f\u0010\u0001\u0000\u0005\u0003\u0000AZ__az\u0004\u000009A"+
		"Z__az\u0001\u000009\u0003\u0000\n\n\r\r\'\'\u0003\u0000\t\n\r\r  q\u0000"+
		"\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000"+
		"\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000"+
		"\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r"+
		"\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0001!\u0001"+
		"\u0000\u0000\u0000\u0003(\u0001\u0000\u0000\u0000\u0005-\u0001\u0000\u0000"+
		"\u0000\u00073\u0001\u0000\u0000\u0000\t5\u0001\u0000\u0000\u0000\u000b"+
		"7\u0001\u0000\u0000\u0000\r9\u0001\u0000\u0000\u0000\u000f;\u0001\u0000"+
		"\u0000\u0000\u0011=\u0001\u0000\u0000\u0000\u0013?\u0001\u0000\u0000\u0000"+
		"\u0015B\u0001\u0000\u0000\u0000\u0017E\u0001\u0000\u0000\u0000\u0019H"+
		"\u0001\u0000\u0000\u0000\u001bP\u0001\u0000\u0000\u0000\u001d\\\u0001"+
		"\u0000\u0000\u0000\u001ff\u0001\u0000\u0000\u0000!\"\u0005S\u0000\u0000"+
		"\"#\u0005E\u0000\u0000#$\u0005L\u0000\u0000$%\u0005E\u0000\u0000%&\u0005"+
		"C\u0000\u0000&\'\u0005T\u0000\u0000\'\u0002\u0001\u0000\u0000\u0000()"+
		"\u0005F\u0000\u0000)*\u0005R\u0000\u0000*+\u0005O\u0000\u0000+,\u0005"+
		"M\u0000\u0000,\u0004\u0001\u0000\u0000\u0000-.\u0005W\u0000\u0000./\u0005"+
		"H\u0000\u0000/0\u0005E\u0000\u000001\u0005R\u0000\u000012\u0005E\u0000"+
		"\u00002\u0006\u0001\u0000\u0000\u000034\u0005*\u0000\u00004\b\u0001\u0000"+
		"\u0000\u000056\u0005,\u0000\u00006\n\u0001\u0000\u0000\u000078\u0005;"+
		"\u0000\u00008\f\u0001\u0000\u0000\u00009:\u0005>\u0000\u0000:\u000e\u0001"+
		"\u0000\u0000\u0000;<\u0005<\u0000\u0000<\u0010\u0001\u0000\u0000\u0000"+
		"=>\u0005=\u0000\u0000>\u0012\u0001\u0000\u0000\u0000?@\u0005>\u0000\u0000"+
		"@A\u0005=\u0000\u0000A\u0014\u0001\u0000\u0000\u0000BC\u0005<\u0000\u0000"+
		"CD\u0005=\u0000\u0000D\u0016\u0001\u0000\u0000\u0000EF\u0005!\u0000\u0000"+
		"FG\u0005=\u0000\u0000G\u0018\u0001\u0000\u0000\u0000HL\u0007\u0000\u0000"+
		"\u0000IK\u0007\u0001\u0000\u0000JI\u0001\u0000\u0000\u0000KN\u0001\u0000"+
		"\u0000\u0000LJ\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000M\u001a"+
		"\u0001\u0000\u0000\u0000NL\u0001\u0000\u0000\u0000OQ\u0007\u0002\u0000"+
		"\u0000PO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000RP\u0001\u0000"+
		"\u0000\u0000RS\u0001\u0000\u0000\u0000SZ\u0001\u0000\u0000\u0000TV\u0005"+
		".\u0000\u0000UW\u0007\u0002\u0000\u0000VU\u0001\u0000\u0000\u0000WX\u0001"+
		"\u0000\u0000\u0000XV\u0001\u0000\u0000\u0000XY\u0001\u0000\u0000\u0000"+
		"Y[\u0001\u0000\u0000\u0000ZT\u0001\u0000\u0000\u0000Z[\u0001\u0000\u0000"+
		"\u0000[\u001c\u0001\u0000\u0000\u0000\\`\u0005\'\u0000\u0000]_\b\u0003"+
		"\u0000\u0000^]\u0001\u0000\u0000\u0000_b\u0001\u0000\u0000\u0000`^\u0001"+
		"\u0000\u0000\u0000`a\u0001\u0000\u0000\u0000ac\u0001\u0000\u0000\u0000"+
		"b`\u0001\u0000\u0000\u0000cd\u0005\'\u0000\u0000d\u001e\u0001\u0000\u0000"+
		"\u0000eg\u0007\u0004\u0000\u0000fe\u0001\u0000\u0000\u0000gh\u0001\u0000"+
		"\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001\u0000\u0000\u0000ij\u0001"+
		"\u0000\u0000\u0000jk\u0006\u000f\u0000\u0000k \u0001\u0000\u0000\u0000"+
		"\u0007\u0000LRXZ`h\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}