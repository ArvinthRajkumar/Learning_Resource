class TokenBucket:
    def __init__(self, rate, capacity, now=0.0):
        self.rate, self.cap, self.tokens, self.last = rate, capacity, capacity, now
    def allow(self, now, cost=1):
        self.tokens = min(self.cap, self.tokens + (now - self.last) * self.rate)
        self.last = now
        if self.tokens >= cost:
            self.tokens -= cost
            return True
        return False

tb = TokenBucket(rate=2, capacity=4)          # 2 tokens per second, burst of 4
results = [tb.allow(t) for t in (0, 0, 0, 0, 0, 0.5, 1.0, 1.0, 1.0)]
print(results)
