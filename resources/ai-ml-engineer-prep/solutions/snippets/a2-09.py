import math
def H(p): return -sum(x * math.log2(x) for x in p if x > 0)
def CE(p, q): return -sum(a * math.log2(b) for a, b in zip(p, q) if a > 0)
def KL(p, q): return CE(p, q) - H(p)
fair, biased = [0.5, 0.5], [0.9, 0.1]
print("H(fair)=%.3f H(biased)=%.3f" % (H(fair), H(biased)))
print("CE(fair, biased)=%.3f KL(fair||biased)=%.3f KL(biased||fair)=%.3f" % (CE(fair, biased), KL(fair, biased), KL(biased, fair)))
