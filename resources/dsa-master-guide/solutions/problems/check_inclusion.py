from collections import Counter

def check_inclusion(s1, s2):
    k = len(s1)
    if k > len(s2):
        return False
    need = Counter(s1)
    window = Counter(s2[:k])
    if window == need:
        return True
    for i in range(k, len(s2)):
        window[s2[i]] += 1                 # letter enters
        out = s2[i - k]
        window[out] -= 1                   # letter leaves
        if window[out] == 0:
            del window[out]
        if window == need:
            return True
    return False
