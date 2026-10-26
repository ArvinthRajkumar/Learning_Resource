"""Confusion-matrix metrics and ROC-AUC from scratch."""
from typing import Dict, List, Sequence


def confusion(y_true: Sequence[int], y_pred: Sequence[int]) -> Dict[str, int]:
    tp = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 1)
    fp = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 1)
    fn = sum(1 for t, p in zip(y_true, y_pred) if t == 1 and p == 0)
    tn = sum(1 for t, p in zip(y_true, y_pred) if t == 0 and p == 0)
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn}


def precision_recall_f1(y_true: Sequence[int], y_pred: Sequence[int], beta: float = 1.0):
    """precision = tp/(tp+fp), recall = tp/(tp+fn), F_beta = (1+b^2)PR/(b^2 P + R).
    Undefined ratios (0/0) are returned as 0.0, the common library convention."""
    c = confusion(y_true, y_pred)
    p = c["tp"] / (c["tp"] + c["fp"]) if c["tp"] + c["fp"] else 0.0
    r = c["tp"] / (c["tp"] + c["fn"]) if c["tp"] + c["fn"] else 0.0
    b2 = beta * beta
    f = (1 + b2) * p * r / (b2 * p + r) if (b2 * p + r) else 0.0
    return p, r, f


def roc_auc(y_true: Sequence[int], scores: Sequence[float]) -> float:
    """AUC = P(score of a random positive > score of a random negative), ties count 1/2.

    Computed with ranks (Mann-Whitney U) in O(n log n): sort by score, give
    tied scores their average rank, then
        AUC = (sum of positive ranks - n_pos (n_pos + 1) / 2) / (n_pos x n_neg)
    """
    n = len(scores)
    order = sorted(range(n), key=lambda i: scores[i])
    ranks: List[float] = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and scores[order[j + 1]] == scores[order[i]]:
            j += 1
        avg = (i + j) / 2 + 1                     # 1-based average rank of the tie group
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    n_pos = sum(1 for t in y_true if t == 1)
    n_neg = n - n_pos
    if n_pos == 0 or n_neg == 0:
        raise ValueError("AUC needs both classes")
    s = sum(r for r, t in zip(ranks, y_true) if t == 1)
    return (s - n_pos * (n_pos + 1) / 2) / (n_pos * n_neg)
