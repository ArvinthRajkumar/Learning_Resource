"""Scaled dot-product attention (single head) with an optional causal mask, pure Python."""
import math
from typing import List

Matrix = List[List[float]]


def attention(Q: Matrix, K: Matrix, V: Matrix, causal: bool = False) -> Matrix:
    """out = softmax(Q K^T / sqrt(d_k) + mask) V

    Q: n_q x d_k, K: n_k x d_k, V: n_k x d_v. With causal=True, query i may
    only attend to keys 0..i (requires n_q == n_k), which is how a decoder
    stops token i from seeing the future. Each softmax row is max-shifted for
    stability. Cost: O(n_q x n_k x d), the quadratic term in sequence length.
    """
    d_k = len(K[0])
    scale = 1.0 / math.sqrt(d_k)
    out = []
    for i, q in enumerate(Q):
        scores = []
        for j, k in enumerate(K):
            if causal and j > i:
                scores.append(-math.inf)           # masked: weight becomes exactly 0
            else:
                scores.append(sum(a * b for a, b in zip(q, k)) * scale)
        m = max(scores)
        exps = [math.exp(s - m) if s != -math.inf else 0.0 for s in scores]
        total = sum(exps)
        weights = [e / total for e in exps]
        out.append([sum(w * v[c] for w, v in zip(weights, V)) for c in range(len(V[0]))])
    return out
