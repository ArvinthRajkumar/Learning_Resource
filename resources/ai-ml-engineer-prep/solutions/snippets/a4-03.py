import random, math
random.seed(0)
sentences = ["cats like milk", "dogs like bones", "cats chase mice", "dogs chase cats", "kings rule lands", "queens rule lands"]
vocab = sorted({w for s in sentences for w in s.split()})
idx = {w: i for i, w in enumerate(vocab)}
dim = 8
W = [[random.uniform(-0.5, 0.5) for _ in range(dim)] for _ in vocab]      # centre vectors
C = [[random.uniform(-0.5, 0.5) for _ in range(dim)] for _ in vocab]      # context vectors
sig = lambda z: 1 / (1 + math.exp(-z))
pairs = []
for s in sentences:
    ws = s.split()
    for i, w in enumerate(ws):
        for j in range(max(0, i - 1), min(len(ws), i + 2)):
            if i != j:
                pairs.append((idx[w], idx[ws[j]]))
for epoch in range(400):
    for c, o in pairs:
        for target, label in ((o, 1), (random.randrange(len(vocab)), 0)):      # one positive, one random negative
            score = sum(W[c][k] * C[target][k] for k in range(dim))
            g = (sig(score) - label) * 0.1
            for k in range(dim):
                wk, ck = W[c][k], C[target][k]
                W[c][k] -= g * ck; C[target][k] -= g * wk
cos = lambda a, b: sum(x * y for x, y in zip(a, b)) / math.sqrt(sum(x * x for x in a) * sum(y * y for y in b))
for a, b in (("cats", "dogs"), ("kings", "queens"), ("cats", "kings")):
    print("%-6s %-7s similarity %.2f" % (a, b, cos(W[idx[a]], W[idx[b]])))
