import syntax
import execute
import typecheck
from typecheck import tpcheck

for line in syntax.read_lines("> "):
    try:
        if(line == "quit"):
            exit(0)
        t = syntax.parse_term(line)
        tp = tpcheck(t)
        if (tp == "Bool" or tp == "Nat"):
            print(execute.evaluation(t))
    except syntax.ParseError as e:
        print("error: {}".format(e))
