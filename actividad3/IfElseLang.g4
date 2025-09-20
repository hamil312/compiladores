grammar IfElseLang;

// Funciones y sentencias
program: (statement | functionDecl)+ EOF;

// Sentencias posibles
statement
    : assignment
    | ifStatement
    | declaration
    | returnStatement
    | expr SEMI
    ;

// Asignación de variable
assignment: ID ASSIGN expr SEMI;

// Declaración de variable Cambio
declaration: type ID (ASSIGN expr)? SEMI;

// Sentencia de retorno
returnStatement: 'return' expr SEMI;

// Sentencia if-else
ifStatement: IF LPAREN condition RPAREN block (ELSE block)?;

// Bloque de sentencias
block: LBRACE statement* RBRACE;

// Declaración de función
functionDecl: type ID LPAREN paramList? RPAREN block;

// Parámetros de función
param: type ID;
paramList: param (',' param)*;

// Condición booleana
condition: expr operator expr;

// Aumentando expresiones y parentesis a expr, operadores aritméticos y llamada a función
expr
    : expr PLUS expr         # addExpr
    | expr MINUS expr        # subExpr
    | expr MULT expr         # mulExpr
    | expr DIV expr          # divExpr
    | ID LPAREN argList? RPAREN   # funcCallExpr
    | ID                          # idExpr
    | NUMBER                      # numberExpr
    | STRING                      # stringExpr
    | LPAREN expr RPAREN          # parenExpr
    ;

// Argumentos de llamada a función
argList: expr (',' expr)*;

// Operadores relacionales
operator: LT | GT | GE | LE | NE;

// Tipos de datos agregados para reconocimiento 
type: INT_TYPE | FLOAT_TYPE | VOID_TYPE | STRING_TYPE;

// Palabras y símbolos
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
NE: '!=';
PLUS: '+';
MINUS: '-';
MULT: '*';
DIV: '/';
INT_TYPE: 'int';
STRING_TYPE: 'string';
VOID_TYPE: 'void';
FLOAT_TYPE: 'float';

// Identificadores, números y cadenas agregadas
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;
STRING: '"' (~["\r\n])* '"';
// Comentarios agregados
COMMENT: '//' .*? '\n' -> skip;
WS: [ \t\r\n]+ -> skip;