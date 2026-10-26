import random
random.seed(4)
latency = [random.lognormvariate(3.0, 0.8) for _ in range(300)]       # skewed data
def p95(x): return sorted(x)[int(0.95 * len(x))]
boots = sorted(p95([random.choice(latency) for _ in latency]) for _ in range(2000))
print("p95 latency %.1f ms, 95%% bootstrap interval (%.1f, %.1f)" % (p95(latency), boots[50], boots[1949]))
