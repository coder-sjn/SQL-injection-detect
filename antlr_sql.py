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

    # tree_str = tree.toStringTree(recog=parser)
    # for token in stream.tokens:
    #     print(token)
    # print(tree_str)
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


def sql_parse(input_str):
    output_list = []
    start = 0                       # 解析的开始位置
    end = len(input_str) - 2        # 用于判断解析是否结束
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
            try:
                start = tree.stop.stop + 1
            except AttributeError:
                break
        # 在出错token与开始解析位置之间存在可解析语句
        else:
            substr = input_str[:flag]
            # 构建语法树
            tree, lexer = build_tree(substr)
            # Listener
            tree_listener(tree, listener)
            start = flag + 1
        end -= start

    return output_list, listener.score


if __name__ == '__main__':
    with open('data/before_parse.txt', 'r', encoding='UTF-8') as f:
        for parse_str in f.readlines():
            parse_str = parse_str.upper()
            line = parse_str.replace("\\\\", " escape ").replace("\\\"", " a ").replace("\\\'", " a ")
            if '\"' in line:
                # 填充双引号
                line = '\"' + line
            if '\'' in line:
                # 填充单引号
                line = '\'' + line
            output1, score1 = sql_parse(parse_str)
            output2, score2 = sql_parse(line)
            with open('data/after_parse.txt', 'a') as f2:
                f2.write("1:  ")
                for token in output1:
                    f2.write(token)
                    f2.write(' ')
                f2.write("2:  ")
                for token in output2:
                    f2.write(token)
                    f2.write(' ')
                f2.write("   type: ")
                if score1 >= 2 or score2 >= 2:
                    f2.write("sql injection!")
                else:
                    f2.write("normal")
                f2.write('\n')
