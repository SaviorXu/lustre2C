from inspect import stack
import sys
import cfg
import generate
# from lustre_lex import lexer
from c_lex import lexer


debug = False

def token2str(token):
    if hasattr(token, 'str'):
        return token.str
    else:
        return token.value

class Recognition():

    def __init__(self, pda, tokens, empty):
        self.pda = pda
        self.stack = list()
        self.tokens = tokens
        self.used = list()
        self.empty = empty
        self.Code = ''
        # self.context = ''
        # self.contextList = list()

    # only accept final state
    def is_accept(self, cur_state, token_index):

        if debug:
            print("cur_state :" + cur_state)
        if cur_state.strip() == cfg.END:
            self.used.append(cur_state)
            return True
        if token_index == len(self.tokens):
            if cur_state.strip() == 'Q_loop' and self.stack[-1] == 'Δ':
                self.used.append(cur_state)
                return True
            if self.stack[-1] in self.empty:
                j = len(self.stack) - 1
                while j > 0 and self.stack[j] != 'Δ' and self.stack[j] in self.empty:
                    j -= 1
                if self.stack[j] == 'Δ':
                    return True
            return False

        cur_stack = self.stack.copy()
        cur_Code = self.Code
        useful_token = self.tokens[token_index]
        for state in self.pda.states[cur_state]:
            cur_token = self.tokens[token_index].value.strs
            if state.read.strip() == cur_token or state.read.strip() == cfg.EPS:
                tmp_index = token_index if state.read.strip() == cfg.EPS else token_index + 1
                if state.action.strip() == 'POP' and len(self.stack) and state.value.strip() == self.stack[-1].strip():
                    if debug:
                        print("=========pop")
                        print(cur_state)
                        print(state)
                        print(self.stack)
                        print(self.tokens[token_index])
                    # first = True
                    # for i in self.contextList:
                    #     if first:
                    #         self.context += i
                    #         self.context += " -> "
                    #         first = False
                    #     else:
                    #         self.context += i
                    #         self.context += " "
                    # self.context += "\n"
                    # self.contextList.clear()
                    # self.contextList.append(state.value)
                    self.stack.pop()
                    if self.is_accept(state.next, tmp_index):
                        self.used.append((cur_state, useful_token,state.action,state.value))
                        if tmp_index != token_index:
                            self.Code += str(useful_token.value.value) + '--'

                        return True
                    else:
                        self.stack = cur_stack.copy()

                elif state.action.strip() == 'PUSH':
                    if debug:
                        print("=========push")
                        print(cur_state)
                        print(state)
                        print(self.stack)
                        print(self.tokens[token_index])
                    # self.contextList.append(state.value)
                    self.stack.append(state.value)
                    if self.is_accept(state.next, tmp_index):
                        self.used.append((cur_state, useful_token,state.action,state.value))
                        return True
                    else:
                        self.stack = cur_stack.copy()

        return False


def unique_list(list_var):
    s = set()
    res = list()
    for v in reversed(list_var):
        if v not in s:
            res.append(v)
            s.add(v)
    return res

