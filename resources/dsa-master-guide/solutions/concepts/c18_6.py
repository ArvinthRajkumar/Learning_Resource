def build_lps(pat):
    lps = [0] * len(pat)
    k = 0
    for i in range(1, len(pat)):
        while k > 0 and pat[i] != pat[k]:
            k = lps[k - 1]               # fall back
        if pat[i] == pat[k]:
            k += 1
        lps[i] = k
    return lps
