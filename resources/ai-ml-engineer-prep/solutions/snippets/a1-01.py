import random
random.seed(0)
xs = [i / 10 for i in range(100)]
ys = [2.0 * x + 1.0 + random.gauss(0, 0.3) for x in xs]       # true line: y = 2x + 1 plus noise

n = len(xs)
mx, my = sum(xs) / n, sum(ys) / n
w = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
b = my - w * mx
print("closed form      w=%.3f b=%.3f" % (w, b))

w2, b2, lr = 0.0, 0.0, 0.01
for _ in range(5000):
    gw = sum(2 * (w2 * x + b2 - y) * x for x, y in zip(xs, ys)) / n
    gb = sum(2 * (w2 * x + b2 - y) for x, y in zip(xs, ys)) / n
    w2, b2 = w2 - lr * gw, b2 - lr * gb
print("gradient descent w=%.3f b=%.3f" % (w2, b2))
