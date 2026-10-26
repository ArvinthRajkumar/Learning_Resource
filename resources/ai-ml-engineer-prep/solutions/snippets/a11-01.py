import random, math
random.seed(0)
population = [random.gauss(100, 15) for _ in range(100000)]
for n in (10, 100, 1000):
    means = []
    for _ in range(2000):
        sample = random.sample(population, n)
        means.append(sum(sample) / n)
    m = sum(means) / len(means)
    se = math.sqrt(sum((x - m) ** 2 for x in means) / len(means))
    print("n=%4d  spread of sample means %.2f   theory 15/sqrt(n) = %.2f" % (n, se, 15 / math.sqrt(n)))
