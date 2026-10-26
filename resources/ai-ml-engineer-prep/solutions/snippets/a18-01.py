import random
random.seed(1)
def true_f(x): return 2 * x + 1
xs = [i / 10 for i in range(0, 11)]
train = [(x, true_f(x) + random.gauss(0, 0.3)) for x in xs]
test = [(x + 0.05, true_f(x + 0.05) + random.gauss(0, 0.3)) for x in xs[:-1]]
def fit_poly(points, degree):                                 # least squares by solving the normal equations
    n = degree + 1
    A = [[sum(x ** (i + j) for x, _ in points) for j in range(n)] for i in range(n)]
    b = [sum(y * x ** i for x, y in points) for i in range(n)]
    M = [A[i] + [b[i]] for i in range(n)]
    for i in range(n):
        p = max(range(i, n), key=lambda r: abs(M[r][i])); M[i], M[p] = M[p], M[i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]; M[r] = [a - f * c for a, c in zip(M[r], M[i])]
    coef = [0.0] * n
    for i in reversed(range(n)): coef[i] = (M[i][n] - sum(M[i][j] * coef[j] for j in range(i + 1, n))) / M[i][i]
    return coef
predict = lambda c, x: sum(ci * x ** i for i, ci in enumerate(c))
mse = lambda c, pts: sum((predict(c, x) - y) ** 2 for x, y in pts) / len(pts)
for degree in (0, 1, 3, 8):
    c = fit_poly(train, degree)
    print(f"degree {degree}: training error {mse(c, train):.3f} | error on new points {mse(c, test):.3f}")
