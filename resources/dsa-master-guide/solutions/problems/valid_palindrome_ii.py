def valid_palindrome_ii(s):
    def ok(lo, hi):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:
            return ok(lo + 1, hi) or ok(lo, hi - 1)
        lo += 1
        hi -= 1
    return True
