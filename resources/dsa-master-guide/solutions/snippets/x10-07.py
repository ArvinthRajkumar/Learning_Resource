from functools import lru_cache
@lru_cache(None)
def wins(n):                                                   # take 1, 2 or 3 stones; taking the last stone wins
    return any(not wins(n - k) for k in (1, 2, 3) if k <= n)
print("losing positions (multiples of 4):", [n for n in range(0, 21) if not wins(n)])
