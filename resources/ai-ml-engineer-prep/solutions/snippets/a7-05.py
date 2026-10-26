import math
def ab_test(conv_a, n_a, conv_b, n_b):
    pa, pb = conv_a / n_a, conv_b / n_b
    p = (conv_a + conv_b) / (n_a + n_b)
    se = math.sqrt(p * (1 - p) * (1 / n_a + 1 / n_b))
    z = (pb - pa) / se
    return pa, pb, z
pa, pb, z = ab_test(480, 10000, 540, 10000)
print("rate A %.2f%%, rate B %.2f%%, z = %.2f (|z| > 1.96 means p < 0.05)" % (pa * 100, pb * 100, z))
def sample_size(p, mde, z_a=1.96, z_b=0.84):          # per group, two-sided alpha 0.05, power 80%
    return int(2 * ((z_a + z_b) ** 2) * p * (1 - p) / mde ** 2) + 1
print("users per group to detect a 0.5 point lift on a 5%% base: %d" % sample_size(0.05, 0.005))
