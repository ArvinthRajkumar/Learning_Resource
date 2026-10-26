import random
random.seed(3)
n = 60; labels = [0] * 30 + [1] * 30                                   # two communities of 30 nodes
adj = [[] for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        p = 0.2 if labels[i] == labels[j] else 0.02                    # many edges inside a community, few between (homophily)
        if random.random() < p: adj[i].append(j); adj[j].append(i)
X = [[(0.4 if y else -0.4) + random.gauss(0, 1.0)] for y in labels]    # one feature per node: weak signal, heavy noise
def gcn_layer(H):                                                      # average over the node and its neighbours
    return [[sum(H[u][0] for u in adj[v] + [v]) / (len(adj[v]) + 1)] for v in range(n)]
def accuracy(H): return sum((H[v][0] > 0) == (labels[v] == 1) for v in range(n)) / n
H = X
print("raw noisy features, accuracy of the sign rule:", round(accuracy(H), 2))
for layer in range(1, 6):
    H = gcn_layer(H)
    spread = max(h[0] for h in H) - min(h[0] for h in H)
    print(f"after {layer} message-passing layer(s): accuracy {accuracy(H):.2f}, feature spread {spread:.2f}")
