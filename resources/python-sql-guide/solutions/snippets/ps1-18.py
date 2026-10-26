from functools import reduce
def compose(*fns):
    return reduce(lambda f, g: lambda x: g(f(x)), fns)
pipeline = compose(str.strip, str.lower, lambda s: s.replace(" ", "-"))
print(pipeline("  Hello Big World  "))
