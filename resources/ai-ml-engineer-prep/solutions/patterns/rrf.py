"""Reciprocal Rank Fusion."""
from typing import Dict, Hashable, List, Tuple


def rrf(rankings: List[List[Hashable]], k: int = 60, top_n: int = None) -> List[Tuple[Hashable, float]]:
    """score(d) = sum over lists containing d of 1 / (k + rank(d)), rank 1-based.

    Only ranks are used, never raw scores, so BM25 scores (unbounded) and
    cosine scores (-1..1) can be fused without calibration. k = 60 is the
    value from the original paper (Cormack et al., 2009); larger k flattens
    the advantage of the top positions. A doc missing from a list simply
    gets nothing from that list. If an id repeats inside one list, only its
    first (best) position counts. Ties: id order, so ids must be comparable.
    """
    scores: Dict[Hashable, float] = {}
    for lst in rankings:
        seen = set()
        for rank, doc in enumerate(lst, start=1):
            if doc in seen:
                continue
            seen.add(doc)
            scores[doc] = scores.get(doc, 0.0) + 1.0 / (k + rank)
    out = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
    return out[:top_n] if top_n is not None else out
