parser grammar SQLParser;
options { tokenVocab=SQLLexer; }
prog:    stmt_list+ ;

stmt_list:
  stmt 
  | functionCall 
  | from_clause 
  | where_clause 
  | group_clause 
  | having_clause 
  | order_clause 
  | limit_clause
  ;

/* statements: select statement */

stmt: union_select_stmt
   | select_stmt
   | delete_stmt
   | drop_stmt
   | insert_stmt
   | replace_stmt
   | update_stmt
   | create_database_stmt
   | create_table_stmt
   | set_stmt
   ;

select_stmt:
     query_expression
   | query_expression into_clause
   ;

query_expression_parens:
     '(' query_expression_parens ')'
   | '(' query_expression ')'
   ;

query_expression:
     query_expression_body opt_order_clause opt_limit_clause opt_locking_clause
   | query_expression_parens order_clause opt_limit_clause opt_locking_clause
   | query_expression_parens limit_clause opt_locking_clause
   | query_expression_parens locking_clause
   ;

query_expression_body:
     query_specification
   | query_expression_body union_select_stmt
   | query_expression_parens union_select_stmt
   ;

union_select_stmt:
    UNION union_option query_specification 
    | UNION union_option query_expression_parens ;


opt_locking_clause: /* Empty. */
        | locking_clause
        ;

locking_clause:
          FOR UPDATE
        | LOCK IN SHARE MODE
        ;

union_option: /* empty */
        | DISTINCT
        | ALL
        ;

query_specification:
     SELECT select_opts select_item_list into_clause opt_from_clause opt_where_clause opt_group_clause opt_having_clause 
   | SELECT select_opts select_item_list opt_from_clause opt_where_clause opt_group_clause opt_having_clause 
   ;

opt_from_clause: /* empty */
   |  from_clause 
   ;
from_clause: FROM table_reference_list ;

opt_where_clause: /* empty */
   |  where_clause 
   ;
where_clause: WHERE expr;

opt_group_clause: /* empty */
   | group_clause 
   ;
group_clause: GROUP BY group_list;

opt_having_clause: /* empty */
   | having_clause 
   ;
having_clause: HAVING expr;

opt_order_clause: /* empty */
        | order_clause
        ;
order_clause:ORDER BY order_list;

opt_limit_clause: /* empty */
        | limit_clause
        ;
limit_clause: LIMIT limit_options;

group_list:
     group_list COMMA expr
   | expr
   ;

order_list:
          order_list COMMA order_expr
        | order_expr
        ;

order_expr:
          expr opt_ordering_direction
        ;

opt_ordering_direction: /* empty */
        | ASC
        | DESC

        ;

limit_options:
          limit_option
        | limit_option COMMA limit_option
        | limit_option OFFSET limit_option
        ;

limit_option:
          NUM
        ;

select_item_list:
     select_item_list COMMA select_item
   | select_item
   | STAR
   ;

select_item:
     table_wild
   | expr AS collabel
   | expr AS string_literal
   | expr ident
   | expr string_literal
   | expr
   ;

/* Column label --- allowed labels in "AS" clauses.
 * This presently includes *all* Postgres keywords.
 */
collabel: ident
   | reserved_keyword
   ;

table_wild:
     ident '.' STAR
   | ident '.' ident '.' STAR
   ;

/* mysql: In the select list of a query, a quoted column alias can be specified using identifier or string quoting characters */
opt_alias: /* empty */
   | AS ident
   | AS string_literal
   | ident
   | string_literal
   ;

into_clause:
     INTO into_destination
   ;

into_destination:
     OUTFILE string_literal opt_load_data_charset opt_field_term opt_line_term
   | DUMPFILE string_literal
   | select_var_list
   ;

opt_load_data_charset: /* Empty */
        | character_set charset_name
        ;

opt_field_term: /* empty */
   | FIELDS field_term_list
   ;

field_term_list:
     field_term_list field_term
   | field_term
   ;

field_term:
     TERMINATED BY string_literal
   | OPTIONALLY ENCLOSED BY string_literal
   | ENCLOSED BY string_literal
   | ESCAPED BY string_literal
   ;

opt_line_term: /* empty */
   | LINES line_term_list
   ;

line_term_list:
     line_term_list line_term
   | line_term
   ;

line_term:
     TERMINATED BY string_literal
   | STARTING BY string_literal
   ;

select_var_list:
     select_var_list COMMA select_var_ident
   | select_var_ident
   ;

select_var_ident:
     '@' ident_or_text
   | ident_or_text
   ;

