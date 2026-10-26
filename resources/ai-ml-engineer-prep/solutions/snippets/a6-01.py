import math
sig = lambda z: 1 / (1 + math.exp(-z))
def loss(rw, rl): return -math.log(sig(rw - rl))
for rw, rl in ((2.0, 0.0), (0.5, 0.0), (0.0, 0.0), (-1.0, 1.0)):
    print("r_w=%5.1f r_l=%5.1f  P(w beats l)=%.3f  loss=%.3f" % (rw, rl, sig(rw - rl), loss(rw, rl)))
