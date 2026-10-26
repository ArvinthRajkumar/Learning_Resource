from collections import defaultdict, deque
import math
class Trending:
    def __init__(self, window=5):
        self.window, self.buckets, self.total, self.baseline = window, deque(), defaultdict(int), defaultdict(lambda: 1.0)
    def push_minute(self, counts):
        self.buckets.append(counts)
        for tag, n in counts.items(): self.total[tag] += n
        if len(self.buckets) > self.window:
            old = self.buckets.popleft()
            for tag, n in old.items():
                self.total[tag] -= n
                if self.total[tag] == 0: del self.total[tag]
    def score(self, tag):                                              # surprise relative to the usual rate
        expected = self.baseline[tag] * self.window
        return (self.total[tag] - expected) / math.sqrt(expected + 1)
    def top(self, k=3): return sorted(((round(self.score(t), 1), t, self.total[t]) for t in self.total), reverse=True)[:k]
t = Trending(window=5)
t.baseline.update({"#monday": 100.0, "#coffee": 20.0})
for minute in range(6):
    t.push_minute({"#monday": 100, "#coffee": 20, "#goal": 5 * (minute > 2) * 40 + 1, "#rare": 2})
print("by score (score, tag, count in window):", t.top())
print("by raw count:", sorted(((n, tag) for tag, n in t.total.items()), reverse=True)[:3])