ident_or_text:
     ident
   | string_literal
   ;

column_list: ident
  | column_list COMMA ident
  ;

select_opts:
| select_opts ALL
| select_opts DISTINCT
| select_opts DISTINCTROW
| select_opts HIGH_PRIORITY
| select_opts STRAIGHT_JOIN
| select_opts SQL_SMALL_RESULT
| select_opts SQL_BIG_RESULT
| select_opts SQL_CALC_FOUND_ROWS
    ;

esc_table_reference:
      table_factor
    | joined_table
    ;

table_reference:
      table_factor
    | BIG_LR_BRACKET ident esc_table_reference BIG_RR_BRACKET
    ;

table_factor:
          single_table
        | single_table_parens
        | table_subquery opt_table_alias opt_derived_column_list
        | joined_table_parens
        | table_reference_list_parens
        | functionCall
  ;

joined_table_parens:
          '(' joined_table_parens ')'
        | '(' joined_table ')'
        ;

table_reference_list_parens:
          '(' table_reference_list_parens ')'
        | '(' table_reference_list COMMA table_reference ')'
        ;

table_reference_list:
          table_reference
        | table_reference_list COMMA table_reference
        ;

opt_derived_column_list: /* empty */
        | '(' index_list ')'
        ;

single_table_parens:
          '(' single_table_parens ')'
        | '(' single_table ')'
        ;

single_table:
          tbl_name opt_use_partition opt_table_alias opt_index_hints_list
        ;

opt_table_alias: /* empty */
        | AS ident
        | ident
        ;

opt_as: /* empty */
        | AS
        ;

index_hints_list:
          index_hint
        | index_hints_list index_hint
        ;

opt_index_hints_list: /* empty */
        | index_hints_list
        ;

opt_use_partition: /* empty */
        | use_partition
        ;

use_partition:
          PARTITION '(' index_list ')'
        ;

joined_table:
     joined_table opt_inner_cross JOIN table_factor opt_join_condition
   | joined_table STRAIGHT_JOIN table_factor
   | joined_table STRAIGHT_JOIN table_factor ON expr
   | joined_table left_or_right opt_outer JOIN table_factor join_condition
   | joined_table NATURAL opt_left_or_right_outer JOIN table_factor
   | table_reference opt_inner_cross JOIN table_factor opt_join_condition
   | table_reference STRAIGHT_JOIN table_factor
   | table_reference STRAIGHT_JOIN table_factor ON expr
   | table_reference left_or_right opt_outer JOIN table_factor join_condition
   | table_reference NATURAL opt_left_or_right_outer JOIN table_factor
   ;

tbl_name: ident ('.' ident)* ;

opt_inner_cross: /* nil */
   | INNER
   | CROSS
   ;

opt_outer: /* nil */
   | OUTER
   ;

left_or_right: LEFT
    | RIGHT
    ;

opt_left_or_right_outer: LEFT opt_outer
   | RIGHT opt_outer
   | /* nil */
   ;

opt_join_condition: join_condition | /* nil */ ;

join_condition:
    ON expr
    | USING '(' column_list ')'
    ;

index_hint:
     USE key_or_index opt_index_hint_clause '(' index_list ')'
   | IGNORE key_or_index opt_index_hint_clause '(' index_list ')'
   | FORCE key_or_index opt_index_hint_clause '(' index_list ')'
   ;

key_or_index:
          KEY
        | INDEX
        ;

opt_index_hint_clause: /* empty */
    | FOR JOIN
    | FOR ORDER BY
    | FOR GROUP BY
    ;

index_list: ident
   | index_list COMMA ident
   ;

table_subquery: '(' select_stmt ')'
   ;

   /* statements: delete statement */
delete_stmt: DELETE delete_opts FROM ident opt_where_clause opt_order_clause opt_limit_clause	
   | DELETE delete_opts delete_list FROM table_reference_list opt_where_clause
   | DELETE delete_opts FROM delete_list USING table_reference_list opt_where_clause
   ;

delete_opts: delete_opts LOW_PRIORITY
   | delete_opts QUICK
   | delete_opts IGNORE
   | /* nil */
   ;

delete_list: ident opt_dot_star
   | delete_list COMMA ident opt_dot_star
   ;

opt_dot_star: /* nil */
   | '.' STAR
   ;

   /* statements: drop statement */
drop_stmt:
   DROP (DATABASE|TABLE) opt_if_not_exists ident
   ;

   /* statements: insert statement */
