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
		#print(t[1:])
		if tpcheck(t[1])=="Nat":
			return "Nat"
		else:
			print("Non numerical argument to "+t[0])
			return "None"
	elif t[0]=="iszero":
		if tpcheck(t[1])=="Nat":
			return "Bool"
		else:
			print("Non numerical argument to "+t[0])
