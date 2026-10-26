import random, math
random.seed(1)
d, N = 16, 3000
data = [[random.gauss(0, 1) for _ in range(d)] for _ in range(N)]
q = [random.gauss(0, 1) for _ in range(d)]
dist = lambda a, b: math.dist(a, b)
exact = sorted(range(N), key=lambda i: dist(q, data[i]))[:5]
print("exact top-5:", exact, "(comparisons:", N, ")")
