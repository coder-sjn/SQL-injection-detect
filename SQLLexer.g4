lexer grammar SQLLexer;

  /* keywords */
ALL: 'ALL' | All;
ANY: 'ANY';
AS: 'AS';
ASC: 'ASC';
AUTO_INCREMENT: 'AUTO_INCREMENT';
BETWEEN: 'BETWEEN';
BIGINT: 'BIGINT|INT8';
BINARY: 'BINARY';
BIT: 'BIT';
BLOB: 'BLOB';
BOOLEAN: 'BOOLEAN';
BOTH: 'BOTH';
BY: 'BY';
CASE: 'CASE';
CHAR: 'CHARACTER'|'CHAR'|'CHR';
COLLATE: 'COLLATE';
COMMENT: 'COMMENT';
CONVERT: 'CONVERT';
COUNT: 'COUNT';
CREATE: 'CREATE';
CROSS: 'CROSS';
DATABASE: 'DATABASE';
DATE: 'DATE';
DATETIME: 'DATETIME';
DAY: 'DAY';
DAY_HOUR: 'DAY_HOUR';
DAY_MICROSECOND: 'DAY_MICROSECOND';
DAY_MINUTE: 'DAY_MINUTE';
DAY_SECOND: 'DAY_SECOND';
DECIMAL: 'DECIMAL'|'NUMERIC'|'DEC';
DEFAULT: 'DEFAULT';
DELAYED: 'DELAYED';
DELETE: 'DELETE';
DEFINITION: 'DEFINITION';
DROP: 'DROP';
DESC: 'DESC';
DISTINCT: 'DISTINCT';
DISTINCTROW: 'DISTINCTROW';
DIV: 'DIV';
DUMPFILE: 'DUMPFILE';
DOUBLE: 'FLOAT8'|'DOUBLE';
ELSE: 'ELSE';
END: 'END';
ENCLOSED: 'ENCLOSED';
ENUM: 'ENUM';
ESCAPE: 'ESCAPE';
ESCAPED: 'ESCAPED';
EXISTS: 'EXISTS'|'NOT'[ \t\n]'EXISTS';
FIELDS: 'FIELDS';
FLOAT: 'FLOAT'|'FLOAT4';
FOR: 'FOR';
FORCE: 'FORCE';
FROM: 'FROM' | From;
FULLTEXT: 'FULLTEXT';
GROUP: 'GROUP';
HAVING: 'HAVING';
HIGH_PRIORITY: 'HIGH_PRIORITY';
HOUR: 'HOUR';
HOUR_MICROSECOND: 'HOUR_MICROSECOND';
HOUR_MINUTE: 'HOUR_MINUTE';
HOUR_SECOND: 'HOUR_SECOND';
IF: 'IF';
IGNORE: 'IGNORE';
IN: 'IN';
INDEX: 'INDEX';
INNER: 'INNER';
INSERT: 'INSERT';
INTEGER: 'INT'|'INT4'|'INTEGER';
INTERVAL: 'INTERVAL';
INTO: 'INTO';
IS: 'IS';
JOIN: 'JOIN';
KEY: 'KEY';
LEADING: 'LEADING';
LEFT: 'LEFT';
LIKE: 'LIKE';
LIMIT: 'LIMIT';
LINES: 'LINES';
LOCK: 'LOCK';
LONGBLOB: 'LONGBLOB';
LONGTEXT: 'LONGTEXT';
LOW_PRIORITY: 'LOW_PRIORITY';
MEDIUMBLOB: 'MEDIUMBLOB';
MICROSECOND: 'MICROSECOND';
MEDIUMINT: 'MIDDLEINT'|'MEDIUMINT';
MEDIUMTEXT: 'MEDIUMTEXT';
MINUTE: 'MINUTE';
MINUTE_MICROSECOND: 'MINUTE_MICROSECOND';
MINUTE_SECOND: 'MINUTE_SECOND';
MOD: 'MOD';
MODE: 'MODE';
MONTH: 'MONTH';
NATURAL: 'NATURAL';
NCHAR: 'NCHAR';
NVARCHAR: 'NVARCHAR';
NOT: 'NOT';
NULLX: 'NULL';
OFFSET: 'OFFSET';
ON: 'ON';
ONDUPLICATE: 'ON'[ \t\n]'DUPLICATE';
ONLY: 'ONLY';
OPTIONALLY: 'OPTIONALLY';
ORDER: 'ORDER';
OUTER: 'OUTER';
OUTFILE: 'OUTFILE';
PARTITION: 'PARTITION';
POSITION: 'POSITION';
PRIMARY: 'PRIMARY';
QUARTER: 'QUARTER';
QUICK: 'QUICK';
REAL: 'REAL';
REGEXP: 'REGEXP'|'RLIKE';
REPLACE: 'REPLACE';
RIGHT: 'RIGHT';
ROW: 'ROW';
SCHEMA: 'SCHEMA';
SECOND: 'SECOND';
SECOND_MICROSECOND: 'SECOND_MICROSECOND';
SELECT: 'SELECT' | Select;
SET: 'SET';
SHARE: 'SHARE';
SIGNED: 'SIGNED';
SMALLINT: 'INT2'|'SMALLINT';
SOME: 'SOME';
SOUNDS: 'SOUNDS';
SQL_BIG_RESULT: 'SQL_BIG_RESULT';
SQL_CALC_FOUND_ROWS: 'SQL_CALC_FOUND_ROWS';
SQL_SMALL_RESULT: 'SQL_SMALL_RESULT';
STARTING: 'STARTING';
STRAIGHT_JOIN: 'STRAIGHT_JOIN';
TABLE: 'TABLE';
TEMPORARY: 'TEMPORARY';
TERMINATED: 'TERMINATED';
TEXT: 'TEXT';
THEN: 'THEN';
TIME: 'TIME';
TIMESTAMP: 'TIMESTAMP';
TINYBLOB: 'TINYBLOB';
TINYINT: 'INT1'|'TINYINT';
TINYTEXT: 'TINYTEXT';
TRAILING: 'TRAILING';
UNICODE: 'UNICODE';
UNION: 'UNION' | Union;
UNIQUE: 'UNIQUE';
UNSIGNED: 'UNSIGNED';
UPDATE: 'UPDATE';
USE: 'USE';
USING: 'USING';
VALUES: 'VALUES';
VARBINARY: 'VARBINARY';
VARCHAR: 'VARCHARACTER'|'VARCHAR';
WEEK: 'WEEK';
WHEN: 'WHEN';
WHERE: 'WHERE' | Where;
XOR: 'XOR';
YEAR: 'YEAR';
YEAR_MONTH: 'YEAR_MONTH';
ZEROFILL: 'ZEROFILL';

    /* Charsets */

