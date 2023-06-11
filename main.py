from audioop import reverse
import os

from pygments import lex
import cfg
import generate
import datetime
#from lustre_lex import get_tokens, getNfadir, lustre_lex
from c_lex import get_tokens
from recognition import Recognition

def ouput_result(pda, tokens, reco, c_code, path = 'result/'):
    if not os.path.exists(path):
        os.makedirs(path)

    lex_ = lustre_lex()
    lex_.set_tokens(tokens)

    # 打印词法分析结果
    with open(path + "tokens.txt", "w+") as f:
        lex_.output_program(f)
        for string_token in tokens:
            f.writelines(str(string_token) + "\n")

    '''flag = input("是否输出词法分析对应的nfa:(y/n)[nfa.txt]")
    if flag == "y":
        nfa_dir = getNfadir()
        with open(path + "nfa.txt", "w+") as f:
            for token in tokens:
                nfa = nfa_dir[token.type]
                f.writelines("类型: %10s, 开始状态:%5s, 结束状态:%5s, 状态个数:%5s, NFA:%s\n"
                    %(token.type.strip(), nfa[3].strip(), nfa[4].strip(), nfa[2].strip(), nfa[5:]))

    flag = input("是否输出文法对应的下推自动机:(y/n)[dfa.txt]")
    # 打印下推自动机
    if flag == "y":
        with open(path + "dfa.txt", "w+") as f:
            f.writelines(str(pda))

    it = 1
    
    with open(path + "reco.txt", "w+") as f:
        for v in reco.used:
            f.writelines(str(it) + " " + str(v) + "\n")
            it += 1

    with open(path + "result.c", "w+") as f:
        f.write(c_code)
'''

#删除了条件语句/赋值语句中的最后一个与异或^= |=有关的/删除了argument expression
if __name__ == '__main__':
    grammarString = ""
    with open("data/ctest.txt") as r_f:
        for line in r_f.readlines():
            grammarString += line

    inputString = '''
    bool _get_bool(int *s){
    int a;
    a=1;
    if(!a)
    {
        a=a+1;
    }
    }
    '''

    # 关键字、变量名、符号
    string_tokens = get_tokens(inputString)
    print(string_tokens)
    grammar, pda = cfg.create_pda(grammarString)
    print(pda)

    may_empty_nonterminal = cfg.get_may_empty_nonterminal(grammar)

    reconigtion = Recognition(pda, string_tokens, may_empty_nonterminal)
    result = reconigtion.is_accept('Start',0)
    # #
    # #
    if result:
        print("result : True")
        print(reconigtion.Code)
        # print(reconigtion.context)
        print(reconigtion.used)
    else:
        print("result : False")

    # reconigtion.used.reverse()
    # g = generate.Generate(reconigtion.used, string_tokens)
    # ouput_result(pda, string_tokens, reconigtion, g.gen_C(), "result" + datetime.datetime.now().strftime('%Y%m%d%H_%M_%S') + '/')


# # 文法单元 -> 前置条件/后置条件
# # 文法单元 -> 下推自动机  ++
# # 文法单元 -> 目标码 C --> misrC  -- **
# # 文法单元 -> 证明序列 （+证明的证据）
# # 文法单元 -> 证明序列的验证


