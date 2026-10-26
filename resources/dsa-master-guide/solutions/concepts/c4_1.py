def is_palindrome(s):
    lo, hi = 0, len(s) - 1
    while lo < hi:
        if s[lo] != s[hi]:      # mismatch -> not a palindrome
            return False
        lo += 1
        hi -= 1
    return True
