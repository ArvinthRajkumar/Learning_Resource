import random
random.seed(1)
def z_function(s):
    n, z, l, r = len(s), [0] * len(s), 0, 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i, i + z[i]
    return z
def z_naive(s):
    return [0] + [next((k for k in range(len(s) - i + 1) if k == len(s) - i or s[k] != s[i + k]), 0) for i in range(1, len(s))]
for _ in range(300):
    s = "".join(random.choice("ab") for _ in range(random.randint(1, 20)))
    assert z_function(s) == z_naive(s)
print("Z function verified; example:", z_function("aabxaabxcaabxaabxay"))
