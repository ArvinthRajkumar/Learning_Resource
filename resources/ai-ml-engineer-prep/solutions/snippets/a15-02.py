import random, math
random.seed(1)
# two dense groups of 5 nodes joined by a single bridge edge
n = 10
A = [[0] * n for _ in range(n)]
def link(a, b): A[a][b] = A[b][a] = 1
for group in (range(0, 5), range(5, 10)):
    for i in group:
        for j in group:
            if i < j: link(i, j)
link(4, 5)
deg = [sum(r) for r in A]
L = [[(deg[i] if i == j else 0) - A[i][j] for j in range(n)] for i in range(n)]
# power iteration on (c I - L), deflating the constant eigenvector, to find the Fiedler vector
c = max(deg) * 2
v = [random.random() for _ in range(n)]
for _ in range(2000):
    mean = sum(v) / n; v = [x - mean for x in v]                         # remove the all-ones (eigenvalue 0) direction
    w = [c * v[i] - sum(L[i][j] * v[j] for j in range(n)) for i in range(n)]
    norm = math.sqrt(sum(x * x for x in w)); v = [x / norm for x in w]
print("Fiedler vector signs (nodes 0-4 vs 5-9):", ["+" if x > 0 else "-" for x in v])
print("spectral clustering recovers the two groups:", len({x > 0 for x in v[:5]}) == 1 and len({x > 0 for x in v[5:]}) == 1 and (v[0] > 0) != (v[9] > 0))
