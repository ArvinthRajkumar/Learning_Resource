import math, random
random.seed(0)
def forward_std(scale_fn, layers=20, width=256):
    x = [random.gauss(0, 1) for _ in range(width)]
    for _ in range(layers):
        s = scale_fn(width)
        x = [math.tanh(sum(random.gauss(0, s) * xi for xi in x)) for _ in range(width)]
    m = sum(x) / len(x)
    return math.sqrt(sum((v - m) ** 2 for v in x) / len(x))
print("std 0.01          :", round(forward_std(lambda n: 0.01, width=64), 6))
print("std 1.0           :", round(forward_std(lambda n: 1.0, width=64), 3))
print("Xavier 1/sqrt(n)  :", round(forward_std(lambda n: 1 / math.sqrt(n), width=64), 3))