insert_stmt: INSERT insert_opts opt_into ident opt_col_names VALUES insert_vals_list opt_ondupupdate
   | INSERT insert_opts opt_into ident SET insert_asgn_list opt_ondupupdate
   | INSERT insert_opts opt_into ident opt_col_names select_stmt opt_ondupupdate
   ;

opt_ondupupdate: /* nil */
   | ONDUPLICATE KEY UPDATE insert_asgn_list
   ;

insert_opts: /* nil */
   | insert_opts LOW_PRIORITY
   | insert_opts DELAYED
   | insert_opts HIGH_PRIORITY
   | insert_opts IGNORE
   ;

opt_into: INTO | /* nil */
   ;

opt_col_names: /* nil */
   | '(' column_list ')'
   ;

insert_vals_list: '(' insert_vals ')'
   | insert_vals_list COMMA '(' insert_vals ')'
   ;

insert_vals:
     expr
   | DEFAULT
   | insert_vals COMMA expr
   | insert_vals COMMA DEFAULT
   ;

insert_asgn_list:
     ident COMPARISON expr
   | ident COMPARISON DEFAULT
   | insert_asgn_list COMMA ident COMPARISON expr
   | insert_asgn_list COMMA ident COMPARISON DEFAULT
   ;

   /** replace just like insert **/
replace_stmt: REPLACE insert_opts opt_into ident opt_col_names VALUES insert_vals_list opt_ondupupdate
   | REPLACE insert_opts opt_into ident SET insert_asgn_list opt_ondupupdate
   | REPLACE insert_opts opt_into ident opt_col_names select_stmt opt_ondupupdate
   ;

/** update **/
update_stmt: UPDATE update_opts table_reference_list
    SET update_asgn_list
    opt_where_clause
    opt_order_clause
    opt_limit_clause
    ;

update_opts: /* nil */
   | insert_opts LOW_PRIORITY
   | insert_opts IGNORE
   ;

update_asgn_list:
     ident COMPARISON expr
   | ident '.' ident COMPARISON expr
   | update_asgn_list COMMA ident COMPARISON expr
   | update_asgn_list COMMA ident '.' ident COMPARISON expr
   ;


   /** create database **/
create_database_stmt:
     CREATE DATABASE opt_if_not_exists ident
   | CREATE SCHEMA opt_if_not_exists ident
   ;

opt_if_not_exists:  /* nil */
   | IF EXISTS
   ;


/** create table **/
create_table_stmt: CREATE opt_temporary TABLE opt_if_not_exists ident '(' create_col_list ')'
   | CREATE opt_temporary TABLE opt_if_not_exists ident '.' ident '(' create_col_list ')'
   | CREATE opt_temporary TABLE opt_if_not_exists ident '(' create_col_list ')' create_select_statement
   | CREATE opt_temporary TABLE opt_if_not_exists ident create_select_statement
   | CREATE opt_temporary TABLE opt_if_not_exists ident '.' ident '(' create_col_list ')' create_select_statement
   | CREATE opt_temporary TABLE opt_if_not_exists ident '.' ident create_select_statement
   | CREATE opt_temporary TABLE opt_if_not_exists ident ('.' ident)* LIKE ident ('.' ident)*
   | CREATE opt_temporary TABLE opt_if_not_exists ident ('.' ident)* (AS)? select_stmt DEFINITION ONLY
   ;

create_col_list: create_definition
    | create_col_list COMMA create_definition
    ;

create_definition: ident data_type column_atts
    | PRIMARY KEY '(' column_list ')'
    | KEY '(' column_list ')'
    | INDEX '(' column_list ')'
    | FULLTEXT INDEX '(' column_list ')'
    | FULLTEXT KEY '(' column_list ')'
    ;

column_atts: /* nil */
    | column_atts NOT NULLX
    | column_atts NULLX
    | column_atts DEFAULT string_literal
    | column_atts DEFAULT NUM
    | column_atts DEFAULT BOOL
    | column_atts AUTO_INCREMENT
    | column_atts UNIQUE '(' column_list ')'
    | column_atts UNIQUE KEY
    | column_atts PRIMARY KEY
    | column_atts KEY
    | column_atts COMMENT string_literal
    ;

opt_length: /* nil */
   | '(' NUM ')'
   | '(' NUM COMMA NUM ')'
   ;

opt_binary: /* nil */
   | BINARY
   ;

opt_uz: /* nil */
   | opt_uz UNSIGNED
   | opt_uz ZEROFILL
   ;

opt_csc: /* nil */
   | opt_csc CHAR SET string_literal
   | opt_csc COLLATE string_literal
   ;

