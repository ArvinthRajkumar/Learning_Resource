import random, math
random.seed(1)
true_p, n, trials, covered = 0.7, 200, 2000, 0
for _ in range(trials):
    x = sum(random.random() < true_p for _ in range(n))
    p = x / n
    se = math.sqrt(p * (1 - p) / n)
    if p - 1.96 * se <= true_p <= p + 1.96 * se:
        covered += 1
print("coverage of 95%% intervals: %.1f%%" % (100 * covered / trials))
def wilson(x, n, z=1.96):
    p = x / n; d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(c - h, 3), round(c + h, 3)
print("accuracy 95/100 -> Wilson interval", wilson(95, 100))
print("accuracy 950/1000 -> Wilson interval", wilson(950, 1000))
