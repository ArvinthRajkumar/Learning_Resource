import random
random.seed(1)
def sign(x): return (x > 0) - (x < 0)
def on_segment(a, b, p): return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1])
def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def segments_intersect(a, b, c, d):
    d1, d2, d3, d4 = sign(cross(a, b, c)), sign(cross(a, b, d)), sign(cross(c, d, a)), sign(cross(c, d, b))
    if d1 * d2 < 0 and d3 * d4 < 0: return True                           # proper crossing
    if d1 == 0 and on_segment(a, b, c): return True                       # touching or collinear overlap cases
    if d2 == 0 and on_segment(a, b, d): return True
    if d3 == 0 and on_segment(c, d, a): return True
    if d4 == 0 and on_segment(c, d, b): return True
    return False
def brute_intersect(a, b, c, d):                                          # exact rational check by sampling lattice points is not possible; use parametric form with Fractions
    from fractions import Fraction as F
    r = (b[0] - a[0], b[1] - a[1]); s = (d[0] - c[0], d[1] - c[1]); den = r[0] * s[1] - r[1] * s[0]
    qp = (c[0] - a[0], c[1] - a[1])
    if den == 0:
        if qp[0] * r[1] - qp[1] * r[0] != 0: return False                  # parallel, not collinear
        rr = r[0] * r[0] + r[1] * r[1]
        if rr == 0: return on_segment(c, d, a)                             # degenerate segment ab is a point
        t0 = F(qp[0] * r[0] + qp[1] * r[1], rr); t1 = t0 + F(s[0] * r[0] + s[1] * r[1], rr)
        lo, hi = sorted((t0, t1)); return hi >= 0 and lo <= 1
    t = F(qp[0] * s[1] - qp[1] * s[0], den); u = F(qp[0] * r[1] - qp[1] * r[0], den)
    return 0 <= t <= 1 and 0 <= u <= 1
for _ in range(3000):
    pts = [(random.randint(0, 6), random.randint(0, 6)) for _ in range(4)]
    a, b, c, d = pts
    if a == b or c == d: continue
    assert segments_intersect(a, b, c, d) == brute_intersect(a, b, c, d), pts
print("segment intersection (orientation tests) agrees with an exact parametric check on 3000 random small cases, including collinear and touching ones")
