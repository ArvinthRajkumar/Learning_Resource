a = [1, 2, 3]
b = a                       # binds a second name to the same list
b.append(4)
print("a:", a, "| same object:", a is b, "| equal copy is a different object:", a is list(a), a == list(a))
x = 10
def show(n): return id(n) == id(x)
print("function parameters bind to the same object:", show(x))
print("types:", type(3).__name__, type(len).__name__, type(type).__name__, type(None).__name__, "| a function is an object with attributes:", hasattr(show, "__code__"))
