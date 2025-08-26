// Generated from /workspaces/compiladores/actividad1/Calculadora.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CalculadoraParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		ID=10, NUMBER=11, WS=12;
	public static final int
		RULE_prog = 0, RULE_asignacion = 1, RULE_expresion = 2;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "asignacion", "expresion"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "';'", "'-'", "'^'", "'*'", "'/'", "'+'", "'('", "')'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "ID", "NUMBER", 
			"WS"
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

	@Override
	public String getGrammarFileName() { return "Calculadora.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CalculadoraParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CalculadoraParser.EOF, 0); }
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(8);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				{
				setState(6);
				asignacion();
				}
				break;
			case 2:
				{
				setState(7);
				expresion(0);
				}
				break;
			}
			setState(10);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AsignacionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CalculadoraParser.ID, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_asignacion);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(12);
			match(ID);
			setState(13);
			match(T__0);
			setState(14);
			expresion(0);
			setState(15);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpresionContext extends ParserRuleContext {
		public ExpresionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expresion; }
	 
		public ExpresionContext() { }
		public void copyFrom(ExpresionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NumeroContext extends ExpresionContext {
		public TerminalNode NUMBER() { return getToken(CalculadoraParser.NUMBER, 0); }
		public NumeroContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class FuncionContext extends ExpresionContext {
		public TerminalNode ID() { return getToken(CalculadoraParser.ID, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public FuncionContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class VariableContext extends ExpresionContext {
		public TerminalNode ID() { return getToken(CalculadoraParser.ID, 0); }
		public VariableContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddSubContext extends ExpresionContext {
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public AddSubContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParentesisContext extends ExpresionContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public ParentesisContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class PotenciaContext extends ExpresionContext {
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public PotenciaContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class NegativoContext extends ExpresionContext {
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public NegativoContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MultDivContext extends ExpresionContext {
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public MultDivContext(ExpresionContext ctx) { copyFrom(ctx); }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		return expresion(0);
	}

	private ExpresionContext expresion(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpresionContext _localctx = new ExpresionContext(_ctx, _parentState);
		ExpresionContext _prevctx = _localctx;
		int _startState = 4;
		enterRecursionRule(_localctx, 4, RULE_expresion, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				{
				_localctx = new NegativoContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(18);
				match(T__2);
				setState(19);
				expresion(8);
				}
				break;
			case 2:
				{
				_localctx = new FuncionContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(20);
				match(ID);
				setState(21);
				match(T__7);
				setState(22);
				expresion(0);
				setState(23);
				match(T__8);
				}
				break;
			case 3:
				{
				_localctx = new ParentesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(25);
				match(T__7);
				setState(26);
				expresion(0);
				setState(27);
				match(T__8);
				}
				break;
			case 4:
				{
				_localctx = new NumeroContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(29);
				match(NUMBER);
				}
				break;
			case 5:
				{
				_localctx = new VariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(30);
				match(ID);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(44);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(42);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
					case 1:
						{
						_localctx = new PotenciaContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(33);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(34);
						match(T__3);
						setState(35);
						expresion(8);
						}
						break;
					case 2:
						{
						_localctx = new MultDivContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(36);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(37);
						_la = _input.LA(1);
						if ( !(_la==T__4 || _la==T__5) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(38);
						expresion(7);
						}
						break;
					case 3:
						{
						_localctx = new AddSubContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(39);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(40);
						_la = _input.LA(1);
						if ( !(_la==T__2 || _la==T__6) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(41);
						expresion(6);
						}
						break;
					}
					} 
				}
				setState(46);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,3,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 2:
			return expresion_sempred((ExpresionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expresion_sempred(ExpresionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 7);
		case 1:
			return precpred(_ctx, 6);
		case 2:
			return precpred(_ctx, 5);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\f0\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0001\u0000\u0001\u0000\u0003\u0000\t\b\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u0002 \b\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0005\u0002+\b\u0002\n\u0002\f\u0002.\t\u0002\u0001"+
		"\u0002\u0000\u0001\u0004\u0003\u0000\u0002\u0004\u0000\u0002\u0001\u0000"+
		"\u0005\u0006\u0002\u0000\u0003\u0003\u0007\u00074\u0000\b\u0001\u0000"+
		"\u0000\u0000\u0002\f\u0001\u0000\u0000\u0000\u0004\u001f\u0001\u0000\u0000"+
		"\u0000\u0006\t\u0003\u0002\u0001\u0000\u0007\t\u0003\u0004\u0002\u0000"+
		"\b\u0006\u0001\u0000\u0000\u0000\b\u0007\u0001\u0000\u0000\u0000\t\n\u0001"+
		"\u0000\u0000\u0000\n\u000b\u0005\u0000\u0000\u0001\u000b\u0001\u0001\u0000"+
		"\u0000\u0000\f\r\u0005\n\u0000\u0000\r\u000e\u0005\u0001\u0000\u0000\u000e"+
		"\u000f\u0003\u0004\u0002\u0000\u000f\u0010\u0005\u0002\u0000\u0000\u0010"+
		"\u0003\u0001\u0000\u0000\u0000\u0011\u0012\u0006\u0002\uffff\uffff\u0000"+
		"\u0012\u0013\u0005\u0003\u0000\u0000\u0013 \u0003\u0004\u0002\b\u0014"+
		"\u0015\u0005\n\u0000\u0000\u0015\u0016\u0005\b\u0000\u0000\u0016\u0017"+
		"\u0003\u0004\u0002\u0000\u0017\u0018\u0005\t\u0000\u0000\u0018 \u0001"+
		"\u0000\u0000\u0000\u0019\u001a\u0005\b\u0000\u0000\u001a\u001b\u0003\u0004"+
		"\u0002\u0000\u001b\u001c\u0005\t\u0000\u0000\u001c \u0001\u0000\u0000"+
		"\u0000\u001d \u0005\u000b\u0000\u0000\u001e \u0005\n\u0000\u0000\u001f"+
		"\u0011\u0001\u0000\u0000\u0000\u001f\u0014\u0001\u0000\u0000\u0000\u001f"+
		"\u0019\u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000\u001f"+
		"\u001e\u0001\u0000\u0000\u0000 ,\u0001\u0000\u0000\u0000!\"\n\u0007\u0000"+
		"\u0000\"#\u0005\u0004\u0000\u0000#+\u0003\u0004\u0002\b$%\n\u0006\u0000"+
		"\u0000%&\u0007\u0000\u0000\u0000&+\u0003\u0004\u0002\u0007\'(\n\u0005"+
		"\u0000\u0000()\u0007\u0001\u0000\u0000)+\u0003\u0004\u0002\u0006*!\u0001"+
		"\u0000\u0000\u0000*$\u0001\u0000\u0000\u0000*\'\u0001\u0000\u0000\u0000"+
		"+.\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000,-\u0001\u0000\u0000"+
		"\u0000-\u0005\u0001\u0000\u0000\u0000.,\u0001\u0000\u0000\u0000\u0004"+
		"\b\u001f*,";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}