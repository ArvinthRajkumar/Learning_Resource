import functools

def cache_with_ttl(ttl, clock):
    def deco(fn):
        store = {}
        @functools.wraps(fn)
        def wrapper(*args):
            now = clock()
            if args in store and now - store[args][1] < ttl:
                return store[args][0]
            value = fn(*args)
            store[args] = (value, now)
            return value
        return wrapper
    return deco

t = [0]
calls = []
@cache_with_ttl(10, lambda: t[0])
def slow(x):
    calls.append(x)
    return x * 2

print(slow(2), slow(2), len(calls))
t[0] = 11                                  # time passes
print(slow(2), len(calls))
