import math
def softmax(xs):
    m = max(xs); e = [math.exp(x - m) for x in xs]; s = sum(e)
    return [x / s for x in e]
def attention(Q, K, V, causal=False):
    d = len(K[0])
    out = []
    for i, q in enumerate(Q):
        scores = [sum(a * b for a, b in zip(q, k)) / math.sqrt(d) for k in K]
        if causal:
            scores = [s if j <= i else float("-inf") for j, s in enumerate(scores)]
        w = softmax(scores)
        out.append([sum(w[j] * V[j][c] for j in range(len(V))) for c in range(len(V[0]))])
    return out
X = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]]
print("full  :", [[round(v, 2) for v in row] for row in attention(X, X, X)])
print("causal:", [[round(v, 2) for v in row] for row in attention(X, X, X, causal=True)])
