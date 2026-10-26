import random
random.seed(5)
a_conv, a_n, b_conv, b_n = 480, 10000, 540, 10000
wins, diffs = 0, []
for _ in range(20000):
    pa = random.betavariate(1 + a_conv, 1 + a_n - a_conv)
    pb = random.betavariate(1 + b_conv, 1 + b_n - b_conv)
    wins += pb > pa
    diffs.append(pb - pa)
diffs.sort()
print("P(B beats A) = %.3f, 95%% credible interval for the lift (%.4f, %.4f)" % (wins / 20000, diffs[500], diffs[19499]))
