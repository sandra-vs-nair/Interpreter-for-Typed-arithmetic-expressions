import sys
import os
import collections
import re
import syntax


def tpcheck(t):
    if t=="true" or t=="false":
        return "Bool"
    elif t=="0" or t[0]=='0':
        return "Nat"
    elif t[0]=="succ" or t[0]=="pred":
        if tpcheck(t[1])=="Nat":
            return "Nat"
        else:
            print("Expected numerical argument to "+t[0])
            return "None"
    elif t[0]=="iszero":
        if tpcheck(t[1])=="Nat":
            return "Bool"
        else:
            print("Expected numerical argument to "+t[0])
            return "None"
    elif t[0] == 'if':
        guard = tpcheck(t[1])
        if guard != 'Bool':
            print("Expected bool guard for if conditional")
            return "None"
        else:
            arm1 = tpcheck(t[2])
            arm2 = tpcheck(t[3])
            if arm1 != "None" and arm1 == arm2:
                return arm1
            else:
                print("Expected same type for both arms in if conditional")
                return "None"
    elif t[0] == "and":
        t1 = tpcheck(t[1])
        t2 = tpcheck(t[2])
        t3 = tpcheck(t[3])

        if(t1 != "Bool" or t2 != "Bool" or t3 != "Bool"):
            print("Expected bool arguments for and-or-not operator")
            return "None"
        else:
            return "Bool"
