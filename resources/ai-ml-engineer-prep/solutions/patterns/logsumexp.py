"""Log-sum-exp and log-softmax, computed stably."""
import math
from typing import List


def logsumexp(xs: List[float]) -> float:
    """log(sum(exp(x))) = m + log(sum(exp(x - m))) with m = max(xs).

    Empty input or all -inf returns -inf (the log of an empty sum).
    """
    if not xs:
        return -math.inf
    m = max(xs)
    if m == -math.inf:
        return -math.inf
    return m + math.log(sum(math.exp(x - m) for x in xs))


def log_softmax(logits: List[float]) -> List[float]:
    """log p_i = z_i - logsumexp(z). Use this instead of log(softmax(z)),
    which returns -inf when a probability underflows to 0."""
    lse = logsumexp(logits)
    return [z - lse for z in logits]
