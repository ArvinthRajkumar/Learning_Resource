from functools import lru_cache
def edit_distance(a, b):
    prev = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        cur = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] != b[j - 1]))
        prev = cur
    return prev[-1]
def lcs(a, b):
    @lru_cache(None)
    def go(i, j):
        if i == len(a) or j == len(b): return 0
        if a[i] == b[j]: return 1 + go(i + 1, j + 1)
        return max(go(i + 1, j), go(i, j + 1))
    return go(0, 0)
print(edit_distance("kitten", "sitting"), edit_distance("", "abc"), lcs("ABCBDAB", "BDCABA"))
