import math
def beta_pdf_grid(a, b, n=2001):
    xs = [i / (n - 1) for i in range(n)]
    ys = [(x ** (a - 1) * (1 - x) ** (b - 1)) if 0 < x < 1 else 0.0 for x in xs]
    total = sum(ys); return xs, [y / total for y in ys]
def credible_interval(a, b, mass=0.95):
    xs, ps = beta_pdf_grid(a, b)
    cum, lo, hi = 0.0, None, None
    for x, p in zip(xs, ps):
        cum += p
        if lo is None and cum >= (1 - mass) / 2: lo = x
        if hi is None and cum >= 1 - (1 - mass) / 2: hi = x
    return lo, hi
lo, hi = credible_interval(8, 4)
print(f"posterior Beta(8,4): 95% credible interval ({lo:.2f}, {hi:.2f}) | P(theta > 0.5) = {sum(p for x, p in zip(*beta_pdf_grid(8, 4)) if x > 0.5):.2f}")
