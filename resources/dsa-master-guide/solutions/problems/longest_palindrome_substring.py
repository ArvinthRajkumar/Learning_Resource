def longest_palindrome_substring(s):
    best = ""
    def expand(lo, hi):
        while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return s[lo + 1:hi]            # last valid palindrome
    for i in range(len(s)):
        for cand in (expand(i, i), expand(i, i + 1)):   # odd and even centres
            if len(cand) > len(best):
                best = cand
    return best
