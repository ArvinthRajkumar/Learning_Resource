def smallest_period(s):
    pi = [0] * len(s)
    k = 0
    for i in range(1, len(s)):
        while k and s[i] != s[k]: k = pi[k - 1]
        if s[i] == s[k]: k += 1
        pi[i] = k
    p = len(s) - pi[-1]
    return p if len(s) % p == 0 else len(s)
print(smallest_period("abcabcabc"), smallest_period("abcab"), smallest_period("aaaa"))
