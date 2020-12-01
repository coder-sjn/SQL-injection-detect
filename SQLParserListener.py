# Generated from SQLParser.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQLParser import SQLParser
else:
    from SQLParser import SQLParser

# This class defines a complete listener for a parse tree produced by SQLParser.
class SQLParserListener(ParseTreeListener):
    def __init__(self, output_list):
        self.output_list = output_list
        self.score = 0

    # Enter a parse tree produced by SQLParser#prog.
    def enterProg(self, ctx:SQLParser.ProgContext):
        pass

    # Exit a parse tree produced by SQLParser#prog.
    def exitProg(self, ctx:SQLParser.ProgContext):
        pass


    # Enter a parse tree produced by SQLParser#stmt_list.
    def enterStmt_list(self, ctx:SQLParser.Stmt_listContext):
        pass

    # Exit a parse tree produced by SQLParser#stmt_list.
    def exitStmt_list(self, ctx:SQLParser.Stmt_listContext):
        pass


    # Enter a parse tree produced by SQLParser#stmt.
    def enterStmt(self, ctx:SQLParser.StmtContext):
        self.output_list.append("stmt")

    # Exit a parse tree produced by SQLParser#stmt.
    def exitStmt(self, ctx:SQLParser.StmtContext):
        pass


    # Enter a parse tree produced by SQLParser#select_stmt.
    def enterSelect_stmt(self, ctx:SQLParser.Select_stmtContext):
        self.score += 1

    # Exit a parse tree produced by SQLParser#select_stmt.
    def exitSelect_stmt(self, ctx:SQLParser.Select_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#query_expression_parens.
    def enterQuery_expression_parens(self, ctx:SQLParser.Query_expression_parensContext):
        pass

    # Exit a parse tree produced by SQLParser#query_expression_parens.
    def exitQuery_expression_parens(self, ctx:SQLParser.Query_expression_parensContext):
        pass


    # Enter a parse tree produced by SQLParser#query_expression.
    def enterQuery_expression(self, ctx:SQLParser.Query_expressionContext):
        pass

    # Exit a parse tree produced by SQLParser#query_expression.
    def exitQuery_expression(self, ctx:SQLParser.Query_expressionContext):
        pass


    # Enter a parse tree produced by SQLParser#query_expression_body.
    def enterQuery_expression_body(self, ctx:SQLParser.Query_expression_bodyContext):
        pass

    # Exit a parse tree produced by SQLParser#query_expression_body.
    def exitQuery_expression_body(self, ctx:SQLParser.Query_expression_bodyContext):
        pass


    # Enter a parse tree produced by SQLParser#union_select_stmt.
    def enterUnion_select_stmt(self, ctx:SQLParser.Union_select_stmtContext):
        pass

    # Exit a parse tree produced by SQLParser#union_select_stmt.
    def exitUnion_select_stmt(self, ctx:SQLParser.Union_select_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_locking_clause.
    def enterOpt_locking_clause(self, ctx:SQLParser.Opt_locking_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_locking_clause.
    def exitOpt_locking_clause(self, ctx:SQLParser.Opt_locking_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#locking_clause.
    def enterLocking_clause(self, ctx:SQLParser.Locking_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#locking_clause.
    def exitLocking_clause(self, ctx:SQLParser.Locking_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#union_option.
    def enterUnion_option(self, ctx:SQLParser.Union_optionContext):
        pass

    # Exit a parse tree produced by SQLParser#union_option.
    def exitUnion_option(self, ctx:SQLParser.Union_optionContext):
        pass


    # Enter a parse tree produced by SQLParser#query_specification.
    def enterQuery_specification(self, ctx:SQLParser.Query_specificationContext):
        pass

    # Exit a parse tree produced by SQLParser#query_specification.
    def exitQuery_specification(self, ctx:SQLParser.Query_specificationContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_from_clause.
    def enterOpt_from_clause(self, ctx:SQLParser.Opt_from_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_from_clause.
    def exitOpt_from_clause(self, ctx:SQLParser.Opt_from_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#from_clause.
    def enterFrom_clause(self, ctx:SQLParser.From_clauseContext):
        self.output_list.append("from_clause")
        self.score += 1

    # Exit a parse tree produced by SQLParser#from_clause.
    def exitFrom_clause(self, ctx:SQLParser.From_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_where_clause.
    def enterOpt_where_clause(self, ctx:SQLParser.Opt_where_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_where_clause.
    def exitOpt_where_clause(self, ctx:SQLParser.Opt_where_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#where_clause.
    def enterWhere_clause(self, ctx:SQLParser.Where_clauseContext):
        self.output_list.append("where_clause")
        self.score += 1

    # Exit a parse tree produced by SQLParser#where_clause.
    def exitWhere_clause(self, ctx:SQLParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_group_clause.
    def enterOpt_group_clause(self, ctx:SQLParser.Opt_group_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_group_clause.
    def exitOpt_group_clause(self, ctx:SQLParser.Opt_group_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#group_clause.
    def enterGroup_clause(self, ctx:SQLParser.Group_clauseContext):
        self.output_list.append("group_clause")
        self.score += 1

    # Exit a parse tree produced by SQLParser#group_clause.
    def exitGroup_clause(self, ctx:SQLParser.Group_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_having_clause.
    def enterOpt_having_clause(self, ctx:SQLParser.Opt_having_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_having_clause.
    def exitOpt_having_clause(self, ctx:SQLParser.Opt_having_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#having_clause.
    def enterHaving_clause(self, ctx:SQLParser.Having_clauseContext):
        self.output_list.append("having_clause")
        self.score += 2

    # Exit a parse tree produced by SQLParser#having_clause.
    def exitHaving_clause(self, ctx:SQLParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_order_clause.
    def enterOpt_order_clause(self, ctx:SQLParser.Opt_order_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_order_clause.
    def exitOpt_order_clause(self, ctx:SQLParser.Opt_order_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#order_clause.
    def enterOrder_clause(self, ctx:SQLParser.Order_clauseContext):
        self.output_list.append("order_clause")
        self.score += 2

    # Exit a parse tree produced by SQLParser#order_clause.
    def exitOrder_clause(self, ctx:SQLParser.Order_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_limit_clause.
    def enterOpt_limit_clause(self, ctx:SQLParser.Opt_limit_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_limit_clause.
    def exitOpt_limit_clause(self, ctx:SQLParser.Opt_limit_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#limit_clause.
    def enterLimit_clause(self, ctx:SQLParser.Limit_clauseContext):
        self.output_list.append("limit_clause")
        self.score += 1

    # Exit a parse tree produced by SQLParser#limit_clause.
    def exitLimit_clause(self, ctx:SQLParser.Limit_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#group_list.
    def enterGroup_list(self, ctx:SQLParser.Group_listContext):
        pass

    # Exit a parse tree produced by SQLParser#group_list.
    def exitGroup_list(self, ctx:SQLParser.Group_listContext):
        pass


    # Enter a parse tree produced by SQLParser#order_list.
    def enterOrder_list(self, ctx:SQLParser.Order_listContext):
        pass

    # Exit a parse tree produced by SQLParser#order_list.
    def exitOrder_list(self, ctx:SQLParser.Order_listContext):
        pass


    # Enter a parse tree produced by SQLParser#order_expr.
    def enterOrder_expr(self, ctx:SQLParser.Order_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#order_expr.
    def exitOrder_expr(self, ctx:SQLParser.Order_exprContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_ordering_direction.
    def enterOpt_ordering_direction(self, ctx:SQLParser.Opt_ordering_directionContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_ordering_direction.
    def exitOpt_ordering_direction(self, ctx:SQLParser.Opt_ordering_directionContext):
        pass


    # Enter a parse tree produced by SQLParser#limit_options.
    def enterLimit_options(self, ctx:SQLParser.Limit_optionsContext):
        pass

    # Exit a parse tree produced by SQLParser#limit_options.
    def exitLimit_options(self, ctx:SQLParser.Limit_optionsContext):
        pass


    # Enter a parse tree produced by SQLParser#limit_option.
    def enterLimit_option(self, ctx:SQLParser.Limit_optionContext):
        pass

    # Exit a parse tree produced by SQLParser#limit_option.
    def exitLimit_option(self, ctx:SQLParser.Limit_optionContext):
        pass


    # Enter a parse tree produced by SQLParser#select_item_list.
    def enterSelect_item_list(self, ctx:SQLParser.Select_item_listContext):
        pass

    # Exit a parse tree produced by SQLParser#select_item_list.
    def exitSelect_item_list(self, ctx:SQLParser.Select_item_listContext):
        pass


    # Enter a parse tree produced by SQLParser#select_item.
    def enterSelect_item(self, ctx:SQLParser.Select_itemContext):
        pass

    # Exit a parse tree produced by SQLParser#select_item.
    def exitSelect_item(self, ctx:SQLParser.Select_itemContext):
        pass


    # Enter a parse tree produced by SQLParser#collabel.
    def enterCollabel(self, ctx:SQLParser.CollabelContext):
        pass

    # Exit a parse tree produced by SQLParser#collabel.
    def exitCollabel(self, ctx:SQLParser.CollabelContext):
        pass


    # Enter a parse tree produced by SQLParser#table_wild.
    def enterTable_wild(self, ctx:SQLParser.Table_wildContext):
        pass

    # Exit a parse tree produced by SQLParser#table_wild.
    def exitTable_wild(self, ctx:SQLParser.Table_wildContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_alias.
    def enterOpt_alias(self, ctx:SQLParser.Opt_aliasContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_alias.
    def exitOpt_alias(self, ctx:SQLParser.Opt_aliasContext):
        pass


    # Enter a parse tree produced by SQLParser#into_clause.
    def enterInto_clause(self, ctx:SQLParser.Into_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#into_clause.
    def exitInto_clause(self, ctx:SQLParser.Into_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#into_destination.
    def enterInto_destination(self, ctx:SQLParser.Into_destinationContext):
        pass

    # Exit a parse tree produced by SQLParser#into_destination.
    def exitInto_destination(self, ctx:SQLParser.Into_destinationContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_load_data_charset.
    def enterOpt_load_data_charset(self, ctx:SQLParser.Opt_load_data_charsetContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_load_data_charset.
    def exitOpt_load_data_charset(self, ctx:SQLParser.Opt_load_data_charsetContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_field_term.
    def enterOpt_field_term(self, ctx:SQLParser.Opt_field_termContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_field_term.
    def exitOpt_field_term(self, ctx:SQLParser.Opt_field_termContext):
        pass


    # Enter a parse tree produced by SQLParser#field_term_list.
    def enterField_term_list(self, ctx:SQLParser.Field_term_listContext):
        pass

    # Exit a parse tree produced by SQLParser#field_term_list.
    def exitField_term_list(self, ctx:SQLParser.Field_term_listContext):
        pass


    # Enter a parse tree produced by SQLParser#field_term.
    def enterField_term(self, ctx:SQLParser.Field_termContext):
        pass

    # Exit a parse tree produced by SQLParser#field_term.
    def exitField_term(self, ctx:SQLParser.Field_termContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_line_term.
    def enterOpt_line_term(self, ctx:SQLParser.Opt_line_termContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_line_term.
    def exitOpt_line_term(self, ctx:SQLParser.Opt_line_termContext):
        pass


    # Enter a parse tree produced by SQLParser#line_term_list.
    def enterLine_term_list(self, ctx:SQLParser.Line_term_listContext):
        pass

    # Exit a parse tree produced by SQLParser#line_term_list.
    def exitLine_term_list(self, ctx:SQLParser.Line_term_listContext):
        pass


    # Enter a parse tree produced by SQLParser#line_term.
    def enterLine_term(self, ctx:SQLParser.Line_termContext):
        pass

    # Exit a parse tree produced by SQLParser#line_term.
    def exitLine_term(self, ctx:SQLParser.Line_termContext):
        pass


    # Enter a parse tree produced by SQLParser#select_var_list.
    def enterSelect_var_list(self, ctx:SQLParser.Select_var_listContext):
        pass

    # Exit a parse tree produced by SQLParser#select_var_list.
    def exitSelect_var_list(self, ctx:SQLParser.Select_var_listContext):
        pass


    # Enter a parse tree produced by SQLParser#select_var_ident.
    def enterSelect_var_ident(self, ctx:SQLParser.Select_var_identContext):
        pass

    # Exit a parse tree produced by SQLParser#select_var_ident.
    def exitSelect_var_ident(self, ctx:SQLParser.Select_var_identContext):
        pass


    # Enter a parse tree produced by SQLParser#ident_or_text.
    def enterIdent_or_text(self, ctx:SQLParser.Ident_or_textContext):
        pass

    # Exit a parse tree produced by SQLParser#ident_or_text.
    def exitIdent_or_text(self, ctx:SQLParser.Ident_or_textContext):
        pass


    # Enter a parse tree produced by SQLParser#column_list.
    def enterColumn_list(self, ctx:SQLParser.Column_listContext):
        pass

    # Exit a parse tree produced by SQLParser#column_list.
    def exitColumn_list(self, ctx:SQLParser.Column_listContext):
        pass


    # Enter a parse tree produced by SQLParser#select_opts.
    def enterSelect_opts(self, ctx:SQLParser.Select_optsContext):
        pass

    # Exit a parse tree produced by SQLParser#select_opts.
    def exitSelect_opts(self, ctx:SQLParser.Select_optsContext):
        pass


    # Enter a parse tree produced by SQLParser#esc_table_reference.
    def enterEsc_table_reference(self, ctx:SQLParser.Esc_table_referenceContext):
        pass

    # Exit a parse tree produced by SQLParser#esc_table_reference.
    def exitEsc_table_reference(self, ctx:SQLParser.Esc_table_referenceContext):
        pass


    # Enter a parse tree produced by SQLParser#table_reference.
    def enterTable_reference(self, ctx:SQLParser.Table_referenceContext):
        pass

    # Exit a parse tree produced by SQLParser#table_reference.
    def exitTable_reference(self, ctx:SQLParser.Table_referenceContext):
        pass


    # Enter a parse tree produced by SQLParser#table_factor.
    def enterTable_factor(self, ctx:SQLParser.Table_factorContext):
        pass

    # Exit a parse tree produced by SQLParser#table_factor.
    def exitTable_factor(self, ctx:SQLParser.Table_factorContext):
        pass


    # Enter a parse tree produced by SQLParser#joined_table_parens.
    def enterJoined_table_parens(self, ctx:SQLParser.Joined_table_parensContext):
        pass

    # Exit a parse tree produced by SQLParser#joined_table_parens.
    def exitJoined_table_parens(self, ctx:SQLParser.Joined_table_parensContext):
        pass


    # Enter a parse tree produced by SQLParser#table_reference_list_parens.
    def enterTable_reference_list_parens(self, ctx:SQLParser.Table_reference_list_parensContext):
        pass

    # Exit a parse tree produced by SQLParser#table_reference_list_parens.
    def exitTable_reference_list_parens(self, ctx:SQLParser.Table_reference_list_parensContext):
        pass


    # Enter a parse tree produced by SQLParser#table_reference_list.
    def enterTable_reference_list(self, ctx:SQLParser.Table_reference_listContext):
        pass

    # Exit a parse tree produced by SQLParser#table_reference_list.
    def exitTable_reference_list(self, ctx:SQLParser.Table_reference_listContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_derived_column_list.
    def enterOpt_derived_column_list(self, ctx:SQLParser.Opt_derived_column_listContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_derived_column_list.
    def exitOpt_derived_column_list(self, ctx:SQLParser.Opt_derived_column_listContext):
        pass


    # Enter a parse tree produced by SQLParser#single_table_parens.
    def enterSingle_table_parens(self, ctx:SQLParser.Single_table_parensContext):
        pass

    # Exit a parse tree produced by SQLParser#single_table_parens.
    def exitSingle_table_parens(self, ctx:SQLParser.Single_table_parensContext):
        pass


    # Enter a parse tree produced by SQLParser#single_table.
    def enterSingle_table(self, ctx:SQLParser.Single_tableContext):
        pass

    # Exit a parse tree produced by SQLParser#single_table.
    def exitSingle_table(self, ctx:SQLParser.Single_tableContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_table_alias.
    def enterOpt_table_alias(self, ctx:SQLParser.Opt_table_aliasContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_table_alias.
    def exitOpt_table_alias(self, ctx:SQLParser.Opt_table_aliasContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_as.
    def enterOpt_as(self, ctx:SQLParser.Opt_asContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_as.
    def exitOpt_as(self, ctx:SQLParser.Opt_asContext):
        pass


    # Enter a parse tree produced by SQLParser#index_hints_list.
    def enterIndex_hints_list(self, ctx:SQLParser.Index_hints_listContext):
        pass

    # Exit a parse tree produced by SQLParser#index_hints_list.
    def exitIndex_hints_list(self, ctx:SQLParser.Index_hints_listContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_index_hints_list.
    def enterOpt_index_hints_list(self, ctx:SQLParser.Opt_index_hints_listContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_index_hints_list.
    def exitOpt_index_hints_list(self, ctx:SQLParser.Opt_index_hints_listContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_use_partition.
    def enterOpt_use_partition(self, ctx:SQLParser.Opt_use_partitionContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_use_partition.
    def exitOpt_use_partition(self, ctx:SQLParser.Opt_use_partitionContext):
        pass


    # Enter a parse tree produced by SQLParser#use_partition.
    def enterUse_partition(self, ctx:SQLParser.Use_partitionContext):
        pass

    # Exit a parse tree produced by SQLParser#use_partition.
    def exitUse_partition(self, ctx:SQLParser.Use_partitionContext):
        pass


    # Enter a parse tree produced by SQLParser#joined_table.
    def enterJoined_table(self, ctx:SQLParser.Joined_tableContext):
        pass

    # Exit a parse tree produced by SQLParser#joined_table.
    def exitJoined_table(self, ctx:SQLParser.Joined_tableContext):
        pass


    # Enter a parse tree produced by SQLParser#tbl_name.
    def enterTbl_name(self, ctx:SQLParser.Tbl_nameContext):
        pass

    # Exit a parse tree produced by SQLParser#tbl_name.
    def exitTbl_name(self, ctx:SQLParser.Tbl_nameContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_inner_cross.
    def enterOpt_inner_cross(self, ctx:SQLParser.Opt_inner_crossContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_inner_cross.
    def exitOpt_inner_cross(self, ctx:SQLParser.Opt_inner_crossContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_outer.
    def enterOpt_outer(self, ctx:SQLParser.Opt_outerContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_outer.
    def exitOpt_outer(self, ctx:SQLParser.Opt_outerContext):
        pass


    # Enter a parse tree produced by SQLParser#left_or_right.
    def enterLeft_or_right(self, ctx:SQLParser.Left_or_rightContext):
        pass

    # Exit a parse tree produced by SQLParser#left_or_right.
    def exitLeft_or_right(self, ctx:SQLParser.Left_or_rightContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_left_or_right_outer.
    def enterOpt_left_or_right_outer(self, ctx:SQLParser.Opt_left_or_right_outerContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_left_or_right_outer.
    def exitOpt_left_or_right_outer(self, ctx:SQLParser.Opt_left_or_right_outerContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_join_condition.
    def enterOpt_join_condition(self, ctx:SQLParser.Opt_join_conditionContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_join_condition.
    def exitOpt_join_condition(self, ctx:SQLParser.Opt_join_conditionContext):
        pass


    # Enter a parse tree produced by SQLParser#join_condition.
    def enterJoin_condition(self, ctx:SQLParser.Join_conditionContext):
        pass

    # Exit a parse tree produced by SQLParser#join_condition.
    def exitJoin_condition(self, ctx:SQLParser.Join_conditionContext):
        pass


    # Enter a parse tree produced by SQLParser#index_hint.
    def enterIndex_hint(self, ctx:SQLParser.Index_hintContext):
        pass

    # Exit a parse tree produced by SQLParser#index_hint.
    def exitIndex_hint(self, ctx:SQLParser.Index_hintContext):
        pass


    # Enter a parse tree produced by SQLParser#key_or_index.
    def enterKey_or_index(self, ctx:SQLParser.Key_or_indexContext):
        pass

    # Exit a parse tree produced by SQLParser#key_or_index.
    def exitKey_or_index(self, ctx:SQLParser.Key_or_indexContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_index_hint_clause.
    def enterOpt_index_hint_clause(self, ctx:SQLParser.Opt_index_hint_clauseContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_index_hint_clause.
    def exitOpt_index_hint_clause(self, ctx:SQLParser.Opt_index_hint_clauseContext):
        pass


    # Enter a parse tree produced by SQLParser#index_list.
    def enterIndex_list(self, ctx:SQLParser.Index_listContext):
        pass

    # Exit a parse tree produced by SQLParser#index_list.
    def exitIndex_list(self, ctx:SQLParser.Index_listContext):
        pass


    # Enter a parse tree produced by SQLParser#table_subquery.
    def enterTable_subquery(self, ctx:SQLParser.Table_subqueryContext):
        pass

    # Exit a parse tree produced by SQLParser#table_subquery.
    def exitTable_subquery(self, ctx:SQLParser.Table_subqueryContext):
        pass


    # Enter a parse tree produced by SQLParser#delete_stmt.
    def enterDelete_stmt(self, ctx:SQLParser.Delete_stmtContext):
        pass

    # Exit a parse tree produced by SQLParser#delete_stmt.
    def exitDelete_stmt(self, ctx:SQLParser.Delete_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#delete_opts.
    def enterDelete_opts(self, ctx:SQLParser.Delete_optsContext):
        pass

    # Exit a parse tree produced by SQLParser#delete_opts.
    def exitDelete_opts(self, ctx:SQLParser.Delete_optsContext):
        pass


    # Enter a parse tree produced by SQLParser#delete_list.
    def enterDelete_list(self, ctx:SQLParser.Delete_listContext):
        pass

    # Exit a parse tree produced by SQLParser#delete_list.
    def exitDelete_list(self, ctx:SQLParser.Delete_listContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_dot_star.
    def enterOpt_dot_star(self, ctx:SQLParser.Opt_dot_starContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_dot_star.
    def exitOpt_dot_star(self, ctx:SQLParser.Opt_dot_starContext):
        pass


    # Enter a parse tree produced by SQLParser#drop_stmt.
    def enterDrop_stmt(self, ctx:SQLParser.Drop_stmtContext):
        pass

    # Exit a parse tree produced by SQLParser#drop_stmt.
    def exitDrop_stmt(self, ctx:SQLParser.Drop_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#insert_stmt.
    def enterInsert_stmt(self, ctx:SQLParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by SQLParser#insert_stmt.
    def exitInsert_stmt(self, ctx:SQLParser.Insert_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_ondupupdate.
    def enterOpt_ondupupdate(self, ctx:SQLParser.Opt_ondupupdateContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_ondupupdate.
    def exitOpt_ondupupdate(self, ctx:SQLParser.Opt_ondupupdateContext):
        pass


    # Enter a parse tree produced by SQLParser#insert_opts.
    def enterInsert_opts(self, ctx:SQLParser.Insert_optsContext):
        pass

    # Exit a parse tree produced by SQLParser#insert_opts.
    def exitInsert_opts(self, ctx:SQLParser.Insert_optsContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_into.
    def enterOpt_into(self, ctx:SQLParser.Opt_intoContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_into.
    def exitOpt_into(self, ctx:SQLParser.Opt_intoContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_col_names.
    def enterOpt_col_names(self, ctx:SQLParser.Opt_col_namesContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_col_names.
    def exitOpt_col_names(self, ctx:SQLParser.Opt_col_namesContext):
        pass


    # Enter a parse tree produced by SQLParser#insert_vals_list.
    def enterInsert_vals_list(self, ctx:SQLParser.Insert_vals_listContext):
        pass

    # Exit a parse tree produced by SQLParser#insert_vals_list.
    def exitInsert_vals_list(self, ctx:SQLParser.Insert_vals_listContext):
        pass


    # Enter a parse tree produced by SQLParser#insert_vals.
    def enterInsert_vals(self, ctx:SQLParser.Insert_valsContext):
        pass

    # Exit a parse tree produced by SQLParser#insert_vals.
    def exitInsert_vals(self, ctx:SQLParser.Insert_valsContext):
        pass


    # Enter a parse tree produced by SQLParser#insert_asgn_list.
    def enterInsert_asgn_list(self, ctx:SQLParser.Insert_asgn_listContext):
        pass

    # Exit a parse tree produced by SQLParser#insert_asgn_list.
    def exitInsert_asgn_list(self, ctx:SQLParser.Insert_asgn_listContext):
        pass


    # Enter a parse tree produced by SQLParser#replace_stmt.
    def enterReplace_stmt(self, ctx:SQLParser.Replace_stmtContext):
        pass

    # Exit a parse tree produced by SQLParser#replace_stmt.
    def exitReplace_stmt(self, ctx:SQLParser.Replace_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#update_stmt.
    def enterUpdate_stmt(self, ctx:SQLParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by SQLParser#update_stmt.
    def exitUpdate_stmt(self, ctx:SQLParser.Update_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#update_opts.
    def enterUpdate_opts(self, ctx:SQLParser.Update_optsContext):
        pass

    # Exit a parse tree produced by SQLParser#update_opts.
    def exitUpdate_opts(self, ctx:SQLParser.Update_optsContext):
        pass


    # Enter a parse tree produced by SQLParser#update_asgn_list.
    def enterUpdate_asgn_list(self, ctx:SQLParser.Update_asgn_listContext):
        pass

    # Exit a parse tree produced by SQLParser#update_asgn_list.
    def exitUpdate_asgn_list(self, ctx:SQLParser.Update_asgn_listContext):
        pass


    # Enter a parse tree produced by SQLParser#create_database_stmt.
    def enterCreate_database_stmt(self, ctx:SQLParser.Create_database_stmtContext):
        pass

    # Exit a parse tree produced by SQLParser#create_database_stmt.
    def exitCreate_database_stmt(self, ctx:SQLParser.Create_database_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_if_not_exists.
    def enterOpt_if_not_exists(self, ctx:SQLParser.Opt_if_not_existsContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_if_not_exists.
    def exitOpt_if_not_exists(self, ctx:SQLParser.Opt_if_not_existsContext):
        pass


    # Enter a parse tree produced by SQLParser#create_table_stmt.
    def enterCreate_table_stmt(self, ctx:SQLParser.Create_table_stmtContext):
        pass

    # Exit a parse tree produced by SQLParser#create_table_stmt.
    def exitCreate_table_stmt(self, ctx:SQLParser.Create_table_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#create_col_list.
    def enterCreate_col_list(self, ctx:SQLParser.Create_col_listContext):
        pass

    # Exit a parse tree produced by SQLParser#create_col_list.
    def exitCreate_col_list(self, ctx:SQLParser.Create_col_listContext):
        pass


    # Enter a parse tree produced by SQLParser#create_definition.
    def enterCreate_definition(self, ctx:SQLParser.Create_definitionContext):
        pass

    # Exit a parse tree produced by SQLParser#create_definition.
    def exitCreate_definition(self, ctx:SQLParser.Create_definitionContext):
        pass


    # Enter a parse tree produced by SQLParser#column_atts.
    def enterColumn_atts(self, ctx:SQLParser.Column_attsContext):
        pass

    # Exit a parse tree produced by SQLParser#column_atts.
    def exitColumn_atts(self, ctx:SQLParser.Column_attsContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_length.
    def enterOpt_length(self, ctx:SQLParser.Opt_lengthContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_length.
    def exitOpt_length(self, ctx:SQLParser.Opt_lengthContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_binary.
    def enterOpt_binary(self, ctx:SQLParser.Opt_binaryContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_binary.
    def exitOpt_binary(self, ctx:SQLParser.Opt_binaryContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_uz.
    def enterOpt_uz(self, ctx:SQLParser.Opt_uzContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_uz.
    def exitOpt_uz(self, ctx:SQLParser.Opt_uzContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_csc.
    def enterOpt_csc(self, ctx:SQLParser.Opt_cscContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_csc.
    def exitOpt_csc(self, ctx:SQLParser.Opt_cscContext):
        pass


    # Enter a parse tree produced by SQLParser#data_type.
    def enterData_type(self, ctx:SQLParser.Data_typeContext):
        pass

    # Exit a parse tree produced by SQLParser#data_type.
    def exitData_type(self, ctx:SQLParser.Data_typeContext):
        pass


    # Enter a parse tree produced by SQLParser#enum_list.
    def enterEnum_list(self, ctx:SQLParser.Enum_listContext):
        pass

    # Exit a parse tree produced by SQLParser#enum_list.
    def exitEnum_list(self, ctx:SQLParser.Enum_listContext):
        pass


    # Enter a parse tree produced by SQLParser#create_select_statement.
    def enterCreate_select_statement(self, ctx:SQLParser.Create_select_statementContext):
        pass

    # Exit a parse tree produced by SQLParser#create_select_statement.
    def exitCreate_select_statement(self, ctx:SQLParser.Create_select_statementContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_ignore_replace.
    def enterOpt_ignore_replace(self, ctx:SQLParser.Opt_ignore_replaceContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_ignore_replace.
    def exitOpt_ignore_replace(self, ctx:SQLParser.Opt_ignore_replaceContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_temporary.
    def enterOpt_temporary(self, ctx:SQLParser.Opt_temporaryContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_temporary.
    def exitOpt_temporary(self, ctx:SQLParser.Opt_temporaryContext):
        pass


    # Enter a parse tree produced by SQLParser#set_stmt.
    def enterSet_stmt(self, ctx:SQLParser.Set_stmtContext):
        pass

    # Exit a parse tree produced by SQLParser#set_stmt.
    def exitSet_stmt(self, ctx:SQLParser.Set_stmtContext):
        pass


    # Enter a parse tree produced by SQLParser#set_list.
    def enterSet_list(self, ctx:SQLParser.Set_listContext):
        pass

    # Exit a parse tree produced by SQLParser#set_list.
    def exitSet_list(self, ctx:SQLParser.Set_listContext):
        pass


    # Enter a parse tree produced by SQLParser#set_expr.
    def enterSet_expr(self, ctx:SQLParser.Set_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#set_expr.
    def exitSet_expr(self, ctx:SQLParser.Set_exprContext):
        pass


    # Enter a parse tree produced by SQLParser#expr_list.
    def enterExpr_list(self, ctx:SQLParser.Expr_listContext):
        pass

    # Exit a parse tree produced by SQLParser#expr_list.
    def exitExpr_list(self, ctx:SQLParser.Expr_listContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_udf_expr_list.
    def enterOpt_udf_expr_list(self, ctx:SQLParser.Opt_udf_expr_listContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_udf_expr_list.
    def exitOpt_udf_expr_list(self, ctx:SQLParser.Opt_udf_expr_listContext):
        pass


    # Enter a parse tree produced by SQLParser#udf_expr_list.
    def enterUdf_expr_list(self, ctx:SQLParser.Udf_expr_listContext):
        pass

    # Exit a parse tree produced by SQLParser#udf_expr_list.
    def exitUdf_expr_list(self, ctx:SQLParser.Udf_expr_listContext):
        pass


    # Enter a parse tree produced by SQLParser#udf_expr.
    def enterUdf_expr(self, ctx:SQLParser.Udf_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#udf_expr.
    def exitUdf_expr(self, ctx:SQLParser.Udf_exprContext):
        pass


    # Enter a parse tree produced by SQLParser#ident.
    def enterIdent(self, ctx:SQLParser.IdentContext):
        pass

    # Exit a parse tree produced by SQLParser#ident.
    def exitIdent(self, ctx:SQLParser.IdentContext):
        pass


    # Enter a parse tree produced by SQLParser#expr.
    def enterExpr(self, ctx:SQLParser.ExprContext):
        pass

    # Exit a parse tree produced by SQLParser#expr.
    def exitExpr(self, ctx:SQLParser.ExprContext):
        pass


    # Enter a parse tree produced by SQLParser#predicate.
    def enterPredicate(self, ctx:SQLParser.PredicateContext):
        pass

    # Exit a parse tree produced by SQLParser#predicate.
    def exitPredicate(self, ctx:SQLParser.PredicateContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_escape.
    def enterOpt_escape(self, ctx:SQLParser.Opt_escapeContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_escape.
    def exitOpt_escape(self, ctx:SQLParser.Opt_escapeContext):
        pass


    # Enter a parse tree produced by SQLParser#expressionAtom.
    def enterExpressionAtom(self, ctx:SQLParser.ExpressionAtomContext):
        pass

    # Exit a parse tree produced by SQLParser#expressionAtom.
    def exitExpressionAtom(self, ctx:SQLParser.ExpressionAtomContext):
        pass


    # Enter a parse tree produced by SQLParser#constant.
    def enterConstant(self, ctx:SQLParser.ConstantContext):
        pass

    # Exit a parse tree produced by SQLParser#constant.
    def exitConstant(self, ctx:SQLParser.ConstantContext):
        pass


    # Enter a parse tree produced by SQLParser#fullColumnName.
    def enterFullColumnName(self, ctx:SQLParser.FullColumnNameContext):
        pass

    # Exit a parse tree produced by SQLParser#fullColumnName.
    def exitFullColumnName(self, ctx:SQLParser.FullColumnNameContext):
        pass


    # Enter a parse tree produced by SQLParser#hexadecimalLiteral.
    def enterHexadecimalLiteral(self, ctx:SQLParser.HexadecimalLiteralContext):
        pass

    # Exit a parse tree produced by SQLParser#hexadecimalLiteral.
    def exitHexadecimalLiteral(self, ctx:SQLParser.HexadecimalLiteralContext):
        pass


    # Enter a parse tree produced by SQLParser#bitValueLiteral.
    def enterBitValueLiteral(self, ctx:SQLParser.BitValueLiteralContext):
        pass

    # Exit a parse tree produced by SQLParser#bitValueLiteral.
    def exitBitValueLiteral(self, ctx:SQLParser.BitValueLiteralContext):
        pass


    # Enter a parse tree produced by SQLParser#stringLiteral.
    def enterStringLiteral(self, ctx:SQLParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by SQLParser#stringLiteral.
    def exitStringLiteral(self, ctx:SQLParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by SQLParser#stringCharsetName.
    def enterStringCharsetName(self, ctx:SQLParser.StringCharsetNameContext):
        pass

    # Exit a parse tree produced by SQLParser#stringCharsetName.
    def exitStringCharsetName(self, ctx:SQLParser.StringCharsetNameContext):
        pass


    # Enter a parse tree produced by SQLParser#string_literal_list.
    def enterString_literal_list(self, ctx:SQLParser.String_literal_listContext):
        pass

    # Exit a parse tree produced by SQLParser#string_literal_list.
    def exitString_literal_list(self, ctx:SQLParser.String_literal_listContext):
        pass


    # Enter a parse tree produced by SQLParser#collationName.
    def enterCollationName(self, ctx:SQLParser.CollationNameContext):
        pass

    # Exit a parse tree produced by SQLParser#collationName.
    def exitCollationName(self, ctx:SQLParser.CollationNameContext):
        pass


    # Enter a parse tree produced by SQLParser#reserved_keyword.
    def enterReserved_keyword(self, ctx:SQLParser.Reserved_keywordContext):
        pass

    # Exit a parse tree produced by SQLParser#reserved_keyword.
    def exitReserved_keyword(self, ctx:SQLParser.Reserved_keywordContext):
        pass


    # Enter a parse tree produced by SQLParser#unreserved_keyword.
    def enterUnreserved_keyword(self, ctx:SQLParser.Unreserved_keywordContext):
        pass

    # Exit a parse tree produced by SQLParser#unreserved_keyword.
    def exitUnreserved_keyword(self, ctx:SQLParser.Unreserved_keywordContext):
        pass


    # Enter a parse tree produced by SQLParser#interval.
    def enterInterval(self, ctx:SQLParser.IntervalContext):
        pass

    # Exit a parse tree produced by SQLParser#interval.
    def exitInterval(self, ctx:SQLParser.IntervalContext):
        pass


    # Enter a parse tree produced by SQLParser#functionCall.
    def enterFunctionCall(self, ctx:SQLParser.FunctionCallContext):
        self.output_list.append("functionCall")
        self.score += 1

    # Exit a parse tree produced by SQLParser#functionCall.
    def exitFunctionCall(self, ctx:SQLParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by SQLParser#function_call_generic.
    def enterFunction_call_generic(self, ctx:SQLParser.Function_call_genericContext):
        pass

    # Exit a parse tree produced by SQLParser#function_call_generic.
    def exitFunction_call_generic(self, ctx:SQLParser.Function_call_genericContext):
        pass


    # Enter a parse tree produced by SQLParser#function_name.
    def enterFunction_name(self, ctx:SQLParser.Function_nameContext):
        pass

    # Exit a parse tree produced by SQLParser#function_name.
    def exitFunction_name(self, ctx:SQLParser.Function_nameContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_expr_list.
    def enterOpt_expr_list(self, ctx:SQLParser.Opt_expr_listContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_expr_list.
    def exitOpt_expr_list(self, ctx:SQLParser.Opt_expr_listContext):
        pass


    # Enter a parse tree produced by SQLParser#function_call_specific.
    def enterFunction_call_specific(self, ctx:SQLParser.Function_call_specificContext):
        pass

    # Exit a parse tree produced by SQLParser#function_call_specific.
    def exitFunction_call_specific(self, ctx:SQLParser.Function_call_specificContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_expr.
    def enterOpt_expr(self, ctx:SQLParser.Opt_exprContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_expr.
    def exitOpt_expr(self, ctx:SQLParser.Opt_exprContext):
        pass


    # Enter a parse tree produced by SQLParser#when_list.
    def enterWhen_list(self, ctx:SQLParser.When_listContext):
        pass

    # Exit a parse tree produced by SQLParser#when_list.
    def exitWhen_list(self, ctx:SQLParser.When_listContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_else.
    def enterOpt_else(self, ctx:SQLParser.Opt_elseContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_else.
    def exitOpt_else(self, ctx:SQLParser.Opt_elseContext):
        pass


    # Enter a parse tree produced by SQLParser#cast_type.
    def enterCast_type(self, ctx:SQLParser.Cast_typeContext):
        pass

    # Exit a parse tree produced by SQLParser#cast_type.
    def exitCast_type(self, ctx:SQLParser.Cast_typeContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_charset_with_opt_binary.
    def enterOpt_charset_with_opt_binary(self, ctx:SQLParser.Opt_charset_with_opt_binaryContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_charset_with_opt_binary.
    def exitOpt_charset_with_opt_binary(self, ctx:SQLParser.Opt_charset_with_opt_binaryContext):
        pass


    # Enter a parse tree produced by SQLParser#charset_name.
    def enterCharset_name(self, ctx:SQLParser.Charset_nameContext):
        pass

    # Exit a parse tree produced by SQLParser#charset_name.
    def exitCharset_name(self, ctx:SQLParser.Charset_nameContext):
        pass


    # Enter a parse tree produced by SQLParser#string_literal.
    def enterString_literal(self, ctx:SQLParser.String_literalContext):
        pass

    # Exit a parse tree produced by SQLParser#string_literal.
    def exitString_literal(self, ctx:SQLParser.String_literalContext):
        pass


    # Enter a parse tree produced by SQLParser#charsetNameBase.
    def enterCharsetNameBase(self, ctx:SQLParser.CharsetNameBaseContext):
        pass

    # Exit a parse tree produced by SQLParser#charsetNameBase.
    def exitCharsetNameBase(self, ctx:SQLParser.CharsetNameBaseContext):
        pass


    # Enter a parse tree produced by SQLParser#character_set.
    def enterCharacter_set(self, ctx:SQLParser.Character_setContext):
        pass

    # Exit a parse tree produced by SQLParser#character_set.
    def exitCharacter_set(self, ctx:SQLParser.Character_setContext):
        pass


    # Enter a parse tree produced by SQLParser#precision.
    def enterPrecision(self, ctx:SQLParser.PrecisionContext):
        pass

    # Exit a parse tree produced by SQLParser#precision.
    def exitPrecision(self, ctx:SQLParser.PrecisionContext):
        pass


    # Enter a parse tree produced by SQLParser#field_length.
    def enterField_length(self, ctx:SQLParser.Field_lengthContext):
        pass

    # Exit a parse tree produced by SQLParser#field_length.
    def exitField_length(self, ctx:SQLParser.Field_lengthContext):
        pass


    # Enter a parse tree produced by SQLParser#opt_float_options.
    def enterOpt_float_options(self, ctx:SQLParser.Opt_float_optionsContext):
        pass

    # Exit a parse tree produced by SQLParser#opt_float_options.
    def exitOpt_float_options(self, ctx:SQLParser.Opt_float_optionsContext):
        pass


