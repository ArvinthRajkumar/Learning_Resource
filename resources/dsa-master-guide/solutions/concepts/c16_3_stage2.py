from functools import lru_cache

def lcs(a, b):
    @lru_cache(maxsize=None)
    def go(i, j):
        if i == 0 or j == 0:
            return 0
        if a[i - 1] == b[j - 1]:
            return 1 + go(i - 1, j - 1)
        return max(go(i - 1, j), go(i, j - 1))
    return go(len(a), len(b))
