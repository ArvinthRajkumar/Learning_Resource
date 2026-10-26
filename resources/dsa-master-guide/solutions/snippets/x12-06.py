from functools import lru_cache
calls = 0
def fib_slow(n):
    global calls; calls += 1
    return n if n < 2 else fib_slow(n - 1) + fib_slow(n - 2)
@lru_cache(None)
def fib_fast(n): return n if n < 2 else fib_fast(n - 1) + fib_fast(n - 2)
result = fib_slow(25); fast = fib_fast(25)
print("fib(25) =", result, "| equal:", result == fast, "| took", calls, "calls without memory; with memory only", fib_fast.cache_info().misses, "distinct problems are solved")
