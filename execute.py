import collections
import syntax

def flatten(L):
    if(type(L) != list):
        return [L]
    if len(L) == 1:
        if type(L[0]) == list:
            result = flatten(L[0])
        else:
            result = L
    elif type(L[0]) == list:
        result = flatten(L[1:])
        result = flatten(L[0]) + result
    else:
        if L[0] == "if":
            res1 = flatten(L[1])
            res2 = flatten(L[2])
            res3 = flatten(L[3])
            result = ["if", "("] + res1 + [")", "then", "("] + \
                res2 + [")", "else", "("]+res3+[")"]
            return result
        elif L[0] == "and":
            res1 = flatten(L[1])
            res2 = flatten(L[2])
            res3 = flatten(L[3])
            result = ["and", "("] + res1 + [")", "or", "("] + \
                res2 + [")", "not", "("]+res3+[")"]
            return result
        else:
            result = flatten(L[1:])
            result = [L[0],"("] + result + [")"]
    return result


def listToString(s):

    if isinstance(s, (str)):
        return s
    # initialize an empty string
    str1 = " "
    s1 = flatten(s)
    # return string
    return (str1.join(s1))


def eval_term(t):
    if t == 'true' or t == True:
        return 'true'
    elif t == 'false' or t == False:
        return 'false'
    elif t == '0':
        return '0'

    #iszero t
    elif t[0] == 'iszero':
        val = (eval_term(t[1]))
        if (val == 0 or val == '0' or val == '( 0 )'):
            return 'true'
        elif val[-4:] == "true" or val[-5:] == "false":
            s = ['iszero', str(val)]
            return listToString(s)
        else:
            return 'false'

    #succ t
    elif t[0] == 'succ':
        val = (eval_term(t[1]))
        s = ['succ', str(val)]
        return (listToString(s))
    
    #pred t
    elif t[0] == 'pred':
        s = (eval_term(t[1]))
        if s == 0 or s == '0' or s == '( 0 )':
            return '0'
        elif s[:4] == 'succ':
            if s[5:] == '( 0 )':
                return '0'
            else:
                return s[5:]
        else:
            s = ['pred', str(s)]
            return (listToString(s))

    #and t or t not t
    elif t[0] == 'and':
        t1 = eval_term(t[1])
        if t1 == "false":
            return "false"
        elif t1 == "true":
            t2 = eval_term(t[2])
            if t2 == "true":
                return "true"
            elif t2 == "false":
                t3 = eval_term(t[3])
                if t3 == "true":
                    return "false"
                elif t3 == "false":
                    return "true"
                else:
                    return "and("+t1+")or("+t2+")not("+t3+")"
            else:
                return "and("+t1+")or("+t2+")not("+listToString(t[3])+")"
        else:
            return "and("+t1+")or("+listToString(t[2])+")not("+listToString(t[3])+")"

    #if-then-else
    elif t[0] == 'if':
        val = eval_term(t[1])
        if val == 'true':
            return eval_term(t[2])
        elif val == 'false':
            return eval_term(t[3])
        else:
            two = ""
            three = ""
            if(t[2] == "true" or t[2] == "false" or t[2] == "0"):
                two = t[2]
            else:
                two = listToString(t[2])

            if(t[3] == "true" or t[3] == "false" or t[3] == "0"):
                three = t[3]
            else:
                three = listToString(t[3])
            return (t[0]+"("+val+")"+"then"+"("+two+")"+"else"+"("+three+")")
    
    #others
    else:
        return listToString(t)
