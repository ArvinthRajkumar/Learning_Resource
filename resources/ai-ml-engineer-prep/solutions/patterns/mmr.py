"""Maximal Marginal Relevance diversification."""
from typing import List


def mmr(query_sim: List[float], doc_sim: List[List[float]], k: int, lam: float = 0.7) -> List[int]:
    """Greedy selection: argmax_d [ lam * sim(q, d) - (1 - lam) * max_{s in S} sim(d, s) ].

    lam = 1 is plain relevance ranking, lam = 0 is pure diversity. The first
    pick is always the most relevant doc (S is empty, penalty 0). Ties:
    smaller index. Returns picks in selection order. O(k * n).
    """
    n = len(query_sim)
    selected: List[int] = []
    max_sim = [float("-inf")] * n  # max similarity to anything selected so far
    remaining = set(range(n))
    while remaining and len(selected) < k:
        def gain(d):
            penalty = max_sim[d] if selected else 0.0
            return (lam * query_sim[d] - (1 - lam) * penalty, -d)
        best = max(remaining, key=gain)
        selected.append(best)
        remaining.discard(best)
        for d in remaining:
            max_sim[d] = max(max_sim[d], doc_sim[d][best])
    return selected
