from collections import Counter

def four_sum_count(a, b, c, d):
    ab = Counter(x + y for x in a for y in b)
    return sum(ab[-(x + y)] for x in c for y in d)
