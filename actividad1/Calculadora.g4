grammar Calculadora;

prog: (asignacion | expresion) EOF ;

asignacion  : ID '=' expresion ';' ;

expresion
    : '-' expresion                       # Negativo 
    | expresion '^' expresion             # Potencia
    | expresion ('*'|'/') expresion       # MultDiv
    | expresion ('+'|'-') expresion       # AddSub
    | ID '(' expresion ')'                # Funcion
    | '(' expresion ')'                   # Parentesis
    | NUMBER                              # Numero
    | ID                                  # Variable
    ;

ID       : [a-zA-Z_][a-zA-Z_0-9]* ;
NUMBER   : [0-9]+ ('.' [0-9]+)? ;
WS       : [ \t\r\n]+ -> skip ;