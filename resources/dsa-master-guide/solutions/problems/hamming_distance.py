def hamming_distance(x, y):
    diff = x ^ y
    count = 0
    while diff:
        diff &= diff - 1       # clear the lowest set bit
        count += 1
    return count
