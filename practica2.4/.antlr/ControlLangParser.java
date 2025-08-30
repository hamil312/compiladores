// Generated from /workspaces/compiladores/practica2.4/ControlLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class ControlLangParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, ELSE=2, FOR=3, SWITCH=4, CASE=5, COLON=6, DEFAULT=7, LPAREN=8, RPAREN=9, 
		LBRACE=10, RBRACE=11, ASSIGN=12, PLUS=13, MINUS=14, MUL=15, DIV=16, GT=17, 
		LT=18, EQ=19, NEQ=20, SEMI=21, ID=22, INT=23, WS=24;
	public static final int
		RULE_programa = 0, RULE_sentencia = 1, RULE_ifElseStmt = 2, RULE_switchStmt = 3, 
		RULE_forStmt = 4, RULE_condicion = 5, RULE_asignacion = 6, RULE_expresion = 7;
	private static String[] makeRuleNames() {
		return new String[] {
			"programa", "sentencia", "ifElseStmt", "switchStmt", "forStmt", "condicion", 
			"asignacion", "expresion"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'else'", "'for'", "'switch'", "'case'", "':'", "'default'", 
			"'('", "')'", "'{'", "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'>'", 
			"'<'", "'=='", "'!='", "';'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "ELSE", "FOR", "SWITCH", "CASE", "COLON", "DEFAULT", "LPAREN", 
			"RPAREN", "LBRACE", "RBRACE", "ASSIGN", "PLUS", "MINUS", "MUL", "DIV", 
			"GT", "LT", "EQ", "NEQ", "SEMI", "ID", "INT", "WS"
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
	public String getGrammarFileName() { return "ControlLang.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public ControlLangParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramaContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(ControlLangParser.EOF, 0); }
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(ControlLangParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(ControlLangParser.SEMI, i);
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
			setState(19); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(16);
				sentencia();
				setState(17);
				match(SEMI);
				}
				}
				setState(21); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 4194330L) != 0) );
			setState(23);
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
		public IfElseStmtContext ifElseStmt() {
			return getRuleContext(IfElseStmtContext.class,0);
		}
		public SwitchStmtContext switchStmt() {
			return getRuleContext(SwitchStmtContext.class,0);
		}
		public ForStmtContext forStmt() {
			return getRuleContext(ForStmtContext.class,0);
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
			setState(29);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(25);
				ifElseStmt();
				}
				break;
			case SWITCH:
				enterOuterAlt(_localctx, 2);
				{
				setState(26);
				switchStmt();
				}
				break;
			case FOR:
				enterOuterAlt(_localctx, 3);
				{
				setState(27);
				forStmt();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 4);
				{
				setState(28);
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
	public static class IfElseStmtContext extends ParserRuleContext {
		public IfElseStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifElseStmt; }
	 
		public IfElseStmtContext() { }
		public void copyFrom(IfElseStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IfElseContext extends IfElseStmtContext {
		public TerminalNode IF() { return getToken(ControlLangParser.IF, 0); }
		public TerminalNode LPAREN() { return getToken(ControlLangParser.LPAREN, 0); }
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ControlLangParser.RPAREN, 0); }
		public List<TerminalNode> LBRACE() { return getTokens(ControlLangParser.LBRACE); }
		public TerminalNode LBRACE(int i) {
			return getToken(ControlLangParser.LBRACE, i);
		}
		public List<TerminalNode> RBRACE() { return getTokens(ControlLangParser.RBRACE); }
		public TerminalNode RBRACE(int i) {
			return getToken(ControlLangParser.RBRACE, i);
		}
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public TerminalNode ELSE() { return getToken(ControlLangParser.ELSE, 0); }
		public List<TerminalNode> SEMI() { return getTokens(ControlLangParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(ControlLangParser.SEMI, i);
		}
		public IfElseContext(IfElseStmtContext ctx) { copyFrom(ctx); }
	}

	public final IfElseStmtContext ifElseStmt() throws RecognitionException {
		IfElseStmtContext _localctx = new IfElseStmtContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_ifElseStmt);
		int _la;
		try {
			_localctx = new IfElseContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(31);
			match(IF);
			setState(32);
			match(LPAREN);
			setState(33);
			condicion();
			setState(34);
			match(RPAREN);
			setState(35);
			match(LBRACE);
			setState(42);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4194330L) != 0)) {
				{
				{
				setState(36);
				sentencia();
				setState(38);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==SEMI) {
					{
					setState(37);
					match(SEMI);
					}
				}

				}
				}
				setState(44);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(45);
			match(RBRACE);
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(46);
				match(ELSE);
				setState(47);
				match(LBRACE);
				setState(54);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4194330L) != 0)) {
					{
					{
					setState(48);
					sentencia();
					setState(50);
					_errHandler.sync(this);
					_la = _input.LA(1);
					if (_la==SEMI) {
						{
						setState(49);
						match(SEMI);
						}
					}

					}
					}
					setState(56);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(57);
				match(RBRACE);
				}
			}

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
	public static class ForContext extends SwitchStmtContext {
		public TerminalNode SWITCH() { return getToken(ControlLangParser.SWITCH, 0); }
		public TerminalNode LPAREN() { return getToken(ControlLangParser.LPAREN, 0); }
		public TerminalNode ID() { return getToken(ControlLangParser.ID, 0); }
		public TerminalNode RPAREN() { return getToken(ControlLangParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(ControlLangParser.LBRACE, 0); }
		public TerminalNode RBRACE() { return getToken(ControlLangParser.RBRACE, 0); }
		public List<TerminalNode> CASE() { return getTokens(ControlLangParser.CASE); }
		public TerminalNode CASE(int i) {
			return getToken(ControlLangParser.CASE, i);
		}
		public List<TerminalNode> INT() { return getTokens(ControlLangParser.INT); }
		public TerminalNode INT(int i) {
			return getToken(ControlLangParser.INT, i);
		}
		public List<TerminalNode> COLON() { return getTokens(ControlLangParser.COLON); }
		public TerminalNode COLON(int i) {
			return getToken(ControlLangParser.COLON, i);
		}
		public List<SentenciaContext> sentencia() {
			return getRuleContexts(SentenciaContext.class);
		}
		public SentenciaContext sentencia(int i) {
			return getRuleContext(SentenciaContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(ControlLangParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(ControlLangParser.SEMI, i);
		}
		public TerminalNode DEFAULT() { return getToken(ControlLangParser.DEFAULT, 0); }
		public ForContext(SwitchStmtContext ctx) { copyFrom(ctx); }
	}

	public final SwitchStmtContext switchStmt() throws RecognitionException {
		SwitchStmtContext _localctx = new SwitchStmtContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_switchStmt);
		int _la;
		try {
			int _alt;
			_localctx = new ForContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(SWITCH);
			setState(61);
			match(LPAREN);
			setState(62);
			match(ID);
			setState(63);
			match(RPAREN);
			setState(64);
			match(LBRACE);
			setState(71); 
			_errHandler.sync(this);
			_alt = 1+1;
			do {
				switch (_alt) {
				case 1+1:
					{
					{
					setState(65);
					match(CASE);
					setState(66);
					match(INT);
					setState(67);
					match(COLON);
					setState(68);
					sentencia();
					setState(69);
					match(SEMI);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(73); 
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			} while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER );
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==DEFAULT) {
				{
				setState(75);
				match(DEFAULT);
				setState(76);
				match(COLON);
				setState(77);
				sentencia();
				setState(78);
				match(SEMI);
				}
			}

			setState(82);
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
	public static class ForStmtContext extends ParserRuleContext {
		public ForStmtContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forStmt; }
	 
		public ForStmtContext() { }
		public void copyFrom(ForStmtContext ctx) {
			super.copyFrom(ctx);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class SwitchContext extends ForStmtContext {
		public TerminalNode FOR() { return getToken(ControlLangParser.FOR, 0); }
		public TerminalNode LPAREN() { return getToken(ControlLangParser.LPAREN, 0); }
		public List<AsignacionContext> asignacion() {
			return getRuleContexts(AsignacionContext.class);
		}
		public AsignacionContext asignacion(int i) {
			return getRuleContext(AsignacionContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(ControlLangParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(ControlLangParser.SEMI, i);
		}
		public CondicionContext condicion() {
			return getRuleContext(CondicionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ControlLangParser.RPAREN, 0); }
		public TerminalNode LBRACE() { return getToken(ControlLangParser.LBRACE, 0); }
		public SentenciaContext sentencia() {
			return getRuleContext(SentenciaContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(ControlLangParser.RBRACE, 0); }
		public SwitchContext(ForStmtContext ctx) { copyFrom(ctx); }
	}

	public final ForStmtContext forStmt() throws RecognitionException {
		ForStmtContext _localctx = new ForStmtContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_forStmt);
		try {
			_localctx = new SwitchContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(84);
			match(FOR);
			setState(85);
			match(LPAREN);
			setState(86);
			asignacion();
			setState(87);
			match(SEMI);
			setState(88);
			condicion();
			setState(89);
			match(SEMI);
			setState(90);
			asignacion();
			setState(91);
			match(RPAREN);
			setState(92);
			match(LBRACE);
			setState(93);
			sentencia();
			setState(94);
			match(SEMI);
			setState(95);
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
		public TerminalNode ID() { return getToken(ControlLangParser.ID, 0); }
		public TerminalNode INT() { return getToken(ControlLangParser.INT, 0); }
		public TerminalNode GT() { return getToken(ControlLangParser.GT, 0); }
		public TerminalNode LT() { return getToken(ControlLangParser.LT, 0); }
		public TerminalNode EQ() { return getToken(ControlLangParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(ControlLangParser.NEQ, 0); }
		public CondicionSimpleContext(CondicionContext ctx) { copyFrom(ctx); }
	}

	public final CondicionContext condicion() throws RecognitionException {
		CondicionContext _localctx = new CondicionContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_condicion);
		int _la;
		try {
			_localctx = new CondicionSimpleContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(ID);
			setState(98);
			((CondicionSimpleContext)_localctx).op = _input.LT(1);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) ) {
				((CondicionSimpleContext)_localctx).op = (Token)_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(99);
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
		public TerminalNode ID() { return getToken(ControlLangParser.ID, 0); }
		public TerminalNode ASSIGN() { return getToken(ControlLangParser.ASSIGN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public AssignContext(AsignacionContext ctx) { copyFrom(ctx); }
	}

	public final AsignacionContext asignacion() throws RecognitionException {
		AsignacionContext _localctx = new AsignacionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_asignacion);
		try {
			_localctx = new AssignContext(_localctx);
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(ID);
			setState(102);
			match(ASSIGN);
			setState(103);
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
		public TerminalNode ID() { return getToken(ControlLangParser.ID, 0); }
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
		public TerminalNode MUL() { return getToken(ControlLangParser.MUL, 0); }
		public TerminalNode DIV() { return getToken(ControlLangParser.DIV, 0); }
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
		public TerminalNode PLUS() { return getToken(ControlLangParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(ControlLangParser.MINUS, 0); }
		public AddSubContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class ParensContext extends ExpresionContext {
		public TerminalNode LPAREN() { return getToken(ControlLangParser.LPAREN, 0); }
		public ExpresionContext expresion() {
			return getRuleContext(ExpresionContext.class,0);
		}
		public TerminalNode RPAREN() { return getToken(ControlLangParser.RPAREN, 0); }
		public ParensContext(ExpresionContext ctx) { copyFrom(ctx); }
	}
	@SuppressWarnings("CheckReturnValue")
	public static class IntContext extends ExpresionContext {
		public TerminalNode INT() { return getToken(ControlLangParser.INT, 0); }
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
		int _startState = 14;
		enterRecursionRule(_localctx, 14, RULE_expresion, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(112);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(106);
				match(INT);
				}
				break;
			case ID:
				{
				_localctx = new VariableContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(107);
				match(ID);
				}
				break;
			case LPAREN:
				{
				_localctx = new ParensContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(108);
				match(LPAREN);
				setState(109);
				expresion(0);
				setState(110);
				match(RPAREN);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(122);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(120);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
					case 1:
						{
						_localctx = new MulDivContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(114);
						if (!(precpred(_ctx, 5))) throw new FailedPredicateException(this, "precpred(_ctx, 5)");
						setState(115);
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
						setState(116);
						expresion(6);
						}
						break;
					case 2:
						{
						_localctx = new AddSubContext(new ExpresionContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expresion);
						setState(117);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(118);
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
						setState(119);
						expresion(5);
						}
						break;
					}
					} 
				}
				setState(124);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,11,_ctx);
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
		case 7:
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
		"\u0004\u0001\u0018~\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0004\u0000\u0014\b\u0000\u000b\u0000\f"+
		"\u0000\u0015\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0003\u0001\u001e\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002\'\b\u0002"+
		"\u0005\u0002)\b\u0002\n\u0002\f\u0002,\t\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u00023\b\u0002\u0005\u0002"+
		"5\b\u0002\n\u0002\f\u00028\t\u0002\u0001\u0002\u0003\u0002;\b\u0002\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0004\u0003H\b"+
		"\u0003\u000b\u0003\f\u0003I\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0003\u0003Q\b\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0003\u0007q\b\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0005"+
		"\u0007y\b\u0007\n\u0007\f\u0007|\t\u0007\u0001\u0007\u0001I\u0001\u000e"+
		"\b\u0000\u0002\u0004\u0006\b\n\f\u000e\u0000\u0003\u0001\u0000\u0011\u0014"+
		"\u0001\u0000\u000f\u0010\u0001\u0000\r\u000e\u0084\u0000\u0013\u0001\u0000"+
		"\u0000\u0000\u0002\u001d\u0001\u0000\u0000\u0000\u0004\u001f\u0001\u0000"+
		"\u0000\u0000\u0006<\u0001\u0000\u0000\u0000\bT\u0001\u0000\u0000\u0000"+
		"\na\u0001\u0000\u0000\u0000\fe\u0001\u0000\u0000\u0000\u000ep\u0001\u0000"+
		"\u0000\u0000\u0010\u0011\u0003\u0002\u0001\u0000\u0011\u0012\u0005\u0015"+
		"\u0000\u0000\u0012\u0014\u0001\u0000\u0000\u0000\u0013\u0010\u0001\u0000"+
		"\u0000\u0000\u0014\u0015\u0001\u0000\u0000\u0000\u0015\u0013\u0001\u0000"+
		"\u0000\u0000\u0015\u0016\u0001\u0000\u0000\u0000\u0016\u0017\u0001\u0000"+
		"\u0000\u0000\u0017\u0018\u0005\u0000\u0000\u0001\u0018\u0001\u0001\u0000"+
		"\u0000\u0000\u0019\u001e\u0003\u0004\u0002\u0000\u001a\u001e\u0003\u0006"+
		"\u0003\u0000\u001b\u001e\u0003\b\u0004\u0000\u001c\u001e\u0003\f\u0006"+
		"\u0000\u001d\u0019\u0001\u0000\u0000\u0000\u001d\u001a\u0001\u0000\u0000"+
		"\u0000\u001d\u001b\u0001\u0000\u0000\u0000\u001d\u001c\u0001\u0000\u0000"+
		"\u0000\u001e\u0003\u0001\u0000\u0000\u0000\u001f \u0005\u0001\u0000\u0000"+
		" !\u0005\b\u0000\u0000!\"\u0003\n\u0005\u0000\"#\u0005\t\u0000\u0000#"+
		"*\u0005\n\u0000\u0000$&\u0003\u0002\u0001\u0000%\'\u0005\u0015\u0000\u0000"+
		"&%\u0001\u0000\u0000\u0000&\'\u0001\u0000\u0000\u0000\')\u0001\u0000\u0000"+
		"\u0000($\u0001\u0000\u0000\u0000),\u0001\u0000\u0000\u0000*(\u0001\u0000"+
		"\u0000\u0000*+\u0001\u0000\u0000\u0000+-\u0001\u0000\u0000\u0000,*\u0001"+
		"\u0000\u0000\u0000-:\u0005\u000b\u0000\u0000./\u0005\u0002\u0000\u0000"+
		"/6\u0005\n\u0000\u000002\u0003\u0002\u0001\u000013\u0005\u0015\u0000\u0000"+
		"21\u0001\u0000\u0000\u000023\u0001\u0000\u0000\u000035\u0001\u0000\u0000"+
		"\u000040\u0001\u0000\u0000\u000058\u0001\u0000\u0000\u000064\u0001\u0000"+
		"\u0000\u000067\u0001\u0000\u0000\u000079\u0001\u0000\u0000\u000086\u0001"+
		"\u0000\u0000\u00009;\u0005\u000b\u0000\u0000:.\u0001\u0000\u0000\u0000"+
		":;\u0001\u0000\u0000\u0000;\u0005\u0001\u0000\u0000\u0000<=\u0005\u0004"+
		"\u0000\u0000=>\u0005\b\u0000\u0000>?\u0005\u0016\u0000\u0000?@\u0005\t"+
		"\u0000\u0000@G\u0005\n\u0000\u0000AB\u0005\u0005\u0000\u0000BC\u0005\u0017"+
		"\u0000\u0000CD\u0005\u0006\u0000\u0000DE\u0003\u0002\u0001\u0000EF\u0005"+
		"\u0015\u0000\u0000FH\u0001\u0000\u0000\u0000GA\u0001\u0000\u0000\u0000"+
		"HI\u0001\u0000\u0000\u0000IJ\u0001\u0000\u0000\u0000IG\u0001\u0000\u0000"+
		"\u0000JP\u0001\u0000\u0000\u0000KL\u0005\u0007\u0000\u0000LM\u0005\u0006"+
		"\u0000\u0000MN\u0003\u0002\u0001\u0000NO\u0005\u0015\u0000\u0000OQ\u0001"+
		"\u0000\u0000\u0000PK\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000"+
		"QR\u0001\u0000\u0000\u0000RS\u0005\u000b\u0000\u0000S\u0007\u0001\u0000"+
		"\u0000\u0000TU\u0005\u0003\u0000\u0000UV\u0005\b\u0000\u0000VW\u0003\f"+
		"\u0006\u0000WX\u0005\u0015\u0000\u0000XY\u0003\n\u0005\u0000YZ\u0005\u0015"+
		"\u0000\u0000Z[\u0003\f\u0006\u0000[\\\u0005\t\u0000\u0000\\]\u0005\n\u0000"+
		"\u0000]^\u0003\u0002\u0001\u0000^_\u0005\u0015\u0000\u0000_`\u0005\u000b"+
		"\u0000\u0000`\t\u0001\u0000\u0000\u0000ab\u0005\u0016\u0000\u0000bc\u0007"+
		"\u0000\u0000\u0000cd\u0005\u0017\u0000\u0000d\u000b\u0001\u0000\u0000"+
		"\u0000ef\u0005\u0016\u0000\u0000fg\u0005\f\u0000\u0000gh\u0003\u000e\u0007"+
		"\u0000h\r\u0001\u0000\u0000\u0000ij\u0006\u0007\uffff\uffff\u0000jq\u0005"+
		"\u0017\u0000\u0000kq\u0005\u0016\u0000\u0000lm\u0005\b\u0000\u0000mn\u0003"+
		"\u000e\u0007\u0000no\u0005\t\u0000\u0000oq\u0001\u0000\u0000\u0000pi\u0001"+
		"\u0000\u0000\u0000pk\u0001\u0000\u0000\u0000pl\u0001\u0000\u0000\u0000"+
		"qz\u0001\u0000\u0000\u0000rs\n\u0005\u0000\u0000st\u0007\u0001\u0000\u0000"+
		"ty\u0003\u000e\u0007\u0006uv\n\u0004\u0000\u0000vw\u0007\u0002\u0000\u0000"+
		"wy\u0003\u000e\u0007\u0005xr\u0001\u0000\u0000\u0000xu\u0001\u0000\u0000"+
		"\u0000y|\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000z{\u0001\u0000"+
		"\u0000\u0000{\u000f\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000\u0000"+
		"\f\u0015\u001d&*26:IPpxz";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}