import math
def desired(current, metric, target, lo=2, hi=50):
    return max(lo, min(hi, math.ceil(current * metric / target)))
replicas, target = 4, 60
for minute, cpu in enumerate([55, 90, 95, 70, 40, 30, 50]):
    new = desired(replicas, cpu, target)
    print(f"min {minute}: cpu {cpu}% with {replicas} pods -> {new}")
    replicas = new
