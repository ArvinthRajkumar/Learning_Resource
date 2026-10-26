import inspect
def f(a, b=2, *args, **kw): ...
print(inspect.signature(f))
print(hasattr("x", "upper"), getattr("x", "upper")(), [n for n in dir(1) if n.startswith("bit")])
print(type(f).__name__, f.__name__, callable(f))
