import math
T = 1000
betas = [1e-4 + (0.02 - 1e-4) * i / (T - 1) for i in range(T)]
ab, p = [], 1.0
for b in betas:
    p *= 1 - b
    ab.append(p)
for t in (0, 250, 500, 750, 999):
    snr = ab[t] / (1 - ab[t])
    print("t=%3d  alpha_bar=%.5f  log SNR=%6.2f" % (t, ab[t], math.log(snr)))
