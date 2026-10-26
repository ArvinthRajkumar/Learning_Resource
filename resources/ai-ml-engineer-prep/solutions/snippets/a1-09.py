import random
random.seed(4)
data = [((random.gauss(-1.5, 0.6), random.gauss(-1.5, 0.6)), -1) for _ in range(60)] + \
       [((random.gauss(1.5, 0.6), random.gauss(1.5, 0.6)), 1) for _ in range(60)]
w, b, lam, lr = [0.0, 0.0], 0.0, 0.01, 0.05
for epoch in range(100):
    for (x1, x2), y in data:
        margin = y * (w[0] * x1 + w[1] * x2 + b)
        if margin < 1:                                  # hinge loss active
            w[0] += lr * (y * x1 - lam * w[0]); w[1] += lr * (y * x2 - lam * w[1]); b += lr * y
        else:
            w[0] -= lr * lam * w[0]; w[1] -= lr * lam * w[1]
acc = sum(y * (w[0] * x1 + w[1] * x2 + b) > 0 for (x1, x2), y in data) / len(data)
print("linear SVM accuracy", acc)
