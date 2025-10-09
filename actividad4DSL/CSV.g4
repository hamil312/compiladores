grammar CSV;

csvFile : header row* EOF ; // Permite cero o más filas completas y una última fila opcional
header  : row ;
row     : field (',' field)* (NL | EOF)? ;

field   : TEXT   # text
        | STRING # string
        ;

NL      : '\r'? '\n' ;
TEXT    : ~[,\n\r"]+ ;
STRING  : '"' ('""'|~'"')* '"' ;
WS      : [ \t]+ -> skip ;