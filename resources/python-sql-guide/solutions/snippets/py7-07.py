import random
random.seed(1)
class Flaky:
    """Fails twice with a 503, then succeeds."""
    def __init__(self): self.calls = 0
    def get(self):
        self.calls += 1
        if self.calls <= 2: return 503, None
        return 200, {"ok": True}
def with_retries(fn, attempts=5, base=0.1):
    delays = []
    for i in range(attempts):
        status, body = fn()
        if status < 500 and status != 429: return status, body, delays
        delay = random.uniform(0, base * 2 ** i)               # full jitter
        delays.append(round(delay, 3))                          # a real client would time.sleep(delay)
    return status, None, delays
f = Flaky()
status, body, delays = with_retries(f.get)
print("final:", status, body, "| attempts:", f.calls, "| back-off delays (s):", delays)
