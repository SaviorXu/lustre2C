import copy
import re
from audioop import reverse
import os

from pygments import lex
import cfg
import generate
import datetime
#from lustre_lex import get_tokens, getNfadir, lustre_lex
from c_lex import get_tokens
from recognition import Recognition
TERMINAL = re.compile(r'[a-zΔε_0-9*><!=+-/";:(){}&?#.%^\[\],\'@~][a-zA-ZΔε_0-9*><=+-/";:(){}&#.%^\[\],\'@~]*')

funcPara=list()
class Context:
    def __init__(self,key=None,value=None):
        self.key=key
        self.value=copy.deepcopy(value)

def getFuncName(context):
    for i in context:
        if i.key=="FunctionName":
            return i.value

def getFuncParaType(context,stStr,targetStr,st,retList):
    # print(stStr,targetStr,st)
    for i in range(st,len(context[st:-1]),1):
        if context[i].key==stStr:
            if context[i].key==targetStr:
                retList.append(context[i].value)
                return
            #若value是终止符，且key和target不相等，则直接返回
            if context[i].key==stStr and len(context[i].value)==1 and TERMINAL.fullmatch(context[i].value[0]):
                return
            for j in context[i].value:
                getFuncParaType(context,j,targetStr,i+1,retList)
            return

def getFuncPara(context,stStr,targetStr,st):
    global funcPara
    for i in range(st,len(context[st:-1]),1):
        if context[i].key==stStr:
            index=i
            if context[i].key==targetStr:
                funcPara.append(context[i].value)
                return i
            if type(context[i].value)!=list and TERMINAL.fullmatch(context[i].value):
                return i
            for j in context[i].value:
                index=getFuncPara(context,j,targetStr,index+1)
            return i
    return st
def createFuncHead(funcName,funcPara,str):
    str+="definition "+funcName +"::" +" \""
    for i in funcPara:
        if i=="int" or i=="float":
            str+="real \<Rightarrow> "
        else:
            str=str+i+" \<Rightarror> "
    str+="("
    for i in range(len(funcPara)):
        if funcPara[i]=="int" or funcPara[i]=="float":
            str+="real"
        else:
            str+=i
        if i!=len(funcPara)-1:
            str+=" \<times> "
        else:
            str+=") \" where \" "+funcName
            for j in range(len(funcPara)):
                str+=" "+chr(ord('a')+j)
            str+="\<equiv>"
    return str

def PrimaryExpression(context,st,stStr):
    print("PrimaryExpression",st,stStr)
    str=""
    index=0
    for i in range(st,len(context)):
        if context[i].key==stStr:
            if type(context[i].value)!=list and len(context[i].value)==1:
                str+=context[i].value
                return i, str
            elif type(context[i].value)==list and len(context[i].value)==3:
                str+="("
                index,tmpStr=Expression(context,i+1,"Expression")
                str+=tmpStr
                str+=")"
                return index,str

def ArithmeticExpression(context,st,stStr):
    print("ArithmeticExpression", st, stStr)
    str=""
    index=0
    for i in range(st,len(context)):
        if context[i].key==stStr:
            index,tmpStr=PrimaryExpression(context,i+1,"PrimaryExpression")
            str+=tmpStr
            str+=context[i].value[1]
            index,tmpStr=Expression(context,index+1,"Expression")
            str+=tmpStr
            return index,str

def Variable(context,st,stStr):
    for i in range(st,len(context)):
        if context[i].key==stStr:
            return i,context[i].value

def AssignmentExpression(context,st,stStr):
    print("AssignmentExpression", st, stStr)
    str=""
    index=0
    var=""
    tmpStr=""
    for i in range(st,len(context)):
        if context[i].key==stStr:
            if context[i].value[1]=="=":
                index,var=Variable(context,i+1,"Variable")
                print("variable finish")
                index,tmpStr=Expression(context,index+1,"Expression")
                break
    str+="("
    for i in range(0,len(funcPara)):
        if var !=funcPara[i]:
            str+=funcPara[i]
        else:
            str+=tmpStr
        if i!=len(funcPara)-1:
            str+=","
        else:
            str+=")"
    print("Assignment",str)
    return index,str

def Expression(context,st,stStr):
    print("Expression", st, stStr)
    index=0
    str=""

    for i in range(st,len(context)):
        if context[i].key==stStr:
            if context[i].value[0]=="PrimaryExpression":
                index,str=PrimaryExpression(context,i+1,"PrimaryExpression")
            if context[i].value[0]=="ArithmeticExpression":
                index,str=ArithmeticExpression(context,i+1,"ArithmeticExpression")
            if context[i].value[0]=="AssignmentExpression":
                index,str=AssignmentExpression(context,i+1,"AssignmentExpression")
            return index,str


