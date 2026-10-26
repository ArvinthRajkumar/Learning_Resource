import statistics
lat = [10] * 99 + [1000]
print("mean =", statistics.mean(lat))
print("median =", statistics.median(lat))
s = sorted(lat)
print("p99 =", s[int(0.99 * len(s)) - 1], "max =", s[-1])
