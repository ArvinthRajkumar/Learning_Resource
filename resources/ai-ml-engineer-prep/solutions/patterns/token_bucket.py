"""Token bucket rate limiter."""
import time
from typing import Callable, Optional


class TokenBucket:
    """Holds up to `capacity` tokens and refills at `rate` tokens per second.

    allow(cost) spends `cost` tokens if available. Bursts up to capacity
    are allowed; the long-run average is limited to `rate`. Refill is
    computed lazily from elapsed time, so there is no background thread.
    For LLM APIs, cost can be the request's token count (tokens-per-minute
    limits) instead of 1 (requests-per-minute limits).
    """

    def __init__(self, rate: float, capacity: float, clock: Callable[[], float] = time.monotonic):
        self.rate, self.capacity, self.clock = rate, capacity, clock
        self.tokens = capacity
        self.last = clock()

    def _refill(self, now: float) -> None:
        if now > self.last:
            self.tokens = min(self.capacity, self.tokens + (now - self.last) * self.rate)
            self.last = now

    def allow(self, cost: float = 1.0, now: Optional[float] = None) -> bool:
        self._refill(self.clock() if now is None else now)
        if cost <= self.tokens:
            self.tokens -= cost
            return True
        return False

    def wait_time(self, cost: float = 1.0, now: Optional[float] = None) -> float:
        """Seconds until `cost` tokens will be available (0 if available now)."""
        self._refill(self.clock() if now is None else now)
        if cost > self.capacity:
            return float("inf")
        return max(0.0, (cost - self.tokens) / self.rate)
