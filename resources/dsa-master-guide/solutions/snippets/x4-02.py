import random
random.seed(0)
def kmp_search(text, pat):
    pi, k, out = prefix_function(pat), 0, []
    for i, ch in enumerate(text):
        while k and ch != pat[k]:
            k = pi[k - 1]
        if ch == pat[k]:
            k += 1
        if k == len(pat):
            out.append(i - k + 1)
            k = pi[k - 1]
    return out
def prefix_function(s):
    pi, k = [0] * len(s), 0
    for i in range(1, len(s)):
        while k and s[i] != s[k]: k = pi[k - 1]
        if s[i] == s[k]: k += 1
        pi[i] = k
    return pi
def naive(text, pat):
    return [i for i in range(len(text) - len(pat) + 1) if text.startswith(pat, i)]
for _ in range(400):
    text = "".join(random.choice("ab") for _ in range(random.randint(0, 25)))
    pat = "".join(random.choice("ab") for _ in range(random.randint(1, 5)))
    assert kmp_search(text, pat) == naive(text, pat)
print("KMP matches naive search on 400 random cases (including overlaps)")
