import random, math
random.seed(5)
pts = [(random.gauss(0, 0.5), random.gauss(0, 0.5)) for _ in range(40)] + [(random.gauss(4, 0.5), random.gauss(4, 0.5)) for _ in range(40)]
cent = [pts[0], pts[1]]
for _ in range(10):
    groups = [[], []]
    for p in pts:
        groups[min((0, 1), key=lambda i: math.dist(p, cent[i]))].append(p)
    cent = [(sum(x for x, _ in g) / len(g), sum(y for _, y in g) / len(g)) for g in groups]
print("centroids:", [(round(x, 2), round(y, 2)) for x, y in cent], "sizes:", [len(g) for g in groups])
