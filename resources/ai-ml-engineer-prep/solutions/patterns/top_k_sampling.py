"""Top-k sampling."""
import random
from typing import List

from softmax import softmax


def top_k_probs(logits: List[float], k: int, temperature: float = 1.0) -> List[float]:
    """Keep the k largest logits (ties: smaller index), renormalize, zero the rest."""
    if k <= 0:
        raise ValueError("k must be >= 1")
    keep = sorted(range(len(logits)), key=lambda i: (-logits[i], i))[:k]
    sub = softmax([logits[i] for i in keep], temperature)
    probs = [0.0] * len(logits)
    for i, p in zip(keep, sub):
        probs[i] = p
    return probs


def sample_top_k(logits: List[float], k: int, temperature: float = 1.0,
                 rng: random.Random = random) -> int:
    """Draw one token id. temperature == 0 means greedy (argmax)."""
    if temperature == 0:
        return max(range(len(logits)), key=lambda i: (logits[i], -i))
    probs = top_k_probs(logits, k, temperature)
    r, acc = rng.random(), 0.0
    for i, p in enumerate(probs):
        acc += p
        if r < acc:
            return i
    return max(i for i, p in enumerate(probs) if p > 0)   # guard against rounding at acc ~ 1
