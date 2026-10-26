import random
random.seed(1)
def make(n):
    rows = []
    for _ in range(n):
        a, b, noise = random.gauss(0, 1), random.gauss(0, 1), random.gauss(0, 1)
        y = 1 if 2.0 * a + 0.5 * b + random.gauss(0, 0.5) > 0 else 0                # feature a matters most, b a little, noise not at all
        rows.append(([a, b, noise], y))
    return rows
train, test = make(2000), make(1000)
w, bias = [0.0, 0.0, 0.0], 0.0
import math
for _ in range(60):                                                                  # logistic regression by gradient descent
    gw, gb = [0.0] * 3, 0.0
    for x, y in train:
        p = 1 / (1 + math.exp(-(sum(wi * xi for wi, xi in zip(w, x)) + bias))); e = p - y
        gw = [g + e * xi for g, xi in zip(gw, x)]; gb += e
    w = [wi - 0.5 * g / len(train) for wi, g in zip(w, gw)]; bias -= 0.5 * gb / len(train)
def accuracy(rows): return sum(((sum(wi * xi for wi, xi in zip(w, x)) + bias) > 0) == (y == 1) for x, y in rows) / len(rows)
base = accuracy(test)
print("learned weights:", [round(v, 2) for v in w], "| test accuracy:", round(base, 3))
for j, name in enumerate(["a", "b", "noise"]):
    drops = []
    for _ in range(10):
        col = [x[j] for x, _ in test]; random.shuffle(col)
        shuffled = [([*x[:j], col[i], *x[j + 1:]], y) for i, (x, y) in enumerate(test)]
        drops.append(base - accuracy(shuffled))
    print(f"permuting {name:>5}: accuracy drops by {sum(drops) / len(drops):.3f}")
