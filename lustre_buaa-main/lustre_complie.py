from lustre_lex import lex_value, lustre_lex, get_tokens
from lustre_lex import tokens
from ply.yacc import yacc

lus_lexer = lustre_lex()

func_set = set()

symbol_table = dict()

static_symbol_table = dict()

const_symbol_table = dict()

empty_status = lex_value("$")

def p_program_packboy(p):
    '''program : packbody'''
    p[0] = p[1]

def p_packbody1(p):
    'packbody : onedecl'
    p[0] = p[1]

def p_onedecl_nodedecl(p):
    'onedecl : nodedecl'
    p[0] = p[1]
    
def p_nodedecl_localnode(p):
    'nodedecl : localnode'
    p[0] = p[1]

def p_localnode_node1(p):
    'localnode : NODE LV6ID staticparams params RETURNS params onetypedecl4 localdecls body localnode1'
    p[0] = p[2]
    p[0].strs = 'node'
    p[0].type = 'node'
    p[0].syms = p[4].syms
    p[0].rets = p[6].syms
    symbol_table[p[0].value] = p[0]

def p_body(p):
    'body : LET body1 TEL'
    p[0] = p[2]

def p_body1(p):
    '''body1 : equationlist
             | empty'''
    p[0] = p[1]
    for v in p[1].syms:
        print(v.value)

def p_equationlist1_eq(p):
    'equationlist : equation'
    p[0] = lex_value('equ_list')
    p[0].syms.append(p[1])

def p_equationlist1_eqlist(p):
    'equationlist : equation equationlist' 
    p[2].syms.append(p[1])
    p[0] = p[2]


def p_equation_left(p):
    'equation : left EQU expression SEMICOLON'
    p[1].value = "=" + p[2].value
    p[0] = p[1]


def p_left(p):
    '''left : leftitemlist
            | LPARENTHESE leftitemlist RPARENTHESE'''
    if p[1].strs == '(':
        p[2].value = "(" + p[2].value + ")"
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_leftitemlist(p):
    '''leftitemlist : leftitem'''
    p[0] = p[1]

def p_leftitem_lv6id(p):
    '''leftitem : LV6ID'''
    p[0] = p[1]

def p_localdecls(p):
    '''localdecls : localdecllist
                  | empty'''
    p[0] = p[1]

def p_localdecllist1(p):
    'localdecllist : onelocaldecl localdecllist'
    p[0] = p[2]

def p_localdecllist2(p):
    'localdecllist : onelocaldecl'
    p[0] = p[1]

def p_onelocaldecl_var(p):
    'onelocaldecl : localvars'
    p[0] = p[1]

def p_onelocaldecl_const(p):
    'onelocaldecl : localconsts'
    p[0] = p[1]

def p_localconsts(p):
    'localconsts : CONST constdecllist'
    p[0] = p[2]
    for sym in p[0].syms:
        const_symbol_table[sym.value] = sym

def p_constdecllist1(p):
    'constdecllist : oneconstdecl SEMICOLON constdecllist'
    p[3].syms.extend(p[1].syms)
    p[0] = p[3]

def p_constdecllist2(p):
    'constdecllist : oneconstdecl'
    p[0] = p[1]

def p_oneconstdecl1(p):
    'oneconstdecl : LV6ID COLON type'
    p[1].type = p[3].type
    p[0] = lex_value('const_list')
    p[0].syms.append(p[1])
    

def p_localvars(p):
    'localvars : VAR vardecllist'
    p[0] = p[2]
    for sym in p[0].syms:
        symbol_table[sym.value] = sym

def p_params(p):
    'params : LPARENTHESE params1 RPARENTHESE'
    p[0] = p[2]

def p_params1(p):
    '''params1 : vardecllist onetypedecl4
             | empty'''
    p[0] = p[1]
    for sym in p[0].syms:
        symbol_table[sym.value] = sym

def p_vardecllist(p):
    '''vardecllist : vardecl vardecllist1'''
    p[2].syms.extend(p[1].syms)
    p[0] = p[2]

def p_vardecllist1(p):
    '''vardecllist1 : SEMICOLON vardecl vardecllist1'''
    p[3].syms.extend(p[2].syms)
    p[0] = p[3]

def p_vardecllist1_empty(p):
    'vardecllist1 : empty'
    p[0] = p[1]

def p_vardecl(p):
    '''vardecl : typedlv6ids'''
    p[0] = p[1]

