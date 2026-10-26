def prefix_function(s):
    pi = [0] * len(s)
    k = 0
    for i in range(1, len(s)):
        while k and s[i] != s[k]:
            k = pi[k - 1]                   # fall back to a shorter border
        if s[i] == s[k]:
            k += 1
        pi[i] = k
    return pi
print(prefix_function("abacabab"))
print(prefix_function("aaaa"))
