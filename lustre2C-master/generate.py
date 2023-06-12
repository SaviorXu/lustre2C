
from cfg import error


class Generate():
    def __init__(self, lex_status, lex_tokens):
        self.lex_status = lex_status
        self.lex_tokens = lex_tokens
        self.C_code = ''
        self.symbols = None
        self.in_symbols = set()
        self.out_symbols = set()

    def get_symbols(self):
        d = dict()
        l = len(self.lex_tokens)
        for i in range(l):
            if self.lex_tokens[i].value == "lv6id" and i + 2 < l \
                and self.lex_tokens[i+1].value == ":" :
                if self.lex_tokens[i+2].value == 'bool':
                    d[self.lex_tokens[i].str] = 'bool'
                elif self.lex_tokens[i+2].value == 'int':
                    d[self.lex_tokens[i].str] = 'int'
                elif self.lex_tokens[i+2].value == 'real':
                    d[self.lex_tokens[i].str] = 'real'
                else:
                    print("Unknown type")
                    break
                if self.lex_tokens[i].str.startswith('in_'):
                    self.in_symbols.add(self.lex_tokens[i].str)
                if self.lex_tokens[i].str.startswith('out_'):
                    self.out_symbols.add(self.lex_tokens[i].str)
                
        return d

    def gen_C(self):
        self.gen_head()
        self.symbols = self.get_symbols()
        self.gen_output_function()
        self.gen_input_function()
        self.gen_main()
        self.gen_nodes()
        return self.C_code

    def gen_head(self):  # 后续可以添加input
        head_str = "#include <stdlib.h>\n#include <stdio.h>\n#include <unistd.h>\n"
        head_str += "#define bool char\n#define ture 1\n#define false 0\nstatic int ISATTY;\n"
        self.C_code += head_str

    def gen_output_function(self):
        self.C_code += '''
void _put_bool(bool _V, char *s){
    if(ISATTY) {
        printf("%s: ", s);
        printf(_V?"true\\n":"false\\n");
    }
}
void _put_int(int _V, char *s){
    if(ISATTY) {
        printf("%s: %d\\n", s, _V);
    }
}
void _put_real(float _V, char *s){
    if(ISATTY) {
        printf("%s: %f\\n", s, _V);
    }
}
'''

    def gen_input_function(self):
        self.C_code += '''
bool _get_bool(){
    int _V;
    if(ISATTY) scanf("%d", &_V);
    return (bool)_V;
}
int _get_int(){
    int _V;
    if(ISATTY) scanf("%d", &_V);
    return _V;
}
float _get_real(){
    float _V;
    if(ISATTY) scanf("%f", &_V);
    return _V;
}
'''

    def gen_inputs(self):
        for in_symbol in self.in_symbols:
            if self.symbols[in_symbol] == 'bool':
                self.C_code += ('\t%s = _get_bool();\n' % in_symbol)
            elif self.symbols[in_symbol] == 'int':
                self.C_code += ('\t%s = _get_int();\n' % in_symbol)
            elif self.symbols[in_symbol] == 'float':
                self.C_code += ('\t%s = _get_real();\n' % in_symbol)

    def gen_outputs(self):
        for out_symbol in self.out_symbols:
            if self.symbols[out_symbol] == 'bool':
                self.C_code += ('\t_put_bool(%s, "%s");\n' % (out_symbol,out_symbol))
            elif self.symbols[out_symbol] == 'int':
                self.C_code += ('\t_put_int(%s, "%s");\n' % (out_symbol,out_symbol))
            elif self.symbols[out_symbol] == 'float':
                self.C_code += ('\t_put_real(%s, "%s");\n' % (out_symbol,out_symbol))

    def gen_main(self):
        main_start = "int main(){\n"
        self.C_code += main_start

        self.gen_def()
        self.gen_main_body()

        main_end = "\treturn 1;\n}\n"
        self.C_code += main_end


    def gen_def(self):
        self.C_code += ("\tint _s = 0;\n")
        for symbol in self.symbols.items():
            if symbol[1] == 'int':
                self.C_code += ("\tint %s;\n" % symbol[0])
            elif symbol[1] == 'real':
                self.C_code += ("\tfloat %s;\n" % symbol[0])
            elif symbol[1] == 'bool':
                self.C_code += ("\tbool %s;\n" % symbol[0])

    def gen_main_body(self):
        self.C_code += ("\tISATTY = isatty(0);\n")
        self.C_code += ("\twhile(1) {\n")
        self.C_code += ("\tif (ISATTY) printf(\"#step %d \\n\", _s++);\n")
        self.gen_inputs()
        start = 0  # TODO:finish in future 
        end = len(self.lex_status) 
        self.gen_body(start , end)
        self.gen_outputs()
        self.C_code += ("\t}\n")

    def gen_body(self, start, end):
        if start >= end:
            return
        next_start = 0
        next_end = 0
        for i in range(start, end):
            if self.lex_status[i][1] == 'let':
                next_start = i
            elif self.lex_status[i][1] == 'tel':
                next_end = i
        for i in range(next_start + 1, next_end):
            if self.lex_status[i][0] == 'Q_EquationList':
                self.gen_equationList(i+1, next_end)
            else: 
                # TODO:finish in future
                pass

    def gen_equationList(self, start, end):
        if start >= end:
            return
        next_left_start = start
        next_left_end = 0
        next_right_start = 0
        next_right_end = end
        for i in range(start, end):
            if self.lex_status[i][1] == '=':
                next_left_end = i-1
                next_right_start = i+1
                break
        left_list = self.gen_left(next_left_start, next_left_end)
        self.gen_expression_list(next_right_start, next_right_end, left_list)

    def gen_left(self, start, end):
        if start >= end:
            return
        
        left_list = set()
        for i in range(start, end):
            if self.lex_status[i][1] in self.symbols.keys():
                left_list.add(self.lex_status[i][1])
        return list(left_list)

    def gen_expression_list(self, start, end, left_list):
        if start >= end:
            return

        next_start = start
        for left in left_list:
            next_start = self.gen_expression(next_start, end, left)

    def gen_expression(self, start, end, left):
        if start >= end:
            return
        
        next_start = start
        next_end = end 
        expression_type = ""
        for i in range(start, end):
            if self.lex_status[i][1] == 'if':
                next_start = i + 1
                expression_type = "if"
            elif self.lex_status[i][1] == ',':
                next_end = i
                break
        if expression_type == 'if':
            self.gen_if(next_start, next_end, left)
        else:
            # TODO:finish in future 
            pass
        return next_end + 1

    def gen_if(self, start, end, left):
        if start >= end:
            return
        self.C_code += ("\tif(")
        self.C_code += ("in_judge")
        #TODO: self.gen_expression()
        self.C_code += ("){\n")
        self.C_code += ("\t%s = 20;\n" % str(left))
        #TODO: self.gen_expression()
        self.C_code += ("\t} else {\n")
        self.C_code += ("\t%s = 30;\n"  % str(left))
        #TODO: self.gen_expression()
        self.C_code += ("\t}\n")


    def gen_nodes(self):
        # TODO:finish in future 
        pass