import sys
import ply.lex as lex


class lex_value:
    def __init__(self, strs=None, value=None, scope=None) -> None:
        self.strs = strs
        self.value = value
        self.scope = scope
        self.type = None
        self.entity = None
        self.syms = list()
        self.rets = list()

    def set_value(self, value):
        self.value = value

    def set_scope(self, scope):
        self.scope = scope

    def __repr__(self) -> str:
        return str(self.value) + " #" + str(self.scope)


reserved = {
    'bool': "BOOL",
    'char': "CHAR",
    'int': "INT",
    'real': "REAL",
    'float': "FLOAT",
    'typedef': "TYPEDEF",
    'if': "IF",
    'else': "ELSE",
    'struct': "STRUCT",
    'false': "FALSE",
    'true': "TRUE",
    'enum': "ENUM",
    'switch': "SWITCH",
    'case': "CASE",
    'do': "DO",
    'while': "WHILE",
    'return': "RETURN",
    'void': "VOID",
    'sizeof': "SIZEOF",
    'for': "FOR",
    'break': "BREAK",
    'const': "CONST",
    'continue': "CONTINUE"
}

tokens = [
             "INTEGER",  # 整数
             "DECIMAL",  # 小数
             "IDENTIFIER",  # 变量
             'PLUS',  # +
             'MINUS',  # -
             'DIVIDE',  # /
             'DOT',  # .
             'EQUAL',  # =
             'STAR',  # *
             'ADDR',  # &
             'MOD',  # %
             'SQUARE',  # **
             'LSHIFT',  # 位运算符 <<
             'RSHIFT',  # >>
             'AND',  # &&
             'OR',  # ||
             'NOT',  # !
             'XOR',  # ^
             'ARROW',  # ->
             'L_PARENTHESIS',  # (
             'R_PARENTHESIS',  # )
             'L_SQUARE_BRACKET',  # [
             'R_SQUARE_BRACKET',  # ]
             'L_BRACE',  # {
             'R_BRACE',  # }
             'QUESTION_SIGN',  # ?
             'COMMA',  # ,
             'COLON',  # :
             'SEMICOLON',  # ;
             'POUND_SIGN',  # #
             'LESS_THAN',  # <
             'LESS_EQUAL_THAN',  # <=
             'GREAT_THAN',  # >
             'GREAT_EQUAL_THAN',  # >=
             'QUOTATION',  # '
             'STRING',  # 字符串
             'ANNOTATION',  # 单行注释
             'MULTI_LINE_ANNOTATION'  # 多行注释
         ] + list(reserved.values())

t_BOOL = r'bool'
t_CHAR = r'char'
t_INT = r'int'
t_REAL = r'real'
t_FLOAT = r'float'
t_TYPEDEF = r'typedef'
t_IF = r'if'
t_ELSE = r'else'
t_STRUCT = r'struct'
t_FALSE = r'false'
t_TRUE = r'true'
t_ENUM = r'enum'
t_SWITCH = r'switch'
t_CASE = r'case'
t_DO = r'do'
t_WHILE = r'while'
t_RETURN = r'return'
t_VOID = r'void'
t_SIZEOF = r'sizeof'
t_FOR = r'for'
t_BREAK = r'break'
t_CONST = r'const'
t_CONTINUE = r'continue'
t_DOT = r'\.'
t_EQUAL = r'='
t_STAR = r'\*'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'/'
t_ADDR = r'&'
t_MOD = r'%'
t_SQUARE = r'\*\*'
t_LSHIFT = r'<<'
t_RSHIFT = r'>>'
t_AND = r'&&'
t_OR = r'\|\|'
t_XOR = r'\^'
t_NOT = r'!'
t_ARROW = r'->'
t_L_PARENTHESIS = r'\('
t_R_PARENTHESIS = r'\)'
t_L_SQUARE_BRACKET= r'\['
t_R_SQUARE_BRACKET = r'\]'
t_L_BRACE = r'\{'
t_R_BRACE = r'\}'
t_QUESTION_SIGN = r'\?'
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'
t_POUND_SIGN = r'\#'
t_LESS_THAN = r'<'
t_LESS_EQUAL_THAN = r'<='
t_GREAT_THAN = r'>'
t_GREAT_EQUAL_THAN = r'>='
t_QUOTATION = r'\''
t_ignore = ' \t'

def t_INTEGER(t):
    r'\d+'
    t.value = lex_value('integer', int(t.value))
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = lex_value('decimal', float(t.value))
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    if not reserved.get(t.value):
        t.value = lex_value('identifier', t.value)
    else:
        t.value = lex_value(t.value, t.value)
    return t

# def t_OPERATOR(t):
#     r'[\*/\+\-]'
#     t.value = lex_value('operator', t.value)
#     return t

