import math, random
random.seed(2)
s, ab = 2.0, 0.4
v = ab * s * s + 1 - ab
analytic = math.sqrt(1 - ab) / v
xs, es = [], []
for _ in range(200000):
    x0, e = random.gauss(0, s), random.gauss(0, 1)
    xs.append(math.sqrt(ab) * x0 + math.sqrt(1 - ab) * e)
    es.append(e)
coef = sum(x * e for x, e in zip(xs, es)) / sum(x * x for x in xs)    # least-squares slope of eps on x_t
print("analytic coefficient %.4f, regression %.4f" % (analytic, coef))
