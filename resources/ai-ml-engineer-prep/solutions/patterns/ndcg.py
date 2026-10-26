"""nDCG@k."""
import math
from typing import Dict, Hashable, List


def dcg(gains: List[float]) -> float:
    """sum_i gain_i / log2(i + 1), positions i = 1, 2, 3, ..."""
    return sum(g / math.log2(i + 1) for i, g in enumerate(gains, start=1))


def ndcg_at_k(ranked: List[Hashable], relevance: Dict[Hashable, float], k: int,
              exponential: bool = False) -> float:
    """DCG of the top k divided by the DCG of the ideal top k.

    relevance holds graded judgments for ALL judged docs (unlisted = 0). The
    ideal ordering sorts every judged doc by relevance, not only the ones the
    system retrieved; otherwise a system that misses relevant docs gets
    flattered. exponential=True uses gain 2^rel - 1 (common in web search),
    the default uses gain = rel. Returns 0.0 when nothing is relevant.
    """
    gain = (lambda r: 2 ** r - 1) if exponential else (lambda r: r)
    got = [gain(relevance.get(d, 0)) for d in ranked[:k]]
    ideal = sorted((gain(r) for r in relevance.values()), reverse=True)[:k]
    idcg = dcg(ideal)
    return dcg(got) / idcg if idcg > 0 else 0.0
