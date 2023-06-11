import sys
import ply.lex as lex

class lex_value:
    def __init__(self, strs = None, value = None, scope = None) -> None:
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
        return  str(self.value) + " #" + str(self.scope) 

reserved = {
    'bool': "BOOL",
    'real': "REAL",
    'if': "IF",
    'struct': "STRUCT",
    'false': "FALSE",
    'fby': "FBY",
    'node': "NODE",
    'xor': "XOR",
    'package': "PACKAGE",
    'let': "LET",
    'int': "INT",
    'provides': "PROVIDES",
    'end': "END",
    'function': "FUNCTION",
    'include': "INCLUDE",
    'is': "IS",
    'pre': "PRE",
    'type': "TYPE",
    'need': "NEEDS",
    'unsafefunction': "UNSAFEFUNCTION",
    'externnode': "EXTERNNODE",
    'current': "CURRENT",
    'div': "DIV",
    'assert': "ASSERT",
    'returns': "RETURNS",
    'uses': "USES",
    'mod': "MOD",
    'enum': "ENUM",
    'externfunction': "EXTERNFUNCTION",
    'when': "WHEN",
    'unsafeexternnode': "UNSAFEEXTERNNODE",
    'model': "MODEL",
    'and': "AND",
    'or': "OR",
    'unsafeexternfunction': "UNSAFEEXTERNFUNCTION",
    'tel': "TEL",
    'body': "BODY",
    'nor': "NOR",
    'merge': "MERGE",
    'const': "CONST",
    'unsafenode': "UNSAFENODE",
    'true': "TRUE",
    'with': "WITH",
    'not': "NOT",
    'then': "THEN",
    'else': "ELSE",
    'step': "STEP",
    'var': "VAR"
}

tokens = [
    "INTCONST",  # ++
    "REALCONST",  # ++
    "LV6IDREF",  # ++
    'LESSEQU',  # <=
    'LBRACKET',  # [
    'COMMA',  # ,
    'GREATEREQU',  # >=
    'RBRACKET',  # ]
    'LPARENTHESE',  # (
    'RPARENTHESE',  # )
    'ARROW',  # ->
    'LSHIFT',  # <<
    'STAR',  # *
    'MINUS',  # -
    'PLUS',  # +
    'LBPARENTHESE',  # {
    'RBPARENTHESE',  # }
    'HASHTAG',  # #
    'EQU',  # =
    'COLON',  # :
    'NOEQU',  # <>
    'DIVIDE',  # /
    'SURPLUS',  # %
    'LESS',  # <
    'EXPONENT',  # ^
    'POINT',  # .
    'RSHIFT',  # >>
    'SEMICOLON',  # ;
    'SHIFT',  # =>
    'TPOINT',  # ..
    'GREATER',  # >
    "LV6ID"  # id
] + list(reserved.values())


def t_LV6IDREF(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*::[a-zA-Z0-9_]+'
    t.value = lex_value('lv6idref', t.value)
    return t


def t_REALCONST(t):
    r'\d+\.\d+'
    t.value = lex_value('realconst', float(t.value))
    return t


def t_INTCONST(t):
    r'\d+'
    t.value = lex_value('intconst', int(t.value))
    return t

t_BOOL = r'bool'
t_REAL = r'real'
t_IF = r'if'
t_STRUCT = r'struct'
t_FALSE = r'false'
t_FBY = r'fby'
t_NODE = r'node'
t_XOR = r'xor'
t_PACKAGE = r'package'
t_LET = r'let'
t_INT = r'int'
t_PROVIDES = r'provides'
t_END = r'end'
t_FUNCTION = r'function'
t_INCLUDE = r'include'
t_IS = r'is'
t_PRE = r'pre'
t_TYPE = r'type'
t_NEEDS = r'NEEDS'
t_UNSAFEFUNCTION = r'unsafefunction'
t_EXTERNNODE = r'externnode'
t_CURRENT = r'current'
t_DIV = r'div'
t_ASSERT = r'assert'
t_RETURNS = r'returns'
t_USES = r'uses'
t_MOD = r'mod'
t_ENUM = r'enum'
t_EXTERNFUNCTION = r'externfunction'
t_TEL = r'tel'
t_BODY = r'body'
t_NOR = r'nor'
t_MERGE = r'merge'
t_CONST = r'const'
t_UNSAFENODE = r'unsafenode'
t_TRUE = r'true'
t_WITH = r'with'
t_NOT = r'not'
t_THEN = r'then'
t_ELSE = r'else'
t_STEP = r'step'
t_VAR = r'var'
t_LESSEQU = r'<='
t_LSHIFT = r'<<'
t_NOEQU = r'<>'
t_GREATEREQU = r'>='
t_ARROW = r'\*>'
t_RSHIFT = r'>>'
t_SHIFT = r'=>'
t_TPOINT = r'\.\.'
t_LBRACKET = r'\['
t_COMMA = r','
t_RBRACKET = r'\]'
t_LPARENTHESE = r'\('
t_RPARENTHESE = r'\)'
t_STAR = r'\*'
t_MINUS = r'-'
t_PLUS = r'\+'
t_LBPARENTHESE = r'{'
t_RBPARENTHESE = r'}'
t_HASHTAG = r'\#'
t_EQU = r'='
t_COLON = r':'
t_DIVIDE = r'/'
t_SURPLUS = r'%'
t_LESS = r'<'
t_EXPONENT = r'\^'
t_POINT = r'\.'
t_SEMICOLON = r';'
t_GREATER = r'>'
t_ignore = ' \t'


def t_LV6ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'LV6ID')
    if not reserved.get(t.value):
        t.value = lex_value('lv6id', t.value)
    else:
        t.value = lex_value(t.value, t.value)
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

def getNfadir():
    nfa_dir = {}
    with open("data/NFA.txt") as nfa_f:
        nfas = list()
        nfa = list()
        for line in nfa_f.readlines():
            if len(line.strip()) == 0:
                nfas.append(nfa)
                nfa = list()
            else:
                nfa.append(line)
        if len(nfa) != 0:
            nfas.append(nfa)
        for n in nfas:
            type = n[0].split(':')[1].strip()
            nfa_dir[type] = n[1:]
    return nfa_dir

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
            scope = tok.value.scope
        f.write("{0:>10}\n".format("#" + scope))
        f.write("--------------------------------------\n")

lexer = lex.lex()

if __name__ == '__main__':
    data = '''
    node edge (X: bool) returns (Y: bool);
    let
     Y = r_edge (X) or r_edge (not(X));
    tel
    node r_edge (X: bool) returns (Y: bool);
    let
     Y = false -> X and not pre(X);
    tel
    '''
    toks = get_tokens(data)
    for tok in toks:
        print(tok, tok.value.strs)
    lex_ = lustre_lex()
    lex_.set_tokens(toks)
    