// Gramática para o formato de resumo
grammar Summary;

// Definição dos tokens
TITLE       : 'title' ':' STRING;
TEXT        : 'text' ':' STRING;
FOCUS       : 'focus' ':' '[' STRING_LIST ']';
NUM_IDEAS   : 'num_ideas' ':' INT;
COMMENT     : 'personal_comment' ':' STRING;
WS          : [ \t\r\n]+ -> skip;

// Fragmentos
fragment CHAR : ~[\[\]\r\n];
STRING        : '"' CHAR+ '"';
STRING_LIST   : '"' CHAR+ '"' (',' '"' CHAR+ '"')*;

// Regra principal: estrutura do resumo
summary : 'summary' '{' title? text? focus? num_ideas? comment? '}';

// Regras auxiliares para cada parte do resumo
title       : TITLE;
text        : TEXT;
focus       : FOCUS;
num_ideas   : NUM_IDEAS;
comment     : COMMENT;
