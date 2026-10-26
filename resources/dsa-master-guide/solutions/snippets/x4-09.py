import bisect
def suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])
def lcp_array(s, sa):
    n, rank, lcp, h = len(s), [0] * len(s), [0] * len(s), 0
    for i, p in enumerate(sa): rank[p] = i
    for i in range(n):                       # Kasai: O(n) longest common prefix of neighbours
        if rank[i] > 0:
            j = sa[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]: h += 1
            lcp[rank[i]] = h
            if h: h -= 1
        else:
            h = 0
    return lcp
def count_occurrences(s, sa, pat):
    suffixes = [s[i:i + len(pat)] for i in sa]
    return bisect.bisect_right(suffixes, pat) - bisect.bisect_left(suffixes, pat)
s = "banana"
sa = suffix_array(s)
print("suffix array:", sa, [s[i:] for i in sa])
lcp = lcp_array(s, sa)
print("LCP array   :", lcp, "| longest repeated substring length:", max(lcp))
print("occurrences of 'ana':", count_occurrences(s, sa, "ana"), "| of 'an':", count_occurrences(s, sa, "an"))
