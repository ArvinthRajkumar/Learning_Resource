import math
def layernorm(x, eps=1e-5):
    m = sum(x) / len(x)
    v = sum((a - m) ** 2 for a in x) / len(x)
    return [(a - m) / math.sqrt(v + eps) for a in x]
def rmsnorm(x, eps=1e-5):
    r = math.sqrt(sum(a * a for a in x) / len(x) + eps)
    return [a / r for a in x]
x = [10.0, 12.0, 8.0, 14.0]
y = layernorm(x)
print("layernorm:", [round(v, 3) for v in y], "mean %.3f" % (sum(y) / len(y)))
print("rmsnorm  :", [round(v, 3) for v in rmsnorm(x)])
