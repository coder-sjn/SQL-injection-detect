from urllib import parse
from antlr_sql import sql_parse


def url_parse(url):
    ret = []
    result = parse.urlparse(url)
    parsed_result = parse.parse_qs(result.query)
    # parsed_result dict类型 {'id': ["1' and 1=2 union all select version(), 2 #"], 'Submit': ['Submit']}
    for values in parsed_result.values():
        for value in values:
            # 只取有可能有注入的参数
            # 注意：此处未处理url编码之外的其他编码类型
            if ' ' in value or '/*' in value:
                ret.append(value)
    # print(result.path)
    with open('white_before.txt', 'a') as f:
        for prm in ret:
            f.write(prm)
            f.write('\n')
    return ret


if __name__ == '__main__':
    with open('url.txt', 'r', encoding='UTF-8') as f:
        for url in f.readlines():
            params = url_parse(url)
            for param in params:
                param = param.upper()
                line = param.replace("\\\\", " escape ").replace("\\\"", " a ").replace("\\\'", " a ")
                if '\"' in line:
                    # 填充双引号
                    line = '\"' + line
                if '\'' in line:
                    # 填充单引号
                    line = '\'' + line
                output1, score1 = sql_parse(param)
                output2, score2 = sql_parse(line)
                with open('white.txt', 'a') as f2:
                    f2.write("1:  ")
                    for token in output1:
                        f2.write(token)
                        f2.write(' ')
                    f2.write("2:  ")
                    # f2.write('\n')
                    for token in output2:
                        f2.write(token)
                        f2.write(' ')
                    f2.write("   type: ")
                    if score1 >= 2 or score2 >= 2:
                        f2.write("sql injection!")
                    else:
                        f2.write("normal")
                    f2.write('\n')

