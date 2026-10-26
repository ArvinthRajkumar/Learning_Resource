from functools import lru_cache

@lru_cache(maxsize=None)
def climb(n):
    return 1 if n <= 1 else climb(n - 1) + climb(n - 2)
