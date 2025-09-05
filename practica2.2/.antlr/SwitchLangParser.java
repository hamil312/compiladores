// Generated from /workspaces/compiladores/practica2.2/SwitchLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class SwitchLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		SWITCH=1, CASE=2, COLON=3, DEFAULT=4, LPAREN=5, RPAREN=6, LBRACE=7, RBRACE=8, 
		ASSIGN=9, PLUS=10, MINUS=11, MUL=12, DIV=13, GT=14, LT=15, EQ=16, NEQ=17, 
		SEMI=18, ID=19, INT=20, WS=21;
	public static final int
		RULE_programa = 0, RULE_sentencia = 1, RULE_switchStmt = 2, RULE_condicion = 3, 
		RULE_asignacion = 4, RULE_expresion = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "sentencia", "switchStmt", "condicion", "asignacion", "expresion"
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

	@Override
	public String getGrammarFileName() { return "SwitchLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public SwitchLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(SwitchLangParser.EOF, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(SwitchLangParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(SwitchLangParser.SEMI, i);
		}
		public ProgramaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_programa; }
	}

	public final ProgramaContext programa() throws RecognitionException {
		ProgramaContext _localctx = new ProgramaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_programa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(15); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(12);
				sentencia();
				setState(13);
				match(SEMI);
				}
				}
				setState(17); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==SWITCH || _la==ID );
			setState(19);
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
	public static class SentenciaContext extends ParserRuleContext {
		public SwitchStmtContext switchStmt() {
			return getRuleContext(SwitchStmtContext.class,0);
		}
		public AsignacionContext asignacion() {
			return getRuleContext(AsignacionContext.class,0);
		}
		public SentenciaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sentencia; }
	}

	public final SentenciaContext sentencia() throws RecognitionException {
		SentenciaContext _localctx = new SentenciaContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_sentencia);
		try {
			setState(23);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SWITCH:
				enterOuterAlt(_localctx, 1);
				{
				setState(21);
				switchStmt();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(22);
				asignacion();
				}
				break;
			default:
				throw new NoViableAltException(this);
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
	public static class SwitchStmtContext extends ParserRuleContext {
		public SwitchStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStmt; }
	 
		public SwitchStmtContext() { }
		public void copyFrom(SwitchStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfElseContext extends SwitchStmtContext {
		public TerminalNode SWITCH() { return getToken(SwitchLangParser.SWITCH, 0); }
		public TerminalNode LPAREN() { return getToken(SwitchLangParser.LPAREN, 0); }
		public TerminalNode ID() { return getToken(SwitchLangParser.ID, 0); }
		public TerminalNode RPAREN() { return getToken(SwitchLangParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(SwitchLangParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(SwitchLangParser.RBRACE, 0); }
		public List<TerminalNode> CASE() { return getTokens(SwitchLangParser.CASE); }
		public TerminalNode CASE(int i) {
			return getToken(SwitchLangParser.CASE, i);
		}
		public List<TerminalNode> INT() { return getTokens(SwitchLangParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(SwitchLangParser.INT, i);
		}
		public List<TerminalNode> COLON() { return getTokens(SwitchLangParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(SwitchLangParser.COLON, i);
		}
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(SwitchLangParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(SwitchLangParser.SEMI, i);
		}
		public TerminalNode DEFAULT() { return getToken(SwitchLangParser.DEFAULT, 0); }
		public IfElseContext(SwitchStmtContext ctx) { copyFrom(ctx); }
	}

	public final SwitchStmtContext switchStmt() throws RecognitionException {
		SwitchStmtContext _localctx = new SwitchStmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_switchStmt);
		int _la;
		try {
			int _alt;
			_localctx = new IfElseContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(25);
			match(SWITCH);
			setState(26);
			match(LPAREN);
			setState(27);
			match(ID);
			setState(28);
			match(RPAREN);
			setState(29);
			match(LBRACE);
			setState(36); 
			_errHandler.sync(this);
			_alt = 1+1;
			do {
				switch (_alt) {
				case 1+1:
					{
					{
					setState(30);
					match(CASE);
					setState(31);
					match(INT);
					setState(32);
					match(COLON);
					setState(33);
					sentencia();
					setState(34);
					match(SEMI);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(38); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,2,_ctx);
			} while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(45);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DEFAULT) {
				{
				setState(40);
				match(DEFAULT);
				setState(41);
				match(COLON);
				setState(42);
				sentencia();
				setState(43);
				match(SEMI);
				}
			}

			setState(47);
			match(RBRACE);
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
	public static class CondicionContext extends ParserRuleContext {
		public CondicionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicion; }
	 
		public CondicionContext() { }
		public void copyFrom(CondicionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class CondicionSimpleContext extends CondicionContext {
		public Token op;
		public TerminalNode ID() { return getToken(SwitchLangParser.ID, 0); }
		public TerminalNode INT() { return getToken(SwitchLangParser.INT, 0); }
		public TerminalNode GT() { return getToken(SwitchLangParser.GT, 0); }
		public TerminalNode LT() { return getToken(SwitchLangParser.LT, 0); }
		public TerminalNode EQ() { return getToken(SwitchLangParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(SwitchLangParser.NEQ, 0); }
		public CondicionSimpleContext(CondicionContext ctx) { copyFrom(ctx); }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_condicion);
		int _la;
		try {
			_localctx = new CondicionSimpleContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(49);
			match(ID);
			setState(50);
			((CondicionSimpleContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 245760L) != 0)) ) {
				((CondicionSimpleContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(51);
			match(INT);
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
		public AsignacionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_asignacion; }
	 
		public AsignacionContext() { }
		public void copyFrom(AsignacionContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AssignContext extends AsignacionContext {
		public TerminalNode ID() { return getToken(SwitchLangParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(SwitchLangParser.ASSIGN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public AssignContext(AsignacionContext ctx) { copyFrom(ctx); }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_asignacion);
		try {
			_localctx = new AssignContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(ID);
			setState(54);
			match(ASSIGN);
			setState(55);
			expresion(0);
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
	public static class VariableContext extends ExpresionContext {
		public TerminalNode ID() { return getToken(SwitchLangParser.ID, 0); }
		public VariableContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class MulDivContext extends ExpresionContext {
		public Token op;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode MUL() { return getToken(SwitchLangParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(SwitchLangParser.DIV, 0); }
		public MulDivContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class AddSubContext extends ExpresionContext {
		public Token op;
		public List<ExpresionContext> expresion() {
			return getRuleContexts(ExpresionContext.class);
		}
		public ExpresionContext expresion(int i) {
			return getRuleContext(ExpresionContext.class,i);
		}
		public TerminalNode PLUS() { return getToken(SwitchLangParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(SwitchLangParser.MINUS, 0); }
		public AddSubContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParensContext extends ExpresionContext {
		public TerminalNode LPAREN() { return getToken(SwitchLangParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(SwitchLangParser.RPAREN, 0); }
		public ParensContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntContext extends ExpresionContext {
		public TerminalNode INT() { return getToken(SwitchLangParser.INT, 0); }
		public IntContext(ExpresionContext ctx) { copyFrom(ctx); }
	}

	public final ExpresionContext expresion() throws RecognitionException {
		return expresion(0);
	}

	private ExpresionContext expresion(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpresionContext _localctx = new ExpresionContext(_ctx, _parentState);
		ExpresionContext _prevctx = _localctx;
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_expresion, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(58);
				match(INT);
				}
				break;
			case ID:
				{
				_localctx = new VariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(59);
				match(ID);
				}
				break;
			case LPAREN:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(60);
				match(LPAREN);
				setState(61);
				expresion(0);
				setState(62);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(74);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(72);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(66);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(67);
						((MulDivContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MUL || _la==DIV) ) {
							((MulDivContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(68);
						expresion(6);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(69);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(70);
						((AddSubContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((AddSubContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(71);
						expresion(5);
						}
						break;
					}
					} 
				}
				setState(76);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,6,_ctx);
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
		case 5:
			return expresion_sempred((ExpresionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expresion_sempred(ExpresionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 5);
		case 1:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0015N\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0001\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u0010"+
		"\b\u0000\u000b\u0000\f\u0000\u0011\u0001\u0000\u0001\u0000\u0001\u0001"+
		"\u0001\u0001\u0003\u0001\u0018\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0004\u0002%\b\u0002\u000b\u0002\f\u0002&\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002.\b"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003"+
		"\u0005A\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0005\u0005I\b\u0005\n\u0005\f\u0005L\t\u0005\u0001"+
		"\u0005\u0001&\u0001\n\u0006\u0000\u0002\u0004\u0006\b\n\u0000\u0003\u0001"+
		"\u0000\u000e\u0011\u0001\u0000\f\r\u0001\u0000\n\u000bO\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0002\u0017\u0001\u0000\u0000\u0000\u0004\u0019\u0001"+
		"\u0000\u0000\u0000\u00061\u0001\u0000\u0000\u0000\b5\u0001\u0000\u0000"+
		"\u0000\n@\u0001\u0000\u0000\u0000\f\r\u0003\u0002\u0001\u0000\r\u000e"+
		"\u0005\u0012\u0000\u0000\u000e\u0010\u0001\u0000\u0000\u0000\u000f\f\u0001"+
		"\u0000\u0000\u0000\u0010\u0011\u0001\u0000\u0000\u0000\u0011\u000f\u0001"+
		"\u0000\u0000\u0000\u0011\u0012\u0001\u0000\u0000\u0000\u0012\u0013\u0001"+
		"\u0000\u0000\u0000\u0013\u0014\u0005\u0000\u0000\u0001\u0014\u0001\u0001"+
		"\u0000\u0000\u0000\u0015\u0018\u0003\u0004\u0002\u0000\u0016\u0018\u0003"+
		"\b\u0004\u0000\u0017\u0015\u0001\u0000\u0000\u0000\u0017\u0016\u0001\u0000"+
		"\u0000\u0000\u0018\u0003\u0001\u0000\u0000\u0000\u0019\u001a\u0005\u0001"+
		"\u0000\u0000\u001a\u001b\u0005\u0005\u0000\u0000\u001b\u001c\u0005\u0013"+
		"\u0000\u0000\u001c\u001d\u0005\u0006\u0000\u0000\u001d$\u0005\u0007\u0000"+
		"\u0000\u001e\u001f\u0005\u0002\u0000\u0000\u001f \u0005\u0014\u0000\u0000"+
		" !\u0005\u0003\u0000\u0000!\"\u0003\u0002\u0001\u0000\"#\u0005\u0012\u0000"+
		"\u0000#%\u0001\u0000\u0000\u0000$\u001e\u0001\u0000\u0000\u0000%&\u0001"+
		"\u0000\u0000\u0000&\'\u0001\u0000\u0000\u0000&$\u0001\u0000\u0000\u0000"+
		"\'-\u0001\u0000\u0000\u0000()\u0005\u0004\u0000\u0000)*\u0005\u0003\u0000"+
		"\u0000*+\u0003\u0002\u0001\u0000+,\u0005\u0012\u0000\u0000,.\u0001\u0000"+
		"\u0000\u0000-(\u0001\u0000\u0000\u0000-.\u0001\u0000\u0000\u0000./\u0001"+
		"\u0000\u0000\u0000/0\u0005\b\u0000\u00000\u0005\u0001\u0000\u0000\u0000"+
		"12\u0005\u0013\u0000\u000023\u0007\u0000\u0000\u000034\u0005\u0014\u0000"+
		"\u00004\u0007\u0001\u0000\u0000\u000056\u0005\u0013\u0000\u000067\u0005"+
		"\t\u0000\u000078\u0003\n\u0005\u00008\t\u0001\u0000\u0000\u00009:\u0006"+
		"\u0005\uffff\uffff\u0000:A\u0005\u0014\u0000\u0000;A\u0005\u0013\u0000"+
		"\u0000<=\u0005\u0005\u0000\u0000=>\u0003\n\u0005\u0000>?\u0005\u0006\u0000"+
		"\u0000?A\u0001\u0000\u0000\u0000@9\u0001\u0000\u0000\u0000@;\u0001\u0000"+
		"\u0000\u0000@<\u0001\u0000\u0000\u0000AJ\u0001\u0000\u0000\u0000BC\n\u0005"+
		"\u0000\u0000CD\u0007\u0001\u0000\u0000DI\u0003\n\u0005\u0006EF\n\u0004"+
		"\u0000\u0000FG\u0007\u0002\u0000\u0000GI\u0003\n\u0005\u0005HB\u0001\u0000"+
		"\u0000\u0000HE\u0001\u0000\u0000\u0000IL\u0001\u0000\u0000\u0000JH\u0001"+
		"\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000K\u000b\u0001\u0000\u0000"+
		"\u0000LJ\u0001\u0000\u0000\u0000\u0007\u0011\u0017&-@HJ";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}