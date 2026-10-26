from collections import deque
class FixedWindow:                                          # cheap, but allows 2N at a window boundary
    def __init__(self, n, w): self.n, self.w, self.win, self.c = n, w, None, 0
    def allow(self, t):
        win = t // self.w
        if win != self.win: self.win, self.c = win, 0
        if self.c < self.n: self.c += 1; return True
        return False
class SlidingLog:                                           # exact, O(N) memory per user
    def __init__(self, n, w): self.n, self.w, self.log = n, w, deque()
    def allow(self, t):
        while self.log and self.log[0] <= t - self.w: self.log.popleft()
        if len(self.log) < self.n: self.log.append(t); return True
        return False
class TokenBucket:                                          # O(1) memory, permits bursts up to capacity
    def __init__(self, capacity, rate): self.cap, self.rate, self.tokens, self.last = capacity, rate, capacity, 0
    def allow(self, t):
        self.tokens = min(self.cap, self.tokens + (t - self.last) * self.rate); self.last = t
        if self.tokens >= 1: self.tokens -= 1; return True
        return False
ts = [0, 1, 2, 9, 10, 11, 12, 13]
fw, sl = FixedWindow(3, 10), SlidingLog(3, 10)
print("fixed window :", [fw.allow(t) for t in ts])
print("sliding log  :", [sl.allow(t) for t in ts])
tb = TokenBucket(capacity=3, rate=0.1)
print("token bucket :", [tb.allow(t) for t in [0, 0, 0, 0, 5, 10, 10, 20]])
fw2, sl2 = FixedWindow(3, 10), SlidingLog(3, 10)
burst = [8, 8, 8, 10, 10, 10]                               # 3 requests just before the boundary, 3 just after
print("burst at the boundary, fixed window lets", sum(fw2.allow(t) for t in burst), "through; sliding log lets", sum(sl2.allow(t) for t in burst))
