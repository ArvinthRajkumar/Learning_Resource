def square(n): return n * n
ops = {"sq": square, "neg": lambda n: -n}
print([ops[k](5) for k in ops])
print(sorted(["bb", "a", "ccc"], key=len), list(map(square, [1, 2, 3])))
