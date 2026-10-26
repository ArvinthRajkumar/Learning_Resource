def report(first, *args, sep="-", **kwargs):
    print(first, args, kwargs, sep)
report(1, 2, 3, sep="+", color="red", size=3)

def add(a, b): return a + b
nums = (4, 5)
opts = {"a": 1, "b": 2}
print(add(*nums), add(**opts))
