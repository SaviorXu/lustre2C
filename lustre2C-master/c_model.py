
def not_model(args, types):
    code = '''{t} not_function_{t}({t} {s1}){{
        return !{s1};
    }}
    '''.format(s1=args,t=types)
    return code


def neg_model(args, types):
    code = '''{t} neg_function_{t}({t} {s1}){{
        return -{s1};
    }}
    '''.format(s1=args,t=types)
    return code

def if_model(args1, args2, args3, types):
    code = '''{t} if_function_{t}(int {s1}, {t} {s2}, {t} {s3}){{
        if({s1})
            return {s2};
        else
            return {s3};
    }}'''.format(s1=args1, s2=args2, s3=args3, t=types)
    return code
