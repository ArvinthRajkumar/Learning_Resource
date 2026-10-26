import random, math
random.seed(6)
period, n = 7, 160
y = [100 + 0.2 * t + 10 * math.sin(2 * math.pi * (t % period) / period) + random.gauss(0, 2) for t in range(n)]
def seasonal_naive(train, h): return [train[len(train) - period + (i % period)] for i in range(h)]
def mean_forecast(train, h): return [sum(train[-28:]) / 28] * h
def walk_forward(model, start=80, horizon=7, step=7):
    errors = []
    for origin in range(start, n - horizon + 1, step):
        fc = model(y[:origin], horizon)
        errors += [abs(a - b) for a, b in zip(y[origin:origin + horizon], fc)]
    return sum(errors) / len(errors)
naive_errors = [abs(y[t] - y[t - 1]) for t in range(1, n)]
naive_mae = sum(naive_errors) / len(naive_errors)
for name, model in [("seasonal naive", seasonal_naive), ("trailing mean", mean_forecast)]:
    m = walk_forward(model)
    print(f"{name:>15}: walk-forward MAE {m:5.2f} | MASE vs one-step naive {m / naive_mae:4.2f}")