ARMSCII8: 'ARMSCII8';
ASCII: 'ASCII';
BIG5: 'BIG5';
CP1250: 'CP1250';
CP1251: 'CP1251';
CP1256: 'CP1256';
CP1257: 'CP1257';
CP850: 'CP850';
CP852: 'CP852';
CP866: 'CP866';
CP932: 'CP932';
DEC8: 'DEC8';
EUCJPMS: 'EUCJPMS';
EUCKR: 'EUCKR';
GB2312: 'GB2312';
GBK: 'GBK';
GEOSTD8: 'GEOSTD8';
GREEK: 'GREEK';
HEBREW: 'HEBREW';
HP8: 'HP8';
KEYBCS2: 'KEYBCS2';
KOI8R: 'KOI8R';
KOI8U: 'KOI8U';
LATIN1: 'LATIN1';
LATIN2: 'LATIN2';
LATIN5: 'LATIN5';
LATIN7: 'LATIN7';
MACCE: 'MACCE';
MACROMAN: 'MACROMAN';
SJIS: 'SJIS';
SWE7: 'SWE7';
TIS620: 'TIS620';
UCS2: 'UCS2';
UJIS: 'UJIS';
UTF16: 'UTF16';
UTF16LE: 'UTF16LE';
UTF32: 'UTF32';
UTF8: 'UTF8';
UTF8MB3: 'UTF8MB3';
UTF8MB4: 'UTF8MB4';

    /* functions */
