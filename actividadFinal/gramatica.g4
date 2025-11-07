grammar gramatica;

program
    : statement+ EOF
    ;

statement
    : assignment
    | printStmt
    | ifStmt
    | whileStmt
    | block
    ;

assignment
    : ID ASSIGN (boolExpr | arithExpr) SEMI
    ;

printStmt
    : PRINT LPAREN ID RPAREN SEMI
    ;

ifStmt
    : IF LPAREN boolExpr RPAREN block (ELSE block)?
    ;

whileStmt
    : WHILE LPAREN boolExpr RPAREN block
    ;

block
    : LBRACE statement* RBRACE
    ;

boolExpr
    : boolExpr OR boolTerm
    | boolTerm
    ;

boolTerm
    : boolTerm AND boolFactor
    | boolFactor
    ;

boolFactor
    : NOT boolFactor
    | LPAREN boolExpr RPAREN
    | TRUE
    | FALSE
    | ID                              
    | comparison                      
    ;

comparison
    : arithExpr compOp arithExpr
    ;

compOp
    : EQ
    | NEQ
    | LT
    | LTE
    | GT
    | GTE
    ;

arithExpr
    : arithExpr ADD arithTerm
    | arithExpr SUB arithTerm
    | arithTerm
    ;

arithTerm
    : arithTerm MUL arithFactor
    | arithTerm DIV arithFactor
    | arithFactor
    ;

arithFactor
    : SUB arithFactor                    
    | LPAREN arithExpr RPAREN
    | INT
    | ID                                 
    ;


AND     : 'and' | 'AND' | 'And' | '&&';
OR      : 'or' | 'OR' | 'Or' | '||';
NOT     : 'not' | 'NOT' | 'Not' | '!';

IF      : 'if' | 'IF' | 'If';
ELSE    : 'else' | 'ELSE' | 'Else';
WHILE   : 'while' | 'WHILE' | 'While';
PRINT   : 'print' | 'PRINT' | 'Print';

TRUE    : 'TRUE' | 'true' | 'True';
FALSE   : 'FALSE' | 'false' | 'False';

ASSIGN  : '=';
SEMI    : ';';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
ADD     : '+';
SUB     : '-';
MUL     : '*';
DIV     : '/';

EQ      : '==';
NEQ     : '!=';
LTE     : '<=';
GTE     : '>=';
LT      : '<';
GT      : '>';

ID
    : [a-zA-Z_] [a-zA-Z_0-9]*
    ;

INT
    : [0-9]+
    ;

WS
    : [ \t\r\n]+ -> skip
    ;

LINE_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

BLOCK_COMMENT
    : '/*' .*? '*/' -> skip
    ;