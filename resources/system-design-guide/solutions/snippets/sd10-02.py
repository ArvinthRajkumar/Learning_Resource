class CircuitBreaker:
    def __init__(self, threshold=3, reset_after=10):
        self.threshold, self.reset_after = threshold, reset_after
        self.failures, self.state, self.opened_at = 0, "closed", 0
    def call(self, fn, now):
        if self.state == "open":
            if now - self.opened_at >= self.reset_after:
                self.state = "half-open"
            else:
                return "rejected (fail fast)"
        try:
            r = fn()
        except Exception:
            self.failures += 1
            if self.state == "half-open" or self.failures >= self.threshold:
                self.state, self.opened_at = "open", now
            return "error"
        self.failures, self.state = 0, "closed"
        return r

def bad(): raise RuntimeError("down")
def good(): return "ok"

cb = CircuitBreaker()
out = [cb.call(bad, t) for t in range(4)]          # trips open after 3 failures
out += [cb.call(good, 5)]                          # still open, rejected
out += [cb.call(good, 14)]                         # half-open probe succeeds
print(out, cb.state)
