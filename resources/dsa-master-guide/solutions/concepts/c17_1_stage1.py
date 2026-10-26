def count_bits(n):
    c = 0
    while n:
        c += n & 1
        n >>= 1
    return c
