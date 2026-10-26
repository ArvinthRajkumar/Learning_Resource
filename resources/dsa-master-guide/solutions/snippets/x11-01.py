from collections import deque
class HitCounter:
    def __init__(self, window=300): self.window, self.q = window, deque()
    def hit(self, t): self.q.append(t)
    def count(self, t):
        while self.q and self.q[0] <= t - self.window: self.q.popleft()          # expired
        return len(self.q)
class BucketHitCounter:                                                          # O(window) memory regardless of traffic
    def __init__(self, window=300): self.w, self.times, self.hits = window, [0] * window, [0] * window
    def hit(self, t):
        i = t % self.w
        if self.times[i] != t: self.times[i], self.hits[i] = t, 0                # slot reused by a newer second
        self.hits[i] += 1
    def count(self, t): return sum(h for tt, h in zip(self.times, self.hits) if t - self.w < tt <= t)
a, b = HitCounter(), BucketHitCounter()
seen = []
for t in [1, 1, 2, 3, 100, 300, 301, 302, 700]:                      # operations arrive in time order
    a.hit(t); b.hit(t); seen.append(t)
    expected = sum(1 for x in seen if t - 300 < x <= t)
    assert a.count(t) == b.count(t) == expected, t
print("both counters agree with a direct count after every hit; at t=302 the last 300 seconds hold", sum(1 for x in seen if 302 - 300 < x <= 302 and x <= 302), "hits")
