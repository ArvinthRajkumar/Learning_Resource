def palindrome_number(n):
    if n < 0:
        return False
    original, rev = n, 0
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == original
