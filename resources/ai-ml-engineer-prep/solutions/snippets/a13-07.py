import random, math, statistics
random.seed(7)
period, n = 24, 24 * 14
y = [50 + 20 * math.sin(2 * math.pi * (t % period) / period) + random.gauss(0, 2) for t in range(n)]
injected = {200: +40, 250: -35, 300: +30}                    # three spikes
for t, d in injected.items(): y[t] += d
naive_flags = [t for t in range(n) if abs(y[t] - statistics.mean(y)) > 3 * statistics.pstdev(y)]
def seasonal_flags(y, period, history_days=7, threshold=5):
    profile = [statistics.median(y[d * period + h] for d in range(history_days)) for h in range(period)]       # typical value for each hour of day
    resid = [y[t] - profile[t % period] for t in range(len(y))]
    med = statistics.median(resid); mad = statistics.median(abs(r - med) for r in resid)                        # robust spread of the residuals
    scale = 1.4826 * mad
    return [t for t, r in enumerate(resid) if abs(r - med) / scale > threshold]
flags = seasonal_flags(y, period)
print("injected anomalies:", sorted(injected))
print("global 3-sigma threshold flags:", naive_flags, "(misses anomalies hidden inside the daily swing)")
print("seasonal robust z-score flags :", flags)
