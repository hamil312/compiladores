grammar WhileLang;

program: statement+ EOF; 

declaration: type ID ('=' expr)? SEMI; 

type: 'int' | 'string';

statement
    : assignment
    | ifStatement
    | whileStatement
    | declaration
    | breakStatement
    | continueStatement
    ;

assignment: ID ASSIGN expr SEMI;

breakStatement
    : BREAK SEMI
    ;

continueStatement
    : CONTINUE SEMI
    ;

ifStatement
    : IF LPAREN condition RPAREN LBRACE statement* RBRACE
    (ELSE LBRACE statement* RBRACE)?
    ;

whileStatement
    : WHILE LPAREN condition RPAREN LBRACE statement* RBRACE
    ;

condition
    : expr                       #ExprCondition
    ;

expr
    : ID                                       # idExpr
    | NUMBER                                   # numberExpr
    | STRING                                   # stringExpr
    | expr (LT | GT | GE | LE | EQ | NE) expr  # comparisonExpr
    | expr (PLUS | MINUS | MUL | DIV) expr     # arithmeticExpr
    | LPAREN expr RPAREN                       # parenExpr
    ;

IF: 'if';
ELSE: 'else';
WHILE: 'while';
LPAREN: '(';
RPAREN: ')';
LBRACE: '{';
RBRACE: '}';
SEMI: ';';
ASSIGN: '=';
LT: '<';
GT: '>';
GE: '>=';
LE: '<=';
EQ: '==';
NE: '!=';
PLUS: '+';
MINUS: '-';
MUL: '*';
DIV: '/';
BREAK: 'break';
CONTINUE: 'continue';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' (~["\r\n])* '"';
COMMENT: '//' .*? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;