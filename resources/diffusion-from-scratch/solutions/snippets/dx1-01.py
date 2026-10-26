import random, math
random.seed(0)
T = 50
betas = [1e-4 + (0.05 - 1e-4) * i / (T - 1) for i in range(T)]
alpha_bar = []
p = 1.0
for b in betas:
    p *= 1 - b
    alpha_bar.append(p)

x0, n = 1.0, 20000
final = []
for _ in range(n):
    x = x0
    for b in betas:                                   # step by step through the chain
        x = math.sqrt(1 - b) * x + math.sqrt(b) * random.gauss(0, 1)
    final.append(x)
mean = sum(final) / n
var = sum((v - mean) ** 2 for v in final) / n
print("simulated  mean %.3f  var %.3f" % (mean, var))
print("closed form mean %.3f  var %.3f" % (math.sqrt(alpha_bar[-1]) * x0, 1 - alpha_bar[-1]))
