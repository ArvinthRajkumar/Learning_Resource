import random, itertools
from fractions import Fraction
random.seed(1)
# expected number of fixed points of a random permutation, exactly
n = 6
total = sum(sum(p[i] == i for i in range(n)) for p in itertools.permutations(range(n)))
print("E[fixed points] =", Fraction(total, 720))
# reservoir sampling is uniform
counts = [0] * 5
for _ in range(50000):
    pick = None
    for i, x in enumerate(range(5)):
        if random.randrange(i + 1) == 0: pick = x
    counts[pick] += 1
print("reservoir counts (each near 10000):", counts)
# coupon collector expectation for n = 5: n * H_n
print("coupon collector n=5:", float(sum(Fraction(5, k) for k in range(1, 6))))
