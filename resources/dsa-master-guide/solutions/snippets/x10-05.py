import random, math
random.seed(3)
def closest_pair(points):
    pts = sorted(points)
    def rec(lo, hi):                                                          # points sorted by x in [lo, hi)
        if hi - lo <= 3:
            return min((math.dist(pts[i], pts[j]) for i in range(lo, hi) for j in range(i + 1, hi)), default=float("inf"))
        mid = (lo + hi) // 2; midx = pts[mid][0]
        d = min(rec(lo, mid), rec(mid, hi))
        strip = sorted((p for p in pts[lo:hi] if abs(p[0] - midx) < d), key=lambda p: p[1])
        for i in range(len(strip)):
            for j in range(i + 1, len(strip)):
                if strip[j][1] - strip[i][1] >= d: break                      # only a few neighbours are ever checked
                d = min(d, math.dist(strip[i], strip[j]))
        return d
    return rec(0, len(pts))
for _ in range(200):
    pts = list({(random.randint(0, 50), random.randint(0, 50)) for _ in range(random.randint(2, 25))})
    if len(pts) < 2: continue
    brute = min(math.dist(a, b) for i, a in enumerate(pts) for b in pts[i + 1:])
    assert abs(closest_pair(pts) - brute) < 1e-9
print("closest pair (divide and conquer) verified against all-pairs")
# sweep line: the maximum number of overlapping intervals (meeting rooms)
def max_overlap(intervals):
    events = sorted([(s, 1) for s, e in intervals] + [(e, -1) for s, e in intervals])    # ends sort before starts at equal times (-1 < 1)
    cur = best = 0
    for _, delta in events: cur += delta; best = max(best, cur)
    return best
for _ in range(300):
    iv = [(s, s + random.randint(1, 5)) for s in [random.randint(0, 12) for _ in range(random.randint(1, 8))]]
    brute = max(sum(s <= t < e for s, e in iv) for t in range(0, 20))
    assert max_overlap(iv) == brute
print("sweep line maximum overlap verified | [(1,4),(2,5),(7,9)] overlaps at most:", max_overlap([(1, 4), (2, 5), (7, 9)]))
