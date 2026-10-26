import functools

def retry(times):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **k):
            for attempt in range(1, times + 1):
                try:
                    return fn(*a, **k)
                except ValueError as e:
                    print("attempt", attempt, "failed:", e)
            raise RuntimeError("gave up")
        return wrapper
    return deco

calls = {"n": 0}
@retry(3)
def flaky():
    calls["n"] += 1
    if calls["n"] < 3:
        raise ValueError("not yet")
    return "ok"
print(flaky())

@functools.lru_cache(maxsize=None)
def fib(n): return n if n < 2 else fib(n - 1) + fib(n - 2)
print(fib(80), fib.cache_info().hits > 0)
