from collections import Counter

def find_all_anagrams(s, p):
    k = len(p)
    need = Counter(p)
    window = Counter(s[:k - 1])
    res = []
    for i in range(k - 1, len(s)):
        window[s[i]] += 1
        if window == need:
            res.append(i - k + 1)
        out = s[i - k + 1]
        window[out] -= 1
        if window[out] == 0:
            del window[out]
    return res
