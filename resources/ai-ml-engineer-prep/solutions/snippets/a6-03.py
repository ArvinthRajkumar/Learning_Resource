import math
sig = lambda z: 1 / (1 + math.exp(-z))
def dpo_loss(lp_w, lp_l, ref_w, ref_l, beta=0.1):
    margin = beta * ((lp_w - ref_w) - (lp_l - ref_l))
    return -math.log(sig(margin)), margin
print("untrained policy == reference: loss %.3f, margin %.2f" % dpo_loss(-10, -12, -10, -12))
print("policy raised preferred, lowered rejected: loss %.3f, margin %.2f" % dpo_loss(-8, -15, -10, -12))
