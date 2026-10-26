"""Mean Reciprocal Rank."""
from typing import Hashable, List, Set


def reciprocal_rank(ranked: List[Hashable], relevant: Set[Hashable], k: int = None) -> float:
    """1 / (1-based position of the FIRST relevant result), 0 if none in the top k."""
    for pos, d in enumerate(ranked[:k] if k else ranked, start=1):
        if d in relevant:
            return 1.0 / pos
    return 0.0


def mean_reciprocal_rank(runs: List[List[Hashable]], qrels: List[Set[Hashable]], k: int = None) -> float:
    """Average of reciprocal_rank over queries. Queries with no hit count as 0."""
    if not runs:
        return 0.0
    return sum(reciprocal_rank(r, q, k) for r, q in zip(runs, qrels)) / len(runs)
