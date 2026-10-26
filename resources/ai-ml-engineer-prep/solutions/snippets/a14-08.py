import random, math
random.seed(6)
def truth(x): return 2 * x + 1
xs = [random.uniform(0, 10) for _ in range(3000)]
data = [(x, truth(x) + random.gauss(0, 1 + 0.2 * x)) for x in xs]
train, calib, test = data[:1000], data[1000:2000], data[2000:]
n = len(train); mx = sum(x for x, _ in train) / n; my = sum(y for _, y in train) / n
slope = sum((x - mx) * (y - my) for x, y in train) / sum((x - mx) ** 2 for x, _ in train); icpt = my - slope * mx
predict = lambda x: slope * x + icpt
scores = sorted(abs(y - predict(x)) for x, y in calib)
alpha = 0.1
q = scores[min(len(scores) - 1, math.ceil((len(scores) + 1) * (1 - alpha)) - 1)]
covered = sum(abs(y - predict(x)) <= q for x, y in test) / len(test)
print(f"fitted line: y = {slope:.2f} x + {icpt:.2f} | conformal half-width {q:.2f} | coverage on fresh data {covered:.1%} (target 90%)")
