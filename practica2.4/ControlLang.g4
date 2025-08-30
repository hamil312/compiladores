grammar ControlLang;

// Regla principal: permite múltiples sentencias terminadas en ';'
programa: (sentencia SEMI)+ EOF ;

// Sentencias permitidas
sentencia
    : ifElseStmt  
    | switchStmt
    | forStmt
    | asignacion  
    ;

// Regla para `if-else`
ifElseStmt
    : IF LPAREN condicion RPAREN LBRACE (sentencia SEMI?)* RBRACE (ELSE LBRACE (sentencia SEMI?)* RBRACE)? # IfElse
    ;

switchStmt
    : SWITCH LPAREN ID RPAREN LBRACE (CASE INT COLON sentencia SEMI)+? (DEFAULT COLON sentencia SEMI)? RBRACE # for
    ;

forStmt
    : FOR LPAREN asignacion SEMI condicion SEMI asignacion RPAREN LBRACE sentencia SEMI RBRACE # switch
    ;

// Condiciones dentro del `if`
condicion
    : ID op=(GT | LT | EQ | NEQ) INT  # CondicionSimple
    ;

// Asignaciones con `;`
asignacion
    : ID ASSIGN expresion  # Assign
    ;

// Expresiones matemáticas con prioridad de operadores
expresion
    : expresion op=(MUL | DIV) expresion     # MulDiv
    | expresion op=(PLUS | MINUS) expresion  # AddSub
    | INT                                    # Int
    | ID                                     # Variable
    | LPAREN expresion RPAREN                # Parens
    ;

// === TOKENS ===
IF     : 'if' ;
ELSE   : 'else' ;
FOR     : 'for' ;
SWITCH     : 'switch' ;
CASE   : 'case' ;
COLON : ':';
DEFAULT : 'default';
LPAREN : '(' ;
RPAREN : ')' ;
LBRACE : '{' ;
RBRACE : '}' ;
ASSIGN : '=' ;
PLUS   : '+' ;
MINUS  : '-' ;
MUL    : '*' ;
DIV    : '/' ;
GT     : '>' ;
LT     : '<' ;
EQ     : '==' ;
NEQ    : '!=' ;
SEMI   : ';' ;

// Reglas léxicas
ID  : [a-zA-Z_][a-zA-Z_0-9]* ;  // Identificadores
INT : [0-9]+ ;                  // Números enteros
WS  : [ \t\r\n]+ -> skip ;      // Ignorar espacios en blanco