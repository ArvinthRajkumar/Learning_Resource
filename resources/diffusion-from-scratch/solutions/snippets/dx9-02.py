import math, random
random.seed(2)
single = [(2.0, 0.5, 1.0)]
def velocity(x, t, comps):
    m, s, w = comps[0]; var = (1 - t) ** 2 + t * t * s * s
    return (m + t * s * s / var * (x - t * m)) - (1 - t) * (x - t * m) / var
def run(steps, comps, n=4000):
    out = []
    for _ in range(n):
        x = random.gauss(0, 1)
        for i in range(steps): x += velocity(x, i / steps, comps) / steps
        out.append(x)
    return out
ref = sorted(random.gauss(2.0, 0.5) for _ in range(4000))
for steps in (1, 2, 8):
    out = sorted(run(steps, single)); w1 = sum(abs(a - b) for a, b in zip(out, ref)) / len(ref)
    print(f"single Gaussian target, {steps} Euler step(s): W1 distance {w1:.3f}, sample mean {sum(out) / len(out):.2f}, sample std {(sum((x - sum(out) / len(out)) ** 2 for x in out) / len(out)) ** 0.5:.2f}")
