grammar IfElseLang;

program: statement+ EOF; 

declaration: type ID ('=' expr)? SEMI; 

type: 'int' | 'string';

statement
    : assignment
    | ifStatement
    | declaration
    | forStatement
    | switchStatement
    ;

forStatement
    : FOR LPAREN (declarationNoSemi | assignmentNoSemi | SEMI)
      condition SEMI
      (assignmentNoSemi)?
      RPAREN LBRACE statement* RBRACE
    ;

declarationNoSemi: type ID ('=' expr)? ;
assignmentNoSemi: ID ASSIGN expr ;

switchStatement
    : 'switch' LPAREN expr RPAREN LBRACE caseStatement+ (defaultStatement)? RBRACE
    ;

caseStatement
    : 'case' expr COLON statement* BREAK SEMI
    ;

defaultStatement
    : 'default' COLON statement* (BREAK SEMI)?
    ;

assignment: ID ASSIGN expr SEMI;

ifStatement
    : IF LPAREN condition RPAREN LBRACE statement* RBRACE
    (ELSE LBRACE statement* RBRACE)?
    ;

condition: expr; // ahora condición es cualquier expresión booleana

// Expresiones con etiquetas
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
FOR     : 'for';
SWITCH  : 'switch';
CASE    : 'case';
DEFAULT : 'default';
COLON   : ':';
BREAK   : 'break';

ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' (~["\r\n])* '"';
COMMENT: '//' .*? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;