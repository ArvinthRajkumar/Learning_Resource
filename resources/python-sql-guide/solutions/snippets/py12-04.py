import sys
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n): return n if n < 2 else fib(n - 1) + fib(n - 2)
print("fib(80) with memoisation:", fib(80), "| cache info:", fib.cache_info().misses, "misses")
def depth(n): return 0 if n == 0 else 1 + depth(n - 1)
print("recursion limit is about", sys.getrecursionlimit() // 100 * 100)
try: depth(1_000_000)
except RecursionError: print("RecursionError for depth one million, so iterate or use an explicit stack")
def depth_iter(n):
    stack, d = [n], 0
    while stack:
        x = stack.pop()
        if x: stack.append(x - 1); d += 1
    return d
print("iterative version handles it:", depth_iter(1_000_000))
