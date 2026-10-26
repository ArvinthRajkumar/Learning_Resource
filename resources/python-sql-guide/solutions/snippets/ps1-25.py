d = {"a": 1, "b": 2}
d["c"] = 3
del d["a"]
d["a"] = 9
print(list(d))
try:
    for k in d:
        d[k + "x"] = 0
except RuntimeError as e:
    print("RuntimeError:", e)
