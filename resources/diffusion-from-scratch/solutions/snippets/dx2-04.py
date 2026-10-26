# Guidance on the toy: condition on "mode +2"; the unconditional prediction is approximated by the prior-weighted mix.
import math
def gauss(x, m, v): return math.exp(-((x - m) ** 2) / (2 * v)) / math.sqrt(2 * math.pi * v)
ab = 0.5
v = ab * 0.3 ** 2 + 1 - ab
def eps_mode(x, m):                      # exact eps for a single Gaussian component
    return math.sqrt(1 - ab) * (x - math.sqrt(ab) * m) / v
x = 1.0
cond, uncond = eps_mode(x, 2.0), 0.3 * eps_mode(x, -2.0) + 0.7 * eps_mode(x, 2.0)
for w in (0.0, 1.0, 3.0, 7.0):
    print("w=%.1f guided eps=%.3f" % (w, uncond + w * (cond - uncond)))
