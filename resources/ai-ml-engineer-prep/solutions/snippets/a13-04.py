import random
random.seed(4)
TRUE_PHI = (0.6, -0.3)
y = [0.0, 0.0]
for _ in range(1500): y.append(TRUE_PHI[0] * y[-1] + TRUE_PHI[1] * y[-2] + random.gauss(0, 1))
def solve(A, b):                                               # Gaussian elimination for the normal equations
    n = len(b); M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i])); M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n + 1): M[r][c] -= f * M[i][c]
    x = [0.0] * n
    for i in reversed(range(n)): x[i] = (M[i][n] - sum(M[i][j] * x[j] for j in range(i + 1, n))) / M[i][i]
    return x
def fit_ar(series, p):
    X = [[1.0] + [series[t - k] for k in range(1, p + 1)] for t in range(p, len(series))]
    target = [series[t] for t in range(p, len(series))]
    XtX = [[sum(X[r][i] * X[r][j] for r in range(len(X))) for j in range(p + 1)] for i in range(p + 1)]
    Xty = [sum(X[r][i] * target[r] for r in range(len(X))) for i in range(p + 1)]
    return solve(XtX, Xty)
coef = fit_ar(y, 2)
print("true phi:", TRUE_PHI, "| estimated phi:", [round(c, 2) for c in coef[1:]], "| intercept:", round(coef[0], 2))
def forecast(series, coef, steps):
    out, hist = [], series[:]
    for _ in range(steps):
        nxt = coef[0] + sum(coef[k] * hist[-k] for k in range(1, len(coef))); out.append(nxt); hist.append(nxt)
    return out
print("multi-step forecasts decay toward the mean:", [round(v, 2) for v in forecast(y, coef, 6)])
