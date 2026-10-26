import random, math
random.seed(3)
def acf(x, max_lag):
    m = sum(x) / len(x); var = sum((v - m) ** 2 for v in x)
    return [sum((x[i] - m) * (x[i + k] - m) for i in range(len(x) - k)) / var for k in range(max_lag + 1)]
n = 400
white = [random.gauss(0, 1) for _ in range(n)]
walk = [0.0]
for _ in range(n - 1): walk.append(walk[-1] + random.gauss(0, 1))
weekly = [math.sin(2 * math.pi * t / 7) + random.gauss(0, 0.3) for t in range(n)]
diff = [walk[i] - walk[i - 1] for i in range(1, n)]
for name, s in [("white noise", white), ("random walk", walk), ("weekly season", weekly), ("differenced walk", diff)]:
    a = acf(s, 8)
    print(f"{name:>17}: ACF lags 1..8 =", [round(v, 2) for v in a[1:]])
