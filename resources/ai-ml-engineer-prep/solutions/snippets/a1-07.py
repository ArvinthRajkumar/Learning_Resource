import random
random.seed(3)
def one_model():           # a noisy estimator of the true value 10
    return 10 + random.gauss(0, 3)
single = [one_model() for _ in range(4000)]
bagged = [sum(one_model() for _ in range(25)) / 25 for _ in range(4000)]
var = lambda v: sum((x - sum(v) / len(v)) ** 2 for x in v) / len(v)
print("variance single %.2f, averaged over 25 independent models %.2f" % (var(single), var(bagged)))