data_type:
     BIT opt_length
   | TINYINT opt_length opt_uz
   | SMALLINT opt_length opt_uz
   | MEDIUMINT opt_length opt_uz
   | INTEGER opt_length opt_uz
   | BIGINT opt_length opt_uz
   | REAL opt_length opt_uz
   | DOUBLE opt_length opt_uz
   | FLOAT opt_length opt_uz
   | DECIMAL opt_length opt_uz
   | DATE
   | TIME
   | TIMESTAMP
   | DATETIME
   | YEAR
   | CHAR opt_length opt_csc
   | VARCHAR '(' NUM ')' opt_csc
   | NVARCHAR '(' NUM ')' opt_csc
   | BINARY opt_length
   | VARBINARY '(' NUM ')'
   | TINYBLOB
   | BLOB
   | MEDIUMBLOB
   | LONGBLOB
   | TINYTEXT opt_binary opt_csc
   | TEXT opt_binary opt_csc
   | MEDIUMTEXT opt_binary opt_csc
   | LONGTEXT opt_binary opt_csc
   | ENUM '(' enum_list ')' opt_csc
   | SET '(' enum_list ')' opt_csc
   ;

enum_list: string_literal
   | enum_list COMMA string_literal
   ;

create_select_statement: opt_ignore_replace opt_as select_stmt
   ;

opt_ignore_replace: /* nil */
   | IGNORE
   | REPLACE
   ;

opt_temporary:   /* nil */
   | TEMPORARY
   ;

/**** set user variables ****/
set_stmt: SET set_list ;

set_list: set_expr | set_list COMMA set_expr ;

set_expr:
      USERVAR COMPARISON expr
    | USERVAR ASSIGN expr
    ;

/**** expressions ****/

expr_list:
     expr
   | expr_list COMMA expr
   ;

opt_udf_expr_list:
   | udf_expr_list
   ;

udf_expr_list:
     udf_expr
   | udf_expr_list COMMA udf_expr
   ;

udf_expr:
     expr opt_alias
   ;

ident:
     IDENT ('.' IDENT)*
   | BQUOTA_STRING
   | unreserved_keyword
   ;

expr:
     NOT expr
   | EXCLAMATION expr
   | expr AND expr
   | expr XOR expr
   | expr OR expr
   | expr TYPECAST cast_type
   | predicate IS NOT BOOL
   | predicate IS BOOL
   | predicate
   ;

predicate:
     predicate IN '(' expr_list ')'
   | predicate NOT IN '(' expr_list ')'
   | predicate IN '(' select_stmt ')'
   | predicate NOT IN '(' select_stmt ')'
   | predicate IS NULLX
   | predicate IS NOT NULLX
   | predicate COMPARISON predicate
   | predicate COMPARISON ANY '(' select_stmt ')'
   | predicate COMPARISON SOME '(' select_stmt ')'
   | predicate COMPARISON ALL '(' select_stmt ')'
   | predicate BETWEEN predicate AND predicate
   | predicate NOT BETWEEN predicate AND predicate
   | predicate SOUNDS LIKE predicate
   | predicate LIKE predicate opt_escape
   | predicate NOT LIKE predicate opt_escape
   | predicate REGEXP predicate
   | predicate NOT REGEXP predicate
   | USERVAR ASSIGN expressionAtom
   | expressionAtom
   ;

opt_escape:
   | ESCAPE string_literal
   ;

expressionAtom:
     constant
   | fullColumnName
   | functionCall
   | expressionAtom COLLATE collationName
   | USERVAR
   | expressionAtom BIT_AND expressionAtom
   | expressionAtom BIT_OR expressionAtom
   | expressionAtom BIT_XOR expressionAtom
   | expressionAtom SHIFT expressionAtom
   | expressionAtom PLUS expressionAtom
   | expressionAtom MINUS expressionAtom
   | expressionAtom STAR expressionAtom
   | expressionAtom DIVIDE expressionAtom
   | expressionAtom MODULE expressionAtom
   | expressionAtom MOD expressionAtom
   | expressionAtom DIV expressionAtom
   | MINUS expressionAtom
   | PLUS expressionAtom
   | BIT_NOT expressionAtom
   | BINARY expressionAtom
   | '(' expr_list ')'
   | '(' select_stmt ')'
   | INTERVAL expr interval
   ;

constant:
     stringLiteral
   | NUM
   | hexadecimalLiteral
   | bitValueLiteral
   | NULLX
   | BOOL
   | STAR
   ;

