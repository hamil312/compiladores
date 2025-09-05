grammar ForLang;

programa: (sentencia SEMI)+ EOF ;

sentencia
    : forStmt  
    | asignacion  
    ;

forStmt
    : FOR LPAREN asignacion SEMI condicion SEMI asignacion RPAREN LBRACE sentencia SEMI RBRACE # IfElse
    ;

condicion
    : ID op=(GT | LT | EQ | NEQ) INT  # CondicionSimple
    ;

asignacion
    : ID ASSIGN expresion  # Assign
    ;

expresion
    : expresion op=(MUL | DIV) expresion     # MulDiv
    | expresion op=(PLUS | MINUS) expresion  # AddSub
    | INT                                    # Int
    | ID                                     # Variable
    | LPAREN expresion RPAREN                # Parens
    ;

// === TOKENS ===
FOR     : 'for' ;
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