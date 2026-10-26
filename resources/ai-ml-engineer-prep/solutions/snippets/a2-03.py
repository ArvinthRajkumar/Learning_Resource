import math
A = [[2.0, 1.0], [1.0, 2.0]]       # eigenvalues 3 and 1, eigenvectors (1,1) and (1,-1)
v = [1.0, 0.0]
for _ in range(60):                 # power iteration converges to the dominant eigenvector
    w = [A[0][0] * v[0] + A[0][1] * v[1], A[1][0] * v[0] + A[1][1] * v[1]]
    n = math.hypot(*w); v = [w[0] / n, w[1] / n]
lam = v[0] * (A[0][0] * v[0] + A[0][1] * v[1]) + v[1] * (A[1][0] * v[0] + A[1][1] * v[1])
print("eigenvector", [round(x, 3) for x in v], "eigenvalue", round(lam, 3))
