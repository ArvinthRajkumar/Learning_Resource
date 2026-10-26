import math, random
random.seed(1)
T = 1000
betas = [1e-4 + (0.02 - 1e-4) * i / (T - 1) for i in range(T)]
ab, p = [], 1.0
for b in betas:
    p *= 1 - b
    ab.append(p)
MEANS, S_STD, W = [-2.0, 2.0], 0.3, [0.3, 0.7]

def eps_star(x, a):
    v = a * S_STD ** 2 + 1 - a
    r = [w * math.exp(-((x - math.sqrt(a) * m) ** 2) / (2 * v)) for m, w in zip(MEANS, W)]
    tot = sum(r)
    score = sum((ri / tot) * (-(x - math.sqrt(a) * m) / v) for ri, m in zip(r, MEANS))
    return -math.sqrt(1 - a) * score

def ddim(x, steps):
    ts = [round(i * (T - 1) / (steps - 1)) for i in range(steps)][::-1]
    for i, t in enumerate(ts):
        a_now = ab[t]
        a_next = ab[ts[i + 1]] if i + 1 < len(ts) else 1.0
        e = eps_star(x, a_now)
        x0 = (x - math.sqrt(1 - a_now) * e) / math.sqrt(a_now)
        x = math.sqrt(a_next) * x0 + math.sqrt(1 - a_next) * e
    return x

noise = [random.gauss(0, 1) for _ in range(1500)]
for steps in (5, 10, 20, 50):
    xs = [ddim(z, steps) for z in noise]
    pos = [x for x in xs if x > 0]
    print("%2d steps: fraction near +2 = %.2f, mode mean %.2f, mode std %.2f" % (
        steps, len(pos) / len(xs), sum(pos) / len(pos), math.sqrt(sum((x - sum(pos) / len(pos)) ** 2 for x in pos) / len(pos))))
print("target:    fraction 0.70, mode mean 2.00, mode std 0.30")
print("deterministic:", ddim(0.5, 20) == ddim(0.5, 20))
