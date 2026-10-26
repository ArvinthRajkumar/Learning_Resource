import math, random
random.seed(0)
T, s = 40, 2.0
betas = [0.005 + (0.2 - 0.005) * i / (T - 1) for i in range(T)]
alphas = [1 - b for b in betas]
ab, p = [], 1.0
for a in alphas:
    p *= a
    ab.append(p)

w = [0.0] * T                              # the "network": one weight per timestep
N = 200000
for step in range(N):
    lr = 0.01 * (1 - step / N) + 1e-4      # learning rate decays to nearly zero
    t = random.randrange(T)                # random timestep, as in training
    x0 = random.gauss(0, s)
    e = random.gauss(0, 1)
    xt = math.sqrt(ab[t]) * x0 + math.sqrt(1 - ab[t]) * e
    pred = w[t] * xt
    w[t] -= lr * 2 * (pred - e) * xt       # gradient of (pred - e)^2 with respect to w[t]

best = [math.sqrt(1 - ab[t]) / (ab[t] * s * s + 1 - ab[t]) for t in range(T)]
print("t    learned  optimal")
for t in (0, 10, 20, 30, 39):
    print("%2d   %.3f    %.3f" % (t, w[t], best[t]))

def sample(weights):
    x = random.gauss(0, 1)                 # start from pure noise
    for t in reversed(range(T)):
        eps = weights[t] * x
        x = (x - betas[t] / math.sqrt(1 - ab[t]) * eps) / math.sqrt(alphas[t])
        if t > 0:
            x += math.sqrt(betas[t]) * random.gauss(0, 1)
    return x

for name, weights in (("learned", w), ("optimal", best)):
    xs = [sample(weights) for _ in range(6000)]
    m = sum(xs) / len(xs)
    sd = math.sqrt(sum((x - m) ** 2 for x in xs) / len(xs))
    print("%s model: generated mean %.2f, std %.2f (data: mean 0.00, std %.2f)" % (name, m, sd, s))