def BoolLogicalExpr(context,st,stStr):
    print("BoolLogicalExpr", st, stStr)
    str=""
    for i in range(st,len(context)):
        if context[i].key==stStr:
            if context[i].value[0]=="BoolNot":
                index,tmpStr=Expression(context,i+1,"Expression")
                str=str+tmpStr+"=0"
                return index,str
def LogicalExpr(context,st,stStr):
    print("LogicalExpr", st, stStr)
    str=""
    for i in range(st,len(context)):
        if context[i].key==stStr:
            if context[i].value[0]=="BoolLogicalExpression":
                index,tmpStr=BoolLogicalExpr(context,i+1,"BoolLogicalExpression")
                str+=tmpStr
            return index,str

def IfStatement(context,st,stStr):
    print("IfStatement", st, stStr)
    str=""
    tmpStr=""
    for i in range(st,len(context)):
        if context[i].key==stStr:
            str+="if"+" ("
            index,tmpStr=LogicalExpr(context,i+1,"LogicalExpression")
            str+=tmpStr
            str+=") then "
            index,tmpStr=StatementList(context,index+1,"StatementList")
            print("then ",tmpStr)
            str+=tmpStr
            str+=" else "
            index,tmpStr=StatementList(context,index+1,"StatementList")
            str+=tmpStr
            return index,str
def ExpressionStatement(context,st,stStr):
    print("ExpressionStatement", st, stStr)
    index=0
    str=""
    for i in range(st,len(context)):
        if context[i].key==stStr:
            if context[i].value[0]=="Expression":
                index,str=Expression(context,i+1,"Expression")
                return index,str
            if context[i].value=="EmptyStatement":
                return i,str
def Statement(context,st,stStr):
    print("Statement", st, stStr)
    index=0
    str=""
    for i in range(st,len(context)):
        if context[i].key==stStr:
            if context[i].value[0]=="IfStatement":
                index,str=IfStatement(context,i+1,"IfStatement")
            if context[i].value[0]=="ExpressionStatement":
                index,str=ExpressionStatement(context,i+1,"ExpressionStatement")
            return index,str

def StatementList(context,st,stStr):
    print("StatementList", st, stStr)
    tmpStr=""
    str=""
    index=st
    for i in range(st,len(context)):
        if context[i].key==stStr:
            if len(context[i].value)==2:
                index=i
                index,tmpStr=Statement(context,index+1,"Statement")
                str+=tmpStr
                index,tmpStr=StatementList(context,index+1,"StatementList")
                str+=tmpStr
                return index,str
            if len(context[i].value)==1:
                return i,str
    return st,str

def change_isabelle(context):
    funcName=getFuncName(context)
    # print(funcName)
    funcParaType=list()
    global funcPara
    getFuncParaType(context,"ParameterList","TypeSpecifier",0,funcParaType)
    getFuncPara(context,"ParameterList","DirectDeclarator",0)
    print("funcPara")
    print(funcPara)
    str=createFuncHead(funcName,funcParaType,"")
    index,tmpStr=StatementList(context,0,"StatementList")
    str+=tmpStr
    str+="\" "
    print(str)


def get_context(stateList,tokens):
    flag=True
    tmpList=list()
    context=list()
    index=0
    for i in stateList:
        if i[2] == 'PUSH':
            tmpList.append(i[3])
        else:
            if flag is False:
                tmp=tmpList[0]
                tmpList.pop(0)
                tmpList.reverse()
                if len(tmpList)!=0:
                    element=Context(tmp,tmpList)
                    context.append(element)
                elif len(tmpList)==0 and tmp != "Empty":
                    tokenStr=str(tokens[index].value)
                    tmpStr = tokenStr.split(" ")[0]
                    element = Context(tmp,tmpStr)
                    index += 1
                    context.append(element)
            else:
                flag=False
            tmpList.clear()
            if len(i)==4:
                tmpList.append(i[3])
    for j in context:
        print(j.key,j.value)
    print(len(context))
    change_isabelle(context)


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
    void example(int a,int b){
    if(!a)
    {
        a=a+(a*2);
    }else
    {
        b=b+1;
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
        reconigtion.used.reverse()
        print(reconigtion.used)
        get_context(reconigtion.used,string_tokens)
    else:
        print("result : False")
    # tmp=list()
    # for i in string_tokens:
    #     tmp.append(i.value.strs)
    # print(tmp)

    # reconigtion.used.reverse()
    # g = generate.Generate(reconigtion.used, string_tokens)
    # ouput_result(pda, string_tokens, reconigtion, g.gen_C(), "result" + datetime.datetime.now().strftime('%Y%m%d%H_%M_%S') + '/')


# # 文法单元 -> 前置条件/后置条件
# # 文法单元 -> 下推自动机  ++
# # 文法单元 -> 目标码 C --> misrC  -- **
# # 文法单元 -> 证明序列 （+证明的证据）
# # 文法单元 -> 证明序列的验证


