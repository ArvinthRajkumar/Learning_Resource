def find_all(text, pat):
    n, m = len(text), len(pat)
    if m == 0:
        return []
    lps = [0] * m                      # build the KMP failure table
    k = 0
    for i in range(1, m):
        while k > 0 and pat[i] != pat[k]:
            k = lps[k - 1]
        if pat[i] == pat[k]:
            k += 1
        lps[i] = k
    res, k = [], 0
    for i in range(n):                 # scan text, never move i backwards
        while k > 0 and text[i] != pat[k]:
            k = lps[k - 1]
        if text[i] == pat[k]:
            k += 1
        if k == m:
            res.append(i - m + 1)
            k = lps[k - 1]
    return res
