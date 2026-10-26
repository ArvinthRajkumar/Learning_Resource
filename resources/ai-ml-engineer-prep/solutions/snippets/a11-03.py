import random, math
random.seed(2)
a = [random.gauss(100, 15) for _ in range(40)]
b = [random.gauss(108, 15) for _ in range(40)]
def welch_t(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    vx = sum((v - mx) ** 2 for v in x) / (len(x) - 1)
    vy = sum((v - my) ** 2 for v in y) / (len(y) - 1)
    return (my - mx) / math.sqrt(vx / len(x) + vy / len(y))
t = welch_t(a, b)
# permutation test: shuffle group labels many times
obs = abs(sum(b) / len(b) - sum(a) / len(a))
pool, count = a + b, 0
for _ in range(5000):
    random.shuffle(pool)
    if abs(sum(pool[40:]) / 40 - sum(pool[:40]) / 40) >= obs:
        count += 1
print("Welch t = %.2f, permutation p-value = %.4f" % (t, count / 5000))