def t_STRING(t):
    r'\"[^"]*\"'
    t.value = lex_value('string', t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal charactor '%s'" % t.value[0])
    t.lexer.skip(1)

def get_tokens(inputString):
    lexer.input(inputString)
    string_tokens = list()
    while True:
        tok = lexer.token()
        if not tok:
            break
        if type(tok.value) == str:
            tok.value = lex_value(tok.value, tok.value)
        string_tokens.append(tok)
    get_scope(string_tokens)
    return string_tokens


def token2string(token):
    return "值：%10s，类型：%15s" % (token.value, token.type)


# def getNfadir():
#     nfa_dir = {}
#     with open("data/C_NFA.txt") as nfa_f:
#         nfas = list()
#         nfa = list()
#         for line in nfa_f.readlines():
#             if len(line.strip()) == 0:
#                 nfas.append(nfa)
#                 nfa = list()
#             else:
#                 nfa.append(line)
#         if len(nfa) != 0:
#             nfas.append(nfa)
#         for n in nfas:
#             type = n[0].split(':')[1].strip()
#             nfa_dir[type] = n[1:]
#     return nfa_dir


def increase_scope(scope) -> str:
    scopes = scope.split(".")
    if len(scopes) == 1:
        return str(int(scopes[0]) + 1)
    else:
        scopes[-1] = str(int(scopes[-1]) + 1)
        return '.'.join(scopes)


def get_scope(tokens) -> bool:
    stack = list()
    scope = str()
    cur_line = 0

    for i, tok in enumerate(tokens):
        if len(stack) == 0:
            stack.append([i, "1"])
            scope = stack[-1][1]
        elif tok.type == "LET":
            tmp = stack[-1][1] + ".1"
            stack.append([i, tmp])
            scope = stack[-1][1]
        elif tok.type == "TEL":
            scope = increase_scope(stack[-1][1])
            if tokens[stack[-1][0]].type == "LET":
                stack.pop()
            else:
                print("Error let/tel at " + str(tok.lineno) + "," + str(tok.lexpos))
                return False
        elif tok.lineno != cur_line:
            stack[-1][1] = increase_scope(stack[-1][1])
            scope = stack[-1][1]

        cur_line = tokens[i].lineno
        tokens[i].value.scope = scope
    return True


def get_raw_lexer():
    return lexer


class lustre_lex:
    def __init__(self):
        self.toks = list()
        self.index = 0

    def set_tokens(self, toks):
        self.index = 0
        self.toks = toks

    def token(self):
        if self.index >= len(self.toks):
            return None
        tmp = self.toks[self.index]
        self.index += 1
        return tmp

    def input(self, strs):
        pass

    def output_program(self, f):
        scope = ""
        cur_line = self.toks[0].lineno
        f.write("--------------program----------------\n")
        for tok in self.toks:
            if cur_line != tok.lineno:
                f.write("{0:>10}\n".format("#" + scope))
                cur_line = tok.lineno
            f.write(str(tok.value.value) + " ")
            # scope = tok.value.scope
        f.write("{0:>10}\n".format("#" + scope))
        f.write("--------------------------------------\n")

lexer = lex.lex()

if __name__ == '__main__':
    data = '''
    #include "sumsum.h"

    bool _get_bool(char* s){
        int _V;
        printf("input 1/0 %s=",s);
        scanf_s("%d", &_V);
        printf("\n");
        return (bool)_V;
    }
    int _get_int(char *s){
        int _V;
        printf("input an integer %s=",s);
        scanf_s("%d", &_V);
        printf("\n");
        return _V;
    }
    float _get_real(char *s){
        float _V;
        printf("input a float %s=",s);
        scanf_s("%f", &_V);
        printf("\n");
        return _V;
    }

    void _put_bool(bool _V, char *s){
        printf("%s: ", s);
        printf(_V?"true\n":"false\n");
    }
    void _put_int(int _V, char *s){
        printf("%s: %d\n", s, _V);
    }
    void _put_real(float _V, char *s){
        printf("%s: %f\n", s, _V);
    }
    arrow_int_ctx_type* arrow_int_ctx_new_ctx(){
        arrow_int_ctx_type* ctx = (arrow_int_ctx_type*)calloc(1, sizeof(arrow_int_ctx_type));
        arrow_int_ctx_reset(ctx);
        return ctx;
    }
    void arrow_int_ctx_reset(arrow_int_ctx_type* ctx){  ctx->_memory = true;
    }
    int arrow_int_func(int s1, int s2, arrow_int_ctx_type* ctx){
        int tmp = (ctx->_memory)? s1 : s2;
        ctx->_memory = false;
        return tmp;
    }
    pre_int_ctx_type* pre_int_ctx_new_ctx(){
        pre_int_ctx_type* ctx = (pre_int_ctx_type*)calloc(1, sizeof(pre_int_ctx_type));
        pre_int_ctx_reset(ctx);
        return ctx;
    }
    void pre_int_ctx_reset(pre_int_ctx_type* ctx){
    }
    int pre_int_get(pre_int_ctx_type* ctx){
        return ctx -> _memory;
    }
    void pre_int_set(int s1, pre_int_ctx_type* ctx){
        ctx -> _memory = s1;
    }
    arrow_real_ctx_type* arrow_real_ctx_new_ctx(){
        arrow_real_ctx_type* ctx = (arrow_real_ctx_type*)calloc(1, sizeof(arrow_real_ctx_type));
        arrow_real_ctx_reset(ctx);
        return ctx;
    }
    void arrow_real_ctx_reset(arrow_real_ctx_type* ctx){  ctx->_memory = true;
    }
    real arrow_real_func(real s1, real s2, arrow_real_ctx_type* ctx){
        real tmp = (ctx->_memory)? s1 : s2;
        ctx->_memory = false;
        return tmp;
    }
    pre_real_ctx_type* pre_real_ctx_new_ctx(){
        pre_real_ctx_type* ctx = (pre_real_ctx_type*)calloc(1, sizeof(pre_real_ctx_type));
        pre_real_ctx_reset(ctx);
        return ctx;
    }
    void pre_real_ctx_reset(pre_real_ctx_type* ctx){
    }
    real pre_real_get(pre_real_ctx_type* ctx){
        return ctx -> _memory;
    }
    void pre_real_set(real s1, pre_real_ctx_type* ctx){
        ctx -> _memory = s1;
    }
    result_ctx_type* new_ctx(){
        result_ctx_type* ctx = (result_ctx_type*)calloc(1, sizeof(result_ctx_type));
        ctx_reset(ctx);
        return ctx;
    }
    void ctx_reset(result_ctx_type* ctx){
        arrow_int_ctx_reset(&ctx->arrow_int_ctx_tab[0]);
        pre_int_ctx_reset(&ctx->pre_int_ctx_tab[0]);
        arrow_real_ctx_reset(&ctx->arrow_real_ctx_tab[0]);
        pre_real_ctx_reset(&ctx->pre_real_ctx_tab[0]);
    }
    struct update_acc{
        int i;
        int j;
        real v;
    };
    void ms_to_kmh(real x,real *res,result_ctx_type* ctx){
    *res=x * 3.6;
    }
    void maxr(real x,real y,real *res,result_ctx_type* ctx){
    *res=(x < y)?(y):(x);;
    }
    void red_0_0_0(real ain1, real ain2[3],real aout, result_ctx_type* ctx){
        for(int i=0;i<3;i++){
            ain1=ain1 + ain2[i];
        }
        memcpy(aout,&ain1,sizeof(real));
    }
    void fillred_0_0_0_0(struct update_acc ain,  real cell[3], struct update_acc *aout,  real ncell[3], result_ctx_type* ctx){
        for(int i=0;i<3;i++){
            update_cell_do_0_0_0_0(ain, cell[i], &ain, &ncell[i], ctx);
        }
        memcpy(aout,&ain,sizeof(struct update_acc));
    }
    void update_cell_do_0_0_0_0(struct update_acc acc,real cell,struct update_acc *nacc,real *ncell,result_ctx_type* ctx){
    *ncell=(acc.i == acc.j)?(acc.v):(cell);;
    struct update_acc split_1;
    split_1.i=acc.i + 1;
    split_1.j=acc.j;
    split_1.v=acc.v;
    *nacc=split_1;
    }
    void assign_0_0_0(real v,int jv,real t[3],real nt[3],result_ctx_type* ctx){
    struct update_acc dummy;
    struct update_acc split_1;
    split_1.i=0;
    split_1.j=jv;
    split_1.v=v;
    struct update_acc split_2;
    real split_3[3];
    fillred_0_0_0_0(split_1,t,&split_2,split_3,ctx);
    dummy=split_2;
    memcpy(nt,split_3,sizeof(real[3]));
    }
    void sum_0_0(real s,real *res,result_ctx_type* ctx){
    real a[3];
    real pre_a[3];
    int i;
    int split_1;
    split_1 = arrow_int_func(0, pre_int_get(&ctx -> pre_int_ctx_tab[0]), &ctx -> arrow_int_ctx_tab[0]);
    i=split_1 + 1;
    real*split_2 = (real*)malloc(sizeof(real[3]));
    for(int i=0;i<3;i++)
      split_2[i] = 0.0;
    real split_3[3];
    split_3 = arrow_real_func((split_2), pre_real_get(&ctx -> pre_real_ctx_tab[0]), &ctx -> arrow_real_ctx_tab[0]);
    memcpy(pre_a,split_3,sizeof(real[3]));
    real split_4[3];
    assign_0_0_0(s,i % 3,pre_a,split_4,ctx);
    memcpy(a,split_4,sizeof(real[3]));
    real split_5;
    red_0_0_0(0.0,a,&split_5,ctx);
    *res=split_5;
    pre_int_set(i,&ctx -> pre_int_ctx_tab[0]);
    pre_real_set(a,&ctx -> pre_real_ctx_tab[0]);
    }
    void sumsum(real s,real *res,result_ctx_type* ctx){
    real split_1;
    sum_0_0(1.5,&split_1,ctx);
    *res=split_1;
    }
    int main(){
        real s;
        real res;
        result_ctx_type* ctx = new_ctx();
        while(1){
            s = _get_real("s");
            sumsum(s,&res,ctx);
            _put_real(res,"res");
        }
    }
    '''
    toks = get_tokens(data)
    for tok in toks:
        print(tok, tok.value.strs)
    lex_ = lustre_lex()
    lex_.set_tokens(toks)
