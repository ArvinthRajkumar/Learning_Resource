import math, random
random.seed(3)
def rbf(a, b, length=1.0, var=1.0): return var * math.exp(-0.5 * ((a - b) / length) ** 2)
def solve(A, B):                                              # solve A X = B by Gauss-Jordan (A is small and positive definite)
    n = len(A); M = [A[i][:] + B[i][:] for i in range(n)]; m = len(B[0])
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i])); M[i], M[p] = M[p], M[i]
        piv = M[i][i]; M[i] = [v / piv for v in M[i]]
        for r in range(n):
            if r != i:
                f = M[r][i]; M[r] = [a - f * b for a, b in zip(M[r], M[i])]
    return [row[n:] for row in M]
X = [-4.0, -3.0, -1.0, 0.0, 2.0]
y = [math.sin(x) + random.gauss(0, 0.05) for x in X]
noise = 0.05 ** 2
K = [[rbf(a, b) + (noise if i == j else 0) for j, b in enumerate(X)] for i, a in enumerate(X)]
tests = [-4.0, -2.0, 0.0, 1.0, 3.0, 6.0]
Ks = [[rbf(t, x) for x in X] for t in tests]
alpha = solve(K, [[v] for v in y])
for t, ks in zip(tests, Ks):
    mean = sum(k * a[0] for k, a in zip(ks, alpha))
    v = solve(K, [[k] for k in ks]); var = rbf(t, t) - sum(k * vv[0] for k, vv in zip(ks, v))
    print(f"x = {t:>4}: prediction {mean:+.2f} +/- {2 * math.sqrt(max(var, 0)):.2f} (true sin(x) = {math.sin(t):+.2f})")
