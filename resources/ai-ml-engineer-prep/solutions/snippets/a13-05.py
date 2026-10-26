import random, math
random.seed(5)
n = 300
x = [20 + 0.05 * t + 6 * math.sin(2 * math.pi * t / 24) + random.gauss(0, 1) for t in range(n)]      # hourly-like with a 24-step cycle
def features(series, t):                                       # only information available before time t
    window = series[max(0, t - 24):t]
    return [series[t - 1], series[t - 24], sum(window) / len(window), t % 24]
rows = [(features(x, t), x[t]) for t in range(48, n)]
split = int(len(rows) * 0.8)
train, test = rows[:split], rows[split:]
def knn_predict(train, f, k=5):
    near = sorted(train, key=lambda r: sum((a - b) ** 2 for a, b in zip(r[0], f)))[:k]
    return sum(r[1] for r in near) / k
pred = [knn_predict(train, f) for f, _ in test]
mae = lambda a, b: sum(abs(p - q) for p, q in zip(a, b)) / len(a)
seasonal_naive = [f[1] for f, _ in test]                       # feature 1 is the value 24 steps ago
print(f"nearest-neighbour regression on lag features MAE {mae([t for _, t in test], pred):.2f} | seasonal naive MAE {mae([t for _, t in test], seasonal_naive):.2f}")
