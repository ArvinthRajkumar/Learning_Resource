import math
data = [1, 0, 1, 1, 0, 1, 1, 1]          # coin flips
def loglik(p): return sum(math.log(p if x else 1 - p) for x in data)
best = max((i / 100 for i in range(1, 100)), key=loglik)
print("MLE of p: %.2f (sample mean %.2f)" % (best, sum(data) / len(data)))
