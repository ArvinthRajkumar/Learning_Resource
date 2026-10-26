import math, random
random.seed(2)
# two clusters
data = [((random.gauss(-1, 0.8), random.gauss(-1, 0.8)), 0) for _ in range(100)] + \
       [((random.gauss(1, 0.8), random.gauss(1, 0.8)), 1) for _ in range(100)]
random.shuffle(data)
w, b, lr = [0.0, 0.0], 0.0, 0.1
sig = lambda z: 1 / (1 + math.exp(-z))
for epoch in range(200):
    for (x1, x2), y in data:
        p = sig(w[0] * x1 + w[1] * x2 + b)
        g = p - y
        w[0] -= lr * g * x1; w[1] -= lr * g * x2; b -= lr * g
acc = sum((sig(w[0] * x1 + w[1] * x2 + b) > 0.5) == bool(y) for (x1, x2), y in data) / len(data)
print("weights", [round(v, 2) for v in w], "bias", round(b, 2), "accuracy", acc)
