import random
random.seed(2)
MOD = (1 << 61) - 1
def rabin_karp(text, pat):
    n, m = len(text), len(pat)
    if m > n: return []
    base = random.randrange(256, MOD - 1)
    hp = ht = 0
    for i in range(m):
        hp = (hp * base + ord(pat[i])) % MOD
        ht = (ht * base + ord(text[i])) % MOD
    top = pow(base, m - 1, MOD)
    out = []
    for i in range(n - m + 1):
        if hp == ht and text[i:i + m] == pat: out.append(i)
        if i + m < n:
            ht = ((ht - ord(text[i]) * top) * base + ord(text[i + m])) % MOD
    return out
def naive(text, pat): return [i for i in range(len(text) - len(pat) + 1) if text.startswith(pat, i)]
for _ in range(300):
    text = "".join(random.choice("abc") for _ in range(random.randint(0, 30)))
    pat = "".join(random.choice("abc") for _ in range(random.randint(1, 4)))
    assert rabin_karp(text, pat) == naive(text, pat)
print("Rabin-Karp matches naive search")
