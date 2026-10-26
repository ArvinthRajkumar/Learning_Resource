import random
random.seed(3)
def manacher(s):
    t = "^#" + "#".join(s) + "#$"
    n, p, centre, right = len(t), [0] * len(t), 0, 0
    for i in range(1, n - 1):
        if i < right:
            p[i] = min(right - i, p[2 * centre - i])
        while t[i + 1 + p[i]] == t[i - 1 - p[i]]:
            p[i] += 1
        if i + p[i] > right:
            centre, right = i, i + p[i]
    best = max(range(1, n - 1), key=lambda i: p[i])
    start = (best - p[best]) // 2
    return s[start:start + p[best]]
def brute(s):
    best = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            sub = s[i:j + 1]
            if sub == sub[::-1] and len(sub) > len(best): best = sub
    return best
for _ in range(300):
    s = "".join(random.choice("ab") for _ in range(random.randint(1, 14)))
    assert len(manacher(s)) == len(brute(s))
print("Manacher finds a longest palindrome of the right length;", manacher("forgeeksskeegfor"))
