import math, random
random.seed(1)
comps = [(-2.0, 0.3, 0.5), (2.5, 0.4, 0.5)]            # (mean, std, weight): a bimodal target
def velocity(x, t, comps=comps):
    weights, vels = [], []
    for m, s, w in comps:
        var = (1 - t) ** 2 + t * t * s * s
        weights.append(w * math.exp(-0.5 * (x - t * m) ** 2 / var) / math.sqrt(var))              # posterior weight of this component
        ex1 = m + t * s * s / var * (x - t * m); ex0 = (1 - t) * (x - t * m) / var
        vels.append(ex1 - ex0)
    z = sum(weights); return sum(w * v for w, v in zip(weights, vels)) / z
def sample(steps, n=4000, comps=comps):
    out = []
    for _ in range(n):
        x = random.gauss(0, 1)
        for i in range(steps): x += velocity(x, i / steps, comps) / steps                           # Euler integration of dx/dt = v
        out.append(x)
    return out
def target(n=4000, comps=comps):
    return [random.gauss(m, s) for m, s, _ in (random.choice(comps) for _ in range(n))]
def wasserstein1(a, b): a, b = sorted(a), sorted(b); return sum(abs(x - y) for x, y in zip(a, b)) / len(a)       # 1-D optimal transport distance
reference = target()
print("W1 distance between generated samples and the target (smaller is better):")
for steps in (1, 2, 4, 8, 32):
    print(f"  {steps:>2} Euler steps: {wasserstein1(sample(steps), reference):.3f}")
