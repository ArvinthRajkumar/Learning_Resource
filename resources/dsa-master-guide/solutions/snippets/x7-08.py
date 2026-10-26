import heapq, random, statistics
random.seed(7)
class MedianFinder:
    def __init__(self): self.lo, self.hi = [], []
    def add(self, x):
        heapq.heappush(self.lo, -x)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo): heapq.heappush(self.lo, -heapq.heappop(self.hi))
    def median(self):
        return -self.lo[0] if len(self.lo) > len(self.hi) else (-self.lo[0] + self.hi[0]) / 2
m, seen = MedianFinder(), []
for _ in range(500):
    x = random.randint(-50, 50); m.add(x); seen.append(x)
    assert m.median() == statistics.median(seen)
print("running median verified over 500 inserts")