fullColumnName: ident ('.' ident)* ;

hexadecimalLiteral:
     HEX_STRING
   | '_' charsetNameBase HEX_STRING
   ;

bitValueLiteral:
     BIT_STRING
   | '_' charsetNameBase BIT_STRING
   ;

stringLiteral:
     string_literal_list
   | string_literal COLLATE collationName
   | START_NATIONAL_STRING_LITERAL
   | START_NATIONAL_STRING_LITERAL string_literal_list
   | START_NATIONAL_STRING_LITERAL COLLATE collationName
   | stringCharsetName string_literal_list
   | stringCharsetName string_literal COLLATE collationName
   ;

stringCharsetName:
          '_' charsetNameBase
        ;

string_literal_list:
     string_literal_list string_literal
   | string_literal
   ;

collationName:
     ident
   | string_literal
   ;

reserved_keyword:
      ALL
    | AND
    | AS
    | ASC
    | BETWEEN
    | BIGINT
    | BINARY
    | BLOB
    | BOTH
    | BY
    | CASE
    | CHAR
    | COLLATE
    | CONVERT
    | CREATE
    | CROSS
    | DATABASE
    | DAY_HOUR
    | DAY_MICROSECOND
    | DAY_MINUTE
    | DAY_SECOND
    | DECIMAL
    | DEFAULT
    | DELAYED
    | DELETE
    | DESC
    | DISTINCT
    | DISTINCTROW
    | DIV
    | DOUBLE
    | ELSE
    | ENCLOSED
    | ESCAPED
    | EXISTS
    | FLOAT
    | FOR
    | FORCE
    | FROM
    | FULLTEXT
    | GROUP
    | HAVING
    | HIGH_PRIORITY
    | HOUR_MICROSECOND
    | HOUR_MINUTE
    | HOUR_SECOND
    | IF
    | IGNORE
    | IN
    | INDEX
    | INNER
    | INSERT
    | INTEGER
    | INTERVAL
    | INTO
    | JOIN
    | KEY
    | LEADING
    | LEFT
    | LIKE
    | LIMIT
    | LINES
    | LOCK
    | LONGBLOB
    | LONGTEXT
    | LOW_PRIORITY
    | MEDIUMBLOB
    | MEDIUMINT
    | MEDIUMTEXT
    | MINUTE_MICROSECOND
    | MINUTE_SECOND
    | MOD
    | NATURAL
    | NOT
    | NULLX
    | ON
    | OPTIONALLY
    | OR
    | ORDER
    | OUTER
    | OUTFILE
    | PRIMARY
    | REAL
    | REGEXP
    | REPLACE
    | RIGHT
    | ROW
    | SCHEMA
    | SECOND_MICROSECOND
    | SELECT
    | SET
    | SMALLINT
    | SQL_BIG_RESULT
    | SQL_CALC_FOUND_ROWS
    | SQL_SMALL_RESULT
    | STARTING
    | STRAIGHT_JOIN
    | TABLE
    | TERMINATED
    | THEN
    | TINYBLOB
    | TINYINT
    | TINYTEXT
    | TRAILING
    | UNION
    | UNIQUE
    | UPDATE
    | USE
    | USING
    | VALUES
    | VARBINARY
    | VARCHAR
    | WHEN
    | WHERE
    | XOR
    | YEAR_MONTH
    | ZEROFILL
    ;

unreserved_keyword:
      ANY
    | AUTO_INCREMENT
    | BIT
    | BOOLEAN
    | COMMENT
    | COUNT
    | DATE
    | DATETIME
    | DAY
    | DUMPFILE
    | END
    | ENUM
    | ESCAPE
    | FIELDS
    | HOUR
    | MICROSECOND
    | MINUTE
    | MODE
    | MONTH
    | NCHAR
    | OFFSET
    | ONDUPLICATE /**/
    | PARTITION
    | POSITION /**/
    | QUARTER
    | QUICK
    | SECOND
    | SHARE
    | SIGNED
    | SOME
    | SOUNDS
    | SUBSTRING
    | TEMPORARY
    | TEXT
    | TIME
    | TIMESTAMP
    | TRIM
    | UNICODE
    | UNSIGNED
    | WEEK
    | YEAR
    ;

