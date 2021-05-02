import sys
import syntax
import execute
import typecheck
from typecheck import tpcheck
from execute import flag

for line in syntax.read_lines("> "):
    try:
        if(line == "quit"):
            exit(0)
        flag = 0
        t = syntax.parse_term(line)
        tp = tpcheck(t)
        if (tp == "Bool" or tp == "Nat"):
            print(execute.eval_term(t))
    except syntax.ParseError as e:
        print("error: {}".format(e))
