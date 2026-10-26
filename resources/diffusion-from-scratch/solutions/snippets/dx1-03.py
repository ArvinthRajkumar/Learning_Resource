import math
T = 1000
betas = [1e-4 + (0.02 - 1e-4) * i / (T - 1) for i in range(T)]
alphas = [1 - b for b in betas]
ab, p = [], 1.0
for a in alphas:
    p *= a
    ab.append(p)
# weight of the true ELBO term with sigma_t^2 = beta_t, relative to the simple loss (weight 1)
for t in (1, 10, 100, 500, 999):
    w = betas[t] ** 2 / (2 * betas[t] * alphas[t] * (1 - ab[t]))
    print("t=%3d  ELBO weight %.4f" % (t, w))
