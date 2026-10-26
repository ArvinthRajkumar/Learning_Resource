import random, math
random.seed(4)
n = 40; labels = [0] * 20 + [1] * 20
adj = [[] for _ in range(n)]
def connect(a, b):
    if a != b and b not in adj[a]: adj[a].append(b); adj[b].append(a)
for i in range(n):
    for j in range(i + 1, n):
        p = 0.35 if labels[i] == labels[j] else 0.03                     # homophilous random graph (stochastic block model)
        if random.random() < p: connect(i, j)
X = [[random.gauss(0.2 if y else -0.2, 1.0), random.gauss(0, 1)] for y in labels]      # weak, noisy features
def aggregate(H): return [[sum(H[u][k] for u in adj[v] + [v]) / (len(adj[v]) + 1) for k in range(2)] for v in range(n)]
def train(features, epochs=300, lr=0.5):
    w, b = [0.0, 0.0], 0.0
    idx = list(range(n)); train_idx = idx[:10] + idx[20:30]; test_idx = idx[10:20] + idx[30:]
    for _ in range(epochs):
        gw, gb = [0.0, 0.0], 0.0
        for v in train_idx:
            z = sum(wi * xi for wi, xi in zip(w, features[v])) + b; p = 1 / (1 + math.exp(-z)); err = p - labels[v]
            gw = [g + err * xi for g, xi in zip(gw, features[v])]; gb += err
        w = [wi - lr * g / len(train_idx) for wi, g in zip(w, gw)]; b -= lr * gb / len(train_idx)
    acc = sum(((sum(wi * xi for wi, xi in zip(w, features[v])) + b) > 0) == (labels[v] == 1) for v in test_idx) / len(test_idx)
    return acc
mlp_acc = train(X)                                   # ignores the graph
gcn_acc = train(aggregate(aggregate(X)))             # two rounds of message passing, then the same classifier
print(f"test accuracy on unseen nodes: features only {mlp_acc:.2f} | after 2 message-passing steps {gcn_acc:.2f}")
