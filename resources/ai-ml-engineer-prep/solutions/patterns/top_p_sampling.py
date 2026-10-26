"""Top-p (nucleus) sampling."""
import random
from typing import List

from softmax import softmax


def top_p_probs(logits: List[float], p: float, temperature: float = 1.0) -> List[float]:
    """Keep the smallest set of most likely tokens whose total probability >= p.

    Sort by probability (ties: smaller index), add tokens until the running
    sum reaches p, always keep at least one, renormalize. Temperature is
    applied BEFORE the cutoff, which is what most inference servers do
    (check your library: the order of processors can differ).
    """
    if not 0 < p <= 1:
        raise ValueError("p must be in (0, 1]")
    probs = softmax(logits, temperature)
    order = sorted(range(len(probs)), key=lambda i: (-probs[i], i))
    keep, acc = [], 0.0
    for i in order:
        keep.append(i)
        acc += probs[i]
        if acc >= p - 1e-12:
            break
    total = sum(probs[i] for i in keep)
    out = [0.0] * len(probs)
    for i in keep:
        out[i] = probs[i] / total
    return out


def sample_top_p(logits: List[float], p: float, temperature: float = 1.0,
                 rng: random.Random = random) -> int:
    probs = top_p_probs(logits, p, temperature)
    r, acc = rng.random(), 0.0
    for i, q in enumerate(probs):
        acc += q
        if r < acc:
            return i
    return max(i for i, q in enumerate(probs) if q > 0)
