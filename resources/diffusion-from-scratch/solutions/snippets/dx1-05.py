import math, random
random.seed(1)
ab = 0.3                                   # any value in (0, 1)
x0, eps = random.gauss(0, 1), random.gauss(0, 1)
xt = math.sqrt(ab) * x0 + math.sqrt(1 - ab) * eps
v = math.sqrt(ab) * eps - math.sqrt(1 - ab) * x0

x0_from_eps = (xt - math.sqrt(1 - ab) * eps) / math.sqrt(ab)
x0_from_v = math.sqrt(ab) * xt - math.sqrt(1 - ab) * v
eps_from_v = math.sqrt(1 - ab) * xt + math.sqrt(ab) * v
print(round(x0 - x0_from_eps, 12), round(x0 - x0_from_v, 12), round(eps - eps_from_v, 12))
