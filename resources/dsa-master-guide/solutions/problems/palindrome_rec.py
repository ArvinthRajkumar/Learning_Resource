def palindrome_rec(s):
    if len(s) < 2:
        return True
    return s[0] == s[-1] and palindrome_rec(s[1:-1])
