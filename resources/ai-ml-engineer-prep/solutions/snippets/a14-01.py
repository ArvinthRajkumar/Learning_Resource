def beta_summary(a, b):
    mean = a / (a + b); var = a * b / ((a + b) ** 2 * (a + b + 1))
    return mean, var ** 0.5
prior = (1, 1)                                              # uniform: we know nothing
print("prior Beta(1,1): mean %.2f, std %.2f" % beta_summary(*prior))
heads, tails = 7, 3
post = (prior[0] + heads, prior[1] + tails)
print(f"after {heads} heads and {tails} tails -> Beta{post}: mean %.3f, std %.3f (MLE would say %.1f)" % (*beta_summary(*post), heads / (heads + tails)))
informative = (20, 20)                                      # a strong belief that the coin is fair
post2 = (informative[0] + heads, informative[1] + tails)
print(f"with a strong 'fair coin' prior Beta(20,20) -> Beta{post2}: mean %.3f" % beta_summary(*post2)[0])
big = (prior[0] + 700, prior[1] + 300)
print("with 1000 flips (700 heads) the prior hardly matters: mean %.3f, std %.3f" % beta_summary(*big))
