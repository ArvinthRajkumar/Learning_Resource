"""Cosine similarity top-k with numpy."""
import numpy as np


def cosine_top_k(matrix: np.ndarray, query: np.ndarray, k: int):
    """Return (indices, scores) of the k rows most cosine-similar to query.

    cos(a, b) = a.b / (|a| |b|). Normalize once, then one matrix-vector
    product scores every row. Zero vectors get similarity 0 instead of NaN.
    argpartition finds the top k in O(n), then only those k are sorted.
    Ties: smaller index first (lexsort on (index, -score)).
    """
    m = np.asarray(matrix, dtype=np.float64)
    q = np.asarray(query, dtype=np.float64)
    n = m.shape[0]
    if n == 0 or k <= 0:
        return np.array([], dtype=int), np.array([])
    k = min(k, n)
    row_norm = np.linalg.norm(m, axis=1)
    q_norm = np.linalg.norm(q)
    denom = row_norm * q_norm
    scores = np.divide(m @ q, denom, out=np.zeros(n), where=denom > 0)
    if k < n:
        # widen the partition to every row tied with the k-th score so the index tie-break is exact
        kth = np.partition(scores, n - k)[n - k]
        cand = np.nonzero(scores >= kth)[0]
    else:
        cand = np.arange(n)
    order = cand[np.lexsort((cand, -scores[cand]))][:k]
    return order, scores[order]
