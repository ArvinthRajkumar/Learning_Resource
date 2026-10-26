"""Numerically stable softmax with temperature."""
import math
from typing import List


def softmax(logits: List[float], temperature: float = 1.0) -> List[float]:
    """p_i = exp((z_i - max z) / T) / sum_j exp((z_j - max z) / T).

    Subtracting the max changes nothing mathematically (it cancels in the
    ratio) but keeps every exponent <= 0, so exp never overflows. At least
    one term is exp(0) = 1, so the denominator is never 0.
    """
    if temperature <= 0:
        raise ValueError("temperature must be > 0 (use argmax for T = 0)")
    if not logits:
        return []
    m = max(logits)
    exps = [math.exp((z - m) / temperature) for z in logits]
    total = sum(exps)
    return [e / total for e in exps]
