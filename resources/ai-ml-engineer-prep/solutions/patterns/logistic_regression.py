"""Logistic regression trained with batch gradient descent, pure Python."""
import math
from typing import List, Sequence, Tuple


def sigmoid(z: float) -> float:
    # stable for large |z|: never calls exp on a big positive number
    if z >= 0:
        return 1.0 / (1.0 + math.exp(-z))
    e = math.exp(z)
    return e / (1.0 + e)


def log_loss(X: Sequence[Sequence[float]], y: Sequence[int], w: List[float], b: float, l2: float = 0.0) -> float:
    eps = 1e-12
    total = 0.0
    for xi, yi in zip(X, y):
        p = sigmoid(sum(a * c for a, c in zip(w, xi)) + b)
        total += -(yi * math.log(p + eps) + (1 - yi) * math.log(1 - p + eps))
    return total / len(y) + 0.5 * l2 * sum(c * c for c in w)


def fit(X: Sequence[Sequence[float]], y: Sequence[int], lr: float = 0.1, epochs: int = 500,
        l2: float = 0.0) -> Tuple[List[float], float]:
    """Minimize mean binary cross-entropy (+ optional L2 on w, not on b).

    The gradient is remarkably simple: dL/dw = mean((p - y) x) + l2 w and
    dL/db = mean(p - y). Same form as linear regression's, with p = sigmoid(w.x + b).
    """
    n, d = len(X), len(X[0])
    w, b = [0.0] * d, 0.0
    for _ in range(epochs):
        gw, gb = [0.0] * d, 0.0
        for xi, yi in zip(X, y):
            err = sigmoid(sum(a * c for a, c in zip(w, xi)) + b) - yi
            for j in range(d):
                gw[j] += err * xi[j]
            gb += err
        w = [w[j] - lr * (gw[j] / n + l2 * w[j]) for j in range(d)]
        b -= lr * gb / n
    return w, b


def predict_proba(X: Sequence[Sequence[float]], w: List[float], b: float) -> List[float]:
    return [sigmoid(sum(a * c for a, c in zip(w, xi)) + b) for xi in X]
