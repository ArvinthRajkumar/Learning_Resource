import random, math
random.seed(6)
pts = []
for _ in range(500):
    t = random.gauss(0, 3)
    pts.append((t + random.gauss(0, 0.5), 0.5 * t + random.gauss(0, 0.5)))   # data stretched along a diagonal
mx = sum(x for x, _ in pts) / len(pts); my = sum(y for _, y in pts) / len(pts)
c = [[sum((p[i] - (mx, my)[i]) * (p[j] - (mx, my)[j]) for p in pts) / len(pts) for j in range(2)] for i in range(2)]
# power iteration finds the top eigenvector of the 2x2 covariance matrix
v = [1.0, 0.0]
for _ in range(100):
    v = [c[0][0] * v[0] + c[0][1] * v[1], c[1][0] * v[0] + c[1][1] * v[1]]
    n = math.hypot(*v); v = [v[0] / n, v[1] / n]
eig = v[0] * (c[0][0] * v[0] + c[0][1] * v[1]) + v[1] * (c[1][0] * v[0] + c[1][1] * v[1])
total = c[0][0] + c[1][1]
print("first component direction", [round(v[0], 2), round(v[1], 2)], "explains %.0f%% of variance" % (100 * eig / total))