SUBSTRING: 'SUBSTRING'|'SUBSTR';
TRIM: 'TRIM';
CAST: 'CAST';
EXTRACT: 'EXTRACT';
WEIGHT_STRING: 'WEIGHT_STRING';

ASSIGN: ':=';
TYPECAST: '::';

    /* booleans */
BOOL: 'true'|'unknown'|'false';

   /* numbers */
NUM: [-+]?[0-9]+ |
     [-+]?[0-9]+'E'[-+]?[0-9]+ |
     [-+]?[0-9]+'.'[0-9]* |
     [-+]?[0-9]+'.'[0-9]*'E'[-+]?[0-9]+ |
     [-+]?'.'[0-9]+ |
     [-+]?'.'[0-9]+'E'[-+]?[0-9]+;

    /* operators */
DOT:              '.';
LR_BRACKET:       '(';
RR_BRACKET:       ')';
BIG_LR_BRACKET:       '{';
BIG_RR_BRACKET:       '}';
COMMA:                      ',';
SEMI:                            ';';
STAR:                           '*';
DIVIDE:                         '/';
MODULE:                     '%';
PLUS:                            '+';
MINUS:                         '-';
BIT_NOT:                      '~';
BIT_OR:                         '|';
BIT_AND:                      '&';
BIT_XOR:                      '^';
EXCLAMATION:            '!';
AT:                     '@';
UNDERLINE:              '_';
HYPHEN:                 '`';

AND: '&&'|'AND';
OR: '||'|'OR';

COMPARISON: '='|'<=>'|'>='|'>'|'<='|'<'|'!='|'<>';

SHIFT: '<<'|'>>';

    /* strings */
QUOTA_STRING: '\''('\\'.|'\'''\''|~['\n])*'\'';
DOUBLE_QUOTA_STRING: '"'('\\'.|'"''"'|~["\n])*'"';
BQUOTA_STRING: '`'('\\'.|'`''`'|~[`\n])*'`';
HEX_STRING: 'X''\''[0-9A-Fa-f]+'\'' | '0''X'[0-9A-Fa-f]+;
BIT_STRING: 'B''\''[01]+'\'' | '0''B'[01]+;
START_NATIONAL_STRING_LITERAL: [nN]'\''('\\'.|'\'''\''|~['\n])*'\'';
IDENT: [A-Za-z_$0-9]*?[A-Za-z_$]+?[A-Za-z_$0-9]*;

    /* user variables */
USERVAR: '@'[A-Za-z0-9._$]+ |
         '@''"'('\\'.|'"''"'|~["\n])*'"' |
         '@''\''('\\'.|'\'''\''|~['\n])*'\'' |
         '@''`'('\\'.|'`''`'|~[`\n])*'`';

   /* system variables */
SYSVAR: '@''@'[A-Za-z0-9._$]+ |
        '@''@''`'('\\'.|'`''`'|~[`\n])*'`';

    /* comments */
OPEN: '/*!' -> pushMode(INSIDE);
COMMENT1: '/*' ~[!]*? '*/' -> skip;
COMMENT2: '#'.* -> skip;
COMMENT3: '--'[ \t]?.* -> skip;

NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t\r\n]+ -> skip ; // toss out whitespace

/*-------------------------------------------INSIDE-----------------------------------------------*/
mode INSIDE;

CLOSE: '*/' -> popMode;

Select: 'SELECT';
Union: 'UNION';
All: 'ALL';
From: 'FROM';
Where: 'WHERE';

S  :   [ \t\r\n]+ -> skip ; // toss out whitespace