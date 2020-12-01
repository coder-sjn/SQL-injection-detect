from antlr4 import *
from antlr4.InputStream import InputStream
from antlr4.tree.Tree import ErrorNodeImpl
from antlr4.tree.Tree import TerminalNodeImpl
from SQLLexer import SQLLexer
from SQLParser import SQLParser
from SQLParserListener import SQLParserListener


# 构建语法树
def build_tree(str):
    input = InputStream(str)
    lexer = SQLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = SQLParser(stream)
    tree = parser.prog()

    tree_str = tree.toStringTree(recog=parser)
    # for token in stream.tokens:
    #     print(token)
    print(tree_str)
    return tree, lexer


# Listener
def tree_listener(tree, listener):
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    return listener.output_list


# 遍历语法树
def my_walk(tree, lexer, start, stop, flag, output_list):
    # 判断是否是错误节点，并且判断错误节点在可解析语句之前（返回-1）还是之后（返回出错位置stop）
    if isinstance(tree, ErrorNodeImpl):
        error_start = tree.parentCtx.start.start
        if start < error_start:
            stop = error_start - 1
            return stop
        token_type_num = tree.parentCtx.start.type
        output_list.append(lexer.ruleNames[token_type_num - 1])
        # print(lexer.ruleNames[token_type_num - 1])
        return -1
    # 判断是否是可解析语句，若可解析返回0
    if isinstance(tree, TerminalNodeImpl):
        return 0
    # 遍历语法树
    for child in tree.getChildren():
        flag = my_walk(child, lexer, start, stop, flag, output_list)
        if flag != 0:
            break
    return flag       # 返回0：可成功解析完整sql语句； 返回-1：在完整sql语句前存在错误； 返回出错位置stop：


if __name__ == '__main__':
    input_str = "/*!union all SELECT*/ * from tablename where 1=1"
    # input_str = "'-1915' UNION ALL SELECT *"
    input_str = input_str.upper()
    input_str = input_str.replace("\\\\", " escape ").replace("\\\"", " a ").replace("\\\'", " a ")
    if '\"' in input_str:
        # 填充双引号
        input_str = '\"' + input_str
    if '\'' in input_str:
        # 填充单引号
        input_str = '\'' + input_str
    output_list = []
    start = 0                       # 解析的开始位置
    end = len(input_str) - 1        # 用于判断解析是否结束
    stop = end + 1                  # 解析的停止位置
    listener = SQLParserListener(output_list)
    while(end >= 0):
        input_str = input_str[start:stop]
        # 构建语法树
        tree, lexer = build_tree(input_str)
        # 判断能否完整解析
        flag = 0
        flag = my_walk(tree, lexer, start, stop, flag, output_list)

        # 解析第一个token出错
        if flag == -1:
            start = tree.start.stop + 1
        # 完整解析
        elif flag == 0:
            # Listener
            tree_listener(tree, listener)
            start = tree.stop.stop + 1
        # 在出错token与开始解析位置之间存在可解析语句
        else:
            substr = input_str[:flag]
            # 构建语法树
            tree, lexer = build_tree(substr)
            # Listener
            tree_listener(tree, listener)
            start = flag + 1
        # if tree.stop.stop != stop - len(tree.stop.text):
        #     start = tree.stop.stop + 1
        end -= start
    score = listener.score
    for token in output_list:
        print(token, end=" ")
    print('\n')
    if score >= 2:
        print("sql injection!")
    else:
        print("normal")

# lexer = sql_parseLexer(input)
# stream = CommonTokenStream(lexer)
# parser = sql_parseParser(stream)
# tree = parser.prog()
# for token in stream.tokens:
#     print(token)
# print(tree.toStringTree(recog=parser))
