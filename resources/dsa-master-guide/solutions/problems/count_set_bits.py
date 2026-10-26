def count_set_bits(n):
    count = 0
    while n:
        n &= n - 1        # clear lowest set bit
        count += 1
    return count
