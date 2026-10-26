from itertools import combinations
from math import factorial
def model(x1, x2, x3): return 3 * x1 + 2 * x2 * x3 + 1                                # a model with an interaction between x2 and x3
instance, baseline = (1.0, 2.0, 3.0), (0.0, 0.0, 0.0)
def value(subset):                                                                    # features outside the subset take baseline values
    return model(*[instance[i] if i in subset else baseline[i] for i in range(3)])
n = 3; shap = []
for i in range(n):
    total = 0.0; others = [j for j in range(n) if j != i]
    for k in range(n):
        for S in combinations(others, k):
            weight = factorial(k) * factorial(n - k - 1) / factorial(n)
            total += weight * (value(set(S) | {i}) - value(set(S)))
    shap.append(total)
print("Shapley values:", [round(v, 2) for v in shap])
print("they sum to prediction minus baseline:", round(sum(shap), 2), "=", model(*instance) - model(*baseline))
print("x2 and x3 each receive half of the interaction term 2*x2*x3 = 12:", shap[1], shap[2])