interval:
     DAY_HOUR
   | DAY_MICROSECOND
   | DAY_MINUTE
   | DAY_SECOND
   | HOUR_MICROSECOND
   | HOUR_MINUTE
   | HOUR_SECOND
   | MINUTE_MICROSECOND
   | MINUTE_SECOND
   | SECOND_MICROSECOND
   | YEAR_MONTH
   | DAY
   | WEEK
   | HOUR
   | MINUTE
   | MONTH
   | QUARTER
   | SECOND
   | MICROSECOND
   | YEAR
   ;

functionCall:
     function_call_specific  
   | function_call_generic  
   ;

function_call_generic:
     ident '(' opt_udf_expr_list ')'
   | ident ('.' ident)* '(' opt_expr_list ')'
   | function_name '(' opt_expr_list ')'
   | SYSVAR
   ;

function_name:
     IF
   | LIKE
   | ASCII
   ;

opt_expr_list: /* empty */
        | expr_list
        ;

function_call_specific:
     CAST '(' expr AS cast_type ')'
   | CASE opt_expr when_list opt_else END
   | CONVERT '(' expr COMMA cast_type ')'
   | CONVERT '(' expr USING charset_name ')'
   | CONVERT '(' INTEGER COMMA expr ')'
   | CHAR '(' expr_list ')'
   | CHAR '(' expr_list USING charset_name ')'
   | COUNT '(' STAR ')'
   | COUNT '(' ALL STAR ')'
   | COUNT '(' expr ')'
   | COUNT '(' ALL expr ')'
   | COUNT '(' DISTINCT expr_list ')'
   | DATABASE '(' ')'
   | EXISTS '(' select_stmt ')'
   | EXTRACT '(' interval FROM expr ')'
   | POSITION '(' expr IN expr ')'
   | ROW '(' expr COMMA expr_list ')'
   | SUBSTRING '(' expr COMMA expr COMMA expr ')'
   | SUBSTRING '(' expr COMMA expr ')'
   | SUBSTRING '(' expr FROM expr FOR expr ')'
   | SUBSTRING '(' expr FROM expr ')'
   | TRIM '(' expr ')'
   | TRIM '(' BOTH expr FROM expr ')'
   | TRIM '(' LEADING expr FROM expr ')'
   | TRIM '(' TRAILING expr FROM expr ')'
   | TRIM '(' BOTH FROM expr ')'
   | TRIM '(' LEADING FROM expr ')'
   | TRIM '(' TRAILING FROM expr ')'
   | TRIM '(' expr FROM expr ')'
   | WEIGHT_STRING '(' expr ')'
   | WEIGHT_STRING '(' expr AS CHAR '(' NUM ')' ')'
   | WEIGHT_STRING '(' expr AS BINARY '(' NUM ')' ')'
   | WEIGHT_STRING '(' expr COMMA NUM COMMA NUM COMMA NUM ')'
   ;

opt_expr: /* empty */
   | expr
   ;

when_list:
     WHEN expr THEN expr
   | when_list WHEN expr THEN expr
   ;

opt_else: /* empty */
   | ELSE expr
   ;

cast_type:
     BINARY field_length
   | NCHAR field_length
   | CHAR field_length opt_charset_with_opt_binary
   | VARCHAR field_length
   | SIGNED INTEGER
   | UNSIGNED INTEGER
   | DECIMAL opt_float_options
   | ident
   ;

opt_charset_with_opt_binary: /* empty */
   | ASCII
   | UNICODE
   | character_set charset_name
   ;

charset_name:
     BINARY
   | charsetNameBase
   | string_literal
   | '`' charsetNameBase '`'
   ;

string_literal:
    QUOTA_STRING
    | DOUBLE_QUOTA_STRING
    | QUOTA_STRING IN BOOLEAN MODE
    | DOUBLE_QUOTA_STRING IN BOOLEAN MODE
   ;

charsetNameBase:
     ARMSCII8 | ASCII | BIG5  | CP1250
   | CP1251 | CP1256 | CP1257 | CP850
   | CP852 | CP866 | CP932 | DEC8 | EUCJPMS
   | EUCKR | GB2312 | GBK | GEOSTD8 | GREEK
   | HEBREW | HP8 | KEYBCS2 | KOI8R | KOI8U
   | LATIN1 | LATIN2 | LATIN5 | LATIN7
   | MACCE | MACROMAN | SJIS | SWE7 | TIS620
   | UCS2 | UJIS | UTF16 | UTF16LE | UTF32
   | UTF8 | UTF8MB3 | UTF8MB4
   ;

character_set:
     CHAR SET
   ;

precision:
     '(' NUM COMMA NUM ')'
   ;

field_length:
     '(' NUM ')'
   ;

opt_float_options:
   | field_length
   | precision
   ;