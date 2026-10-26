import dis
def add(a, b): return a + b
ops = [i.opname for i in dis.get_instructions(add)]
print("add() uses a small stack machine; instruction kinds include load and return:", any(o.startswith("LOAD") for o in ops), any("RETURN" in o for o in ops))
code = add.__code__
print("argument names:", code.co_varnames, "| argument count:", code.co_argcount, "| constants:", code.co_consts)
