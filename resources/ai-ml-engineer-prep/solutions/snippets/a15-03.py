import random, math
random.seed(2)
# a "barbell": two cliques of 4 connected through a path
edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(6,7),(6,8),(6,9),(7,8),(7,9),(8,9)]
n = 10
adj = [[] for _ in range(n)]
for a, b in edges: adj[a].append(b); adj[b].append(a)
def walk(start, length):
    path = [start]
    for _ in range(length - 1): path.append(random.choice(adj[path[-1]]))
    return path
cooc = [[0.0] * n for _ in range(n)]
for _ in range(400):
    for s in range(n):
        w = walk(s, 12)
        for i, a in enumerate(w):
            for b in w[i + 1:i + 4]: cooc[a][b] += 1; cooc[b][a] += 1             # nodes within a window of 3 co-occur
total = sum(map(sum, cooc)); rowsum = [sum(r) for r in cooc]
ppmi = [[max(0.0, math.log(cooc[i][j] * total / (rowsum[i] * rowsum[j]))) if cooc[i][j] > 0 else 0.0 for j in range(n)] for i in range(n)]   # positive pointwise mutual information
def top_eigvecs(M, k, iters=300):
    vecs = []
    for _ in range(k):
        v = [random.random() for _ in range(n)]
        for _ in range(iters):
            for u in vecs:                                                         # orthogonalise against earlier vectors
                dot = sum(a * b for a, b in zip(v, u)); v = [a - dot * b for a, b in zip(v, u)]
            w = [sum(M[i][j] * v[j] for j in range(n)) for i in range(n)]
            norm = math.sqrt(sum(x * x for x in w)) or 1; v = [x / norm for x in w]
        vecs.append(v)
    return vecs
vecs = top_eigvecs(ppmi, 2)
emb = [(vecs[0][i], vecs[1][i]) for i in range(n)]
cos = lambda a, b: sum(x * y for x, y in zip(a, b)) / (math.hypot(*a) * math.hypot(*b) + 1e-12)
print("within the left clique, cosine(0,1):", round(cos(emb[0], emb[1]), 2), "| within the right clique, cosine(8,9):", round(cos(emb[8], emb[9]), 2))
print("across the cliques, cosine(0,9):", round(cos(emb[0], emb[9]), 2), "| nodes in the same clique are closer than nodes in different cliques:", cos(emb[0], emb[1]) > cos(emb[0], emb[9]) and cos(emb[8], emb[9]) > cos(emb[0], emb[9]))
