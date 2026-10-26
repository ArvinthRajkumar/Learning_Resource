import random
random.seed(0)
means = [sum(random.random() for _ in range(30)) / 30 for _ in range(5000)]   # averages of uniform draws
m = sum(means) / len(means)
sd = (sum((x - m) ** 2 for x in means) / len(means)) ** 0.5
inside = sum(abs(x - m) < sd for x in means) / len(means)
print("mean %.3f, std %.3f (theory %.3f), within 1 std: %.2f (normal: 0.68)" % (m, sd, (1 / 12 / 30) ** 0.5, inside))
