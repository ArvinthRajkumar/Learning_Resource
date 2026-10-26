import random, math
random.seed(2)
period, n = 7, 120
y = [100 + 0.3 * t + 12 * math.sin(2 * math.pi * (t % period) / period) + random.gauss(0, 2) for t in range(n)]
train, test = y[:100], y[100:]
def mae(a, b): return sum(abs(p - q) for p, q in zip(a, b)) / len(a)
naive = [train[-1]] * len(test)
seasonal_naive = [train[len(train) - period + (i % period)] for i in range(len(test))]
def ses(x, alpha):
    level = x[0]
    for v in x[1:]: level = alpha * v + (1 - alpha) * level
    return level
ses_fc = [ses(train, 0.3)] * len(test)
def holt_winters(x, period, alpha=0.3, beta=0.05, gamma=0.3, horizon=20):
    level, trend = sum(x[:period]) / period, (sum(x[period:2 * period]) - sum(x[:period])) / period ** 2
    season = [x[i] - level for i in range(period)]
    for t in range(period, len(x)):
        last_level = level
        level = alpha * (x[t] - season[t % period]) + (1 - alpha) * (level + trend)
        trend = beta * (level - last_level) + (1 - beta) * trend
        season[t % period] = gamma * (x[t] - level) + (1 - gamma) * season[t % period]
    return [level + (h + 1) * trend + season[(len(x) + h) % period] for h in range(horizon)]
hw = holt_winters(train, period, horizon=len(test))
for name, fc in [("naive", naive), ("seasonal naive", seasonal_naive), ("simple exp. smoothing", ses_fc), ("Holt-Winters", hw)]:
    print(f"{name:>22}: MAE {mae(test, fc):6.2f}")
