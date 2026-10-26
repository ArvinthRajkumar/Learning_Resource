import random, math
random.seed(4)
dim = 100
w_true = [random.gauss(0, 1) for _ in range(dim)]
def sample():
    y = random.choice([-1, 1]); x = [y * 0.2 * wi + random.gauss(0, 1) for wi in w_true]; return x, y         # many small weak signals
train = [sample() for _ in range(2000)]
w = [0.0] * dim
for _ in range(40):
    grad = [0.0] * dim
    for x, y in train:
        z = y * sum(wi * xi for wi, xi in zip(w, x)); s = -y / (1 + math.exp(z))
        grad = [g + s * xi for g, xi in zip(grad, x)]
    w = [wi - 0.1 * g / len(train) for wi, g in zip(w, grad)]
test = [sample() for _ in range(1000)]
acc = lambda data: sum((sum(wi * xi for wi, xi in zip(w, x)) > 0) == (y == 1) for x, y in data) / len(data)
def attack(x, y, eps): return [xi - eps * y * (1 if wi > 0 else -1) for xi, wi in zip(x, w)]              # step against the true class along sign(w)
print("clean accuracy:", round(acc(test), 3))
for eps in (0.05, 0.1, 0.2, 0.4):
    print(f"perturbation of size {eps} per coordinate -> accuracy {acc([(attack(x, y, eps), y) for x, y in test]):.3f}")
