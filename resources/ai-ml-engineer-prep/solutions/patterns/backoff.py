"""Retry with exponential backoff and full jitter."""
import random
import time
from typing import Callable, Tuple, Type


def backoff_delay(attempt: int, base: float = 0.5, cap: float = 30.0,
                  rng: random.Random = random) -> float:
    """Full jitter: uniform(0, min(cap, base * 2^attempt)), attempt = 0, 1, 2...

    Exponential growth gives a struggling server room. Jitter spreads
    clients out so they do not all retry at the same instant (the
    "thundering herd"). The cap keeps one delay from growing without bound.
    """
    return rng.uniform(0, min(cap, base * (2 ** attempt)))


def retry(fn: Callable[[], object], max_attempts: int = 5,
          retry_on: Tuple[Type[BaseException], ...] = (TimeoutError, ConnectionError),
          base: float = 0.5, cap: float = 30.0,
          sleep: Callable[[float], None] = time.sleep, rng: random.Random = random):
    """Call fn until it succeeds, retrying only on retry_on errors.

    Only safe for idempotent operations: if fn has side effects (a payment,
    a refund), pass the same idempotency key on every attempt so a retry
    after a timeout cannot apply the effect twice.
    """
    for attempt in range(max_attempts):
        try:
            return fn()
        except retry_on:
            if attempt == max_attempts - 1:
                raise
            sleep(backoff_delay(attempt, base, cap, rng))
