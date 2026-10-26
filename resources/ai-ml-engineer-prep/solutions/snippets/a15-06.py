import random, math
random.seed(5)
n = 60; group = [i // 20 for i in range(n)]
edges = set()
for i in range(n):
    for j in range(i + 1, n):
        if random.random() < (0.25 if group[i] == group[j] else 0.02): edges.add((i, j))
held = random.sample(sorted(edges), len(edges) // 5)
train = edges - set(held)
adj = [set() for _ in range(n)]
for a, b in train: adj[a].add(b); adj[b].add(a)
def common(a, b): return len(adj[a] & adj[b])
def adamic_adar(a, b): return sum(1 / math.log(len(adj[z]) + 1) for z in adj[a] & adj[b])
non_edges = random.sample([(i, j) for i in range(n) for j in range(i + 1, n) if (i, j) not in edges], len(held))
def auc(score):
    pos, neg = [score(a, b) for a, b in held], [score(a, b) for a, b in non_edges]
    return sum((p > q) + 0.5 * (p == q) for p in pos for q in neg) / (len(pos) * len(neg))
print(f"held-out edges: {len(held)} | AUC common neighbours {auc(common):.2f} | AUC Adamic-Adar {auc(adamic_adar):.2f} | random guessing 0.50")
