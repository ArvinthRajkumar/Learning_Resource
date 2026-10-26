import random
random.seed(0)
# observed (user, item, rating) triples from a small matrix with two tastes
data = [(0, 0, 5), (0, 1, 4), (0, 2, 1), (1, 0, 4), (1, 2, 1), (1, 3, 2), (2, 1, 1), (2, 2, 5), (2, 3, 4), (3, 0, 1), (3, 2, 4), (3, 3, 5)]
k, n_users, n_items = 2, 4, 4
P = [[random.gauss(0, 0.3) for _ in range(k)] for _ in range(n_users)]
Q = [[random.gauss(0, 0.3) for _ in range(k)] for _ in range(n_items)]
lr, reg = 0.02, 0.02
for epoch in range(3000):
    for u, i, r in data:
        pred = sum(P[u][f] * Q[i][f] for f in range(k))
        e = r - pred
        for f in range(k):
            pu, qi = P[u][f], Q[i][f]
            P[u][f] += lr * (e * qi - reg * pu)
            Q[i][f] += lr * (e * pu - reg * qi)
rmse = (sum((r - sum(P[u][f] * Q[i][f] for f in range(k))) ** 2 for u, i, r in data) / len(data)) ** 0.5
print("training RMSE %.3f" % rmse)
print("predicted rating user 1 for item 1 (unobserved): %.2f" % sum(P[1][f] * Q[1][f] for f in range(k)))
