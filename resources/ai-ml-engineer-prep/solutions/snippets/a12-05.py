# Compare two prompts on a small labelled set; report the difference with an exact sign test on disagreements.
from math import comb
a_correct = [1,1,0,1,0,1,1,0,1,1,0,1,1,1,0,1,0,1,1,1]
b_correct = [1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1]
b_only = sum(1 for x, y in zip(a_correct, b_correct) if y and not x)
a_only = sum(1 for x, y in zip(a_correct, b_correct) if x and not y)
n = a_only + b_only
p = 2 * sum(comb(n, k) for k in range(0, min(a_only, b_only) + 1)) / 2 ** n
print("A accuracy %.2f, B accuracy %.2f, B-only wins %d, A-only wins %d, sign test p = %.3f" % (sum(a_correct) / 20, sum(b_correct) / 20, b_only, a_only, p))
