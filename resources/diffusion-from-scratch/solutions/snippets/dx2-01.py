import math, random
random.seed(0)

def schedule(T):
    betas = [1e-4 + (0.02 - 1e-4) * i / (T - 1) for i in range(T)]
    alphas = [1 - b for b in betas]
    ab, p = [], 1.0
    for a in alphas:
        p *= a
        ab.append(p)
    return betas, alphas, ab

MEANS, S_STD, W = [-2.0, 2.0], 0.3, [0.3, 0.7]      # target: 30 percent near -2, 70 percent near +2

def eps_star(x, ab):
    """Exact optimal noise prediction for the mixture data at noise level ab."""
    v = ab * S_STD ** 2 + 1 - ab
    resp, tot = [], 0.0
    for m, w in zip(MEANS, W):
        r = w * math.exp(-((x - math.sqrt(ab) * m) ** 2) / (2 * v))
        resp.append(r); tot += r
    score = sum((r / tot) * (-(x - math.sqrt(ab) * m) / v) for r, m in zip(resp, MEANS))
    return -math.sqrt(1 - ab) * score

def ddpm_sample(n, T=1000):
    betas, alphas, ab = schedule(T)
    out = []
    for _ in range(n):
        x = random.gauss(0, 1)
        for t in reversed(range(T)):
            mean = (x - betas[t] / math.sqrt(1 - ab[t]) * eps_star(x, ab[t])) / math.sqrt(alphas[t])
            x = mean + (math.sqrt(betas[t]) * random.gauss(0, 1) if t > 0 else 0.0)
        out.append(x)
    return out

xs = ddpm_sample(600)
right = sum(1 for x in xs if x > 0) / len(xs)
m1 = sum(x for x in xs if x > 0) / max(1, sum(1 for x in xs if x > 0))
print("fraction near +2: %.2f (target 0.70), mean of that mode: %.2f (target 2.00)" % (right, m1))
