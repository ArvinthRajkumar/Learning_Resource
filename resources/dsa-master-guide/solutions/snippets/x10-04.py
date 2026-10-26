import random, itertools
random.seed(2)
def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def convex_hull(points):
    pts = sorted(set(points))
    if len(pts) <= 2: return pts
    lower, upper = [], []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0: lower.pop()
        lower.append(p)
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0: upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]                                           # counter-clockwise, no repeated endpoints
def hull_brute(points):                                                       # a point is a hull vertex if no triangle of the others contains it strictly or on an edge
    pts = list(set(points)); keep = []
    for p in pts:
        others = [q for q in pts if q != p]
        def in_tri(a, b, c):
            d1, d2, d3 = cross(a, b, p), cross(b, c, p), cross(c, a, p)
            has_neg = d1 < 0 or d2 < 0 or d3 < 0; has_pos = d1 > 0 or d2 > 0 or d3 > 0
            return not (has_neg and has_pos) and cross(a, b, c) != 0
        collinear_between = any(cross(a, b, p) == 0 and min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and min(a[1], b[1]) <= p[1] <= max(a[1], b[1]) for a, b in itertools.combinations(others, 2))
        if not any(in_tri(a, b, c) for a, b, c in itertools.combinations(others, 3)) and not collinear_between: keep.append(p)
    return sorted(keep)
for _ in range(300):
    pts = [(random.randint(0, 8), random.randint(0, 8)) for _ in range(random.randint(3, 9))]
    assert sorted(convex_hull(pts)) == hull_brute(pts) or len(set(pts)) < 3, pts
print("monotone chain hull matches the brute-force definition on 300 random point sets")
print("hull of a square with an interior point:", convex_hull([(0, 0), (4, 0), (4, 4), (0, 4), (2, 2)]))
