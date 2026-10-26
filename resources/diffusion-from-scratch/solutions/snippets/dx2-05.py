import math, random
random.seed(3)
m, s = 3.0, 0.5

def v(x, t):
    """E[x1 - x0 | x_t = x] for x0 ~ N(m, s^2), x1 ~ N(0, 1), x_t = (1 - t) x0 + t x1."""
    var_t = (1 - t) ** 2 * s * s + t * t
    return -m + (t - (1 - t) * s * s) / var_t * (x - (1 - t) * m)

def sample(steps):
    x = random.gauss(0, 1)           # start from noise at t = 1
    dt = 1.0 / steps
    for i in range(steps):
        t = 1 - i * dt
        x -= v(x, t) * dt            # integrate backwards in t with Euler
    return x

for steps in (2, 4, 8, 32):
    xs = [sample(steps) for _ in range(4000)]
    mean = sum(xs) / len(xs)
    std = math.sqrt(sum((x - mean) ** 2 for x in xs) / len(xs))
    print("%2d Euler steps: mean %.2f (target %.2f), std %.2f (target %.2f)" % (steps, mean, m, std, s))
