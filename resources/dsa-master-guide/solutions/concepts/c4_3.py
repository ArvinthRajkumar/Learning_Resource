def rabin_karp(text, pat, base=256, mod=1_000_003):
    n, m = len(text), len(pat)
    if m > n:
        return []
    high = pow(base, m - 1, mod)           # weight of the leftmost char
    hp = ht = 0
    for i in range(m):
        hp = (hp * base + ord(pat[i])) % mod
        ht = (ht * base + ord(text[i])) % mod
    res = []
    for i in range(n - m + 1):
        if hp == ht and text[i:i + m] == pat:   # verify to rule out collisions
            res.append(i)
        if i < n - m:                           # roll the window one step
            ht = ((ht - ord(text[i]) * high) * base + ord(text[i + m])) % mod
    return res
