def merge(a, b): return {k: max(a.get(k, 0), b.get(k, 0)) for k in sorted(a.keys() | b.keys())}
def compare(a, b):
    keys = a.keys() | b.keys()
    le = all(a.get(k, 0) <= b.get(k, 0) for k in keys)
    ge = all(a.get(k, 0) >= b.get(k, 0) for k in keys)
    return "equal" if le and ge else "before" if le else "after" if ge else "CONCURRENT"
v1 = {"A": 1}                         # write on node A
v2 = merge(v1, {"B": 1})              # B saw v1 then wrote
v3 = {"A": 2}                         # A wrote again without seeing B's write
print("v1 vs v2:", compare(v1, v2))
print("v2 vs v3:", compare(v2, v3), "-> a genuine conflict that the application must merge")
print("merged:", merge(v2, v3))
