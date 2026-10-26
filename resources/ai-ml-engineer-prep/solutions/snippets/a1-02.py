import random
random.seed(1)
xs = [random.gauss(0, 1) for _ in range(20)]
ys = [3.0 * x + random.gauss(0, 2) for x in xs]
mx, my = sum(xs) / 20, sum(ys) / 20
cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / 20
var = sum((x - mx) ** 2 for x in xs) / 20
for lam in (0, 0.5, 2, 10):
    print("lambda %4.1f -> slope %.3f" % (lam, cov / (var + lam)))
