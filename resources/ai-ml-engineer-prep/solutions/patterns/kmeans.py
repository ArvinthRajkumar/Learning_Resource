"""k-means (Lloyd's algorithm) with k-means++ initialization, pure Python."""
import random
from typing import List, Sequence, Tuple

Point = Sequence[float]


def _d2(a: Point, b: Point) -> float:
    return sum((x - y) ** 2 for x, y in zip(a, b))


def kmeans(points: List[Point], k: int, iters: int = 100, seed: int = 0) -> Tuple[List[List[float]], List[int]]:
    """Alternate two steps until assignments stop changing:
    1. assign each point to its nearest centroid (squared Euclidean),
    2. move each centroid to the mean of its points.
    Each step can only lower the within-cluster sum of squares, so it
    converges, but to a LOCAL optimum that depends on the initialization.
    k-means++ picks initial centroids far apart (probability proportional to
    squared distance), which makes bad local optima much less likely.
    """
    rng = random.Random(seed)
    centroids = [list(rng.choice(points))]
    while len(centroids) < k:
        d2 = [min(_d2(p, c) for c in centroids) for p in points]
        total = sum(d2)
        r, acc = rng.random() * total, 0.0
        for p, w in zip(points, d2):
            acc += w
            if acc >= r:
                centroids.append(list(p))
                break
    assign: List[int] = [-1] * len(points)
    for _ in range(iters):
        new = [min(range(k), key=lambda c: (_d2(p, centroids[c]), c)) for p in points]
        if new == assign:
            break
        assign = new
        for c in range(k):
            members = [p for p, a in zip(points, assign) if a == c]
            if members:                               # keep an empty cluster's centroid in place
                centroids[c] = [sum(col) / len(members) for col in zip(*members)]
    return centroids, assign


def inertia(points: List[Point], centroids: List[List[float]], assign: List[int]) -> float:
    """Within-cluster sum of squared distances, the objective k-means minimizes."""
    return sum(_d2(p, centroids[a]) for p, a in zip(points, assign))
