import random
random.seed(3)
m, alpha = 100, 0.05
pvals = sorted(random.random() for _ in range(m))             # 100 tests where the null is true everywhere
print("raw 'significant' results:", sum(p < alpha for p in pvals))
print("Bonferroni significant   :", sum(p < alpha / m for p in pvals))
bh = max([i for i, p in enumerate(pvals, 1) if p <= alpha * i / m], default=0)
print("Benjamini-Hochberg       :", bh)
