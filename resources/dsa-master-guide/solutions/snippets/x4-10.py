def is_rotation(s, t):
    return len(s) == len(t) and t in s + s
def shortest_palindrome(s):
    r = s[::-1]
    comb = s + "#" + r
    pi, k = [0] * len(comb), 0
    for i in range(1, len(comb)):
        while k and comb[i] != comb[k]: k = pi[k - 1]
        if comb[i] == comb[k]: k += 1
        pi[i] = k
    return r[:len(s) - pi[-1]] + s
print(is_rotation("waterbottle", "erbottlewat"), is_rotation("abc", "acb"))
print(shortest_palindrome("aacecaaa"), shortest_palindrome("abcd"))