def p_typedlv6ids(p):
    '''typedlv6ids : LV6ID user1 COLON type'''
    p[2].syms.append(p[1])
    for i, sym in enumerate(p[2].syms):
        p[2].syms[i].type = p[3].type
    p[0] = p[2]

def p_user1(p):
    '''user1 : COMMA LV6ID user1
             | empty'''
    if p[1].strs == ';':
        p[3].syms.append(p[2])
        p[0] = p[2]
    else:
        p[0] = lex_value('var_list')


def p_localnode1(p):
    '''localnode1 : POINT 
                  | onetypedecl4'''
    p[0] = p[1]

def p_ondetypedecl4(p):
    '''onetypedecl4 : SEMICOLON
                     | empty'''
    pass

def p_empty(p):
    'empty :'
    p[0] = empty_status

def p_staticparams(p):
    '''staticparams : LSHIFT staticparamlist RSHIFT
                    | empty'''
    if p[1].strs == '(':
        p[0] = p[2]

def p_staticparamslist(p):
    'staticparamlist : staticparam staticparamlist1'
    p[0] = p[1]

def p_staticparamlist1(p):
    '''staticparamlist1 : SEMICOLON staticparam staticparamlist1
                        | empty'''
    p[0] = p[2]

def p_staticparam_typelv6id(p):
    'staticparam : type LV6ID'
    p[2].type = p[1].type
    p[0] = p[2]
    static_symbol_table[p[2].value] = p[2]

def p_type(p):
    'type : type1 type2'
    p[0] = p[1]

def p_type1(p):
    '''type1 : BOOL
             | INT
             | REAL
             | LV6IDREF'''
    if p[1].strs == 'bool':
        p[1].type = 'bool'
    elif p[1].strs == 'int':
        p[1].type = 'int'
    elif p[1].strs == 'real':
        p[1].type = 'float'
    else:
        p[1].type = 'void *'
    p[0] = p[1]

def p_type2(p):
    '''type2 : EXPONENT expression type2
             | empty'''
    #TODO - remain to explain
    p[0] = empty_status

def p_expression_constant(p):
    'expression : constant'
    p[0] = p[1]

def p_constant(p):
    '''constant : TRUE
                | FALSE
                | REALCONST
                | INTCONST'''
    if p[1].strs == 'true' or p[1].strs == 'false':
        p[0] = p[1]
        p[0].type = 'bool'
    elif p[1].strs == 'intconst': 
        p[0] = p[1]
        p[0].type = 'int'
    elif p[1].strs == 'realconst':
        p[0] = p[1]
        p[0].type = 'float'
    else:
        print("error p_constant")

def p_expression_lv6id(p):
    'expression : LV6ID'
    if p[1].strs == 'lv6id' and p[1].value in symbol_table:
        p[0] = symbol_table[p[1].value]
    else:
        print("error p_expression_lv6id")

def p_expression_neg(p):
    'expression : MINUS expression'
    if p[1].strs == '-':
        p[0] = p[2]
        func_set.add("neg_function_%s" % p[2].type)
        p[0].value = "neg_function_%s(%s)" % (p[2].type, p[2].value) 
    else:
        print("error p_expression_neg")

def p_exression_not(p):
    'expression : NOT expression'
    if p[1].strs == 'not':
        p[0] = p[2]
        func_set.add("not_function_%s" % p[2].type)
        p[0].value = "not_function_%s(%s)" % (p[2].type, p[2].value) 
    else:
        print("error p_exression_not")

def p_expression_if(p):
    'expression : IF expression THEN expression ELSE expression'
    p[0] = p[4]
    func_set.add("if_function_%s" % p[4].type)
    p[0].value = "if_function_%s(%s,%s,%s)" % (p[4].type, p[2].value, p[4].value, p[6].value)


def p_error(p):
    print(p)
    print(func_set)
    print(symbol_table)
    print("Syntax error in input!")

def get_parse(strs, parse):
    ast = parse.parse(strs, lexer=lus_lexer)
    print(ast)

if __name__ == '__main__':
    data = '''
    node STABLE (in_judge: bool) returns (out_C: int);
    let
        out_C = if in_judge then 20 else 30;
    tel
    '''
    # data = '''true'''
    parse = yacc(debug=1)

    string_tokens = get_tokens(data)

    lus_lexer.set_tokens(string_tokens)

    # while True:
    #     tok = lexer.token()
    #     if tok == None:
    #         break
    #     # print(tok)

    get_parse(data, parse)
    print(symbol_table)
    print(func_set)
    