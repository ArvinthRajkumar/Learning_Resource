def count_bits(n):
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c
