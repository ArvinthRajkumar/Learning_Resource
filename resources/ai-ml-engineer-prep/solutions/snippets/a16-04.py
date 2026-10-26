import random, math
random.seed(3)
ages = [random.randint(18, 80) for _ in range(1000)]
true_count = sum(a > 60 for a in ages)                              # a counting query: sensitivity 1 (one person changes it by at most 1)
def laplace(scale):                                                 # Laplace noise as the difference of two exponentials
    return random.expovariate(1 / scale) - random.expovariate(1 / scale)
def private_count(epsilon): return true_count + laplace(1 / epsilon)
print("true count of people over 60:", true_count)
for eps in (0.1, 1.0, 10.0):
    answers = [private_count(eps) for _ in range(2000)]
    err = sum(abs(a - true_count) for a in answers) / len(answers)
    print(f"epsilon {eps:>4}: typical absolute error {err:6.2f} (theory: 1/epsilon = {1 / eps:5.1f})")
