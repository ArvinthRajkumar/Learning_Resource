import math, random
random.seed(0)
def stats(xs):
    m = sum(xs) / len(xs)
    return m, math.sqrt(sum((x - m) ** 2 for x in xs) / len(xs))
def fid_1d(a, b):
    (ma, sa), (mb, sb) = stats(a), stats(b)
    return (ma - mb) ** 2 + (sa - sb) ** 2
real = [random.gauss(0, 1) for _ in range(5000)]
good = [random.gauss(0.05, 1.0) for _ in range(5000)]       # close to real
shifted = [random.gauss(1.0, 1.0) for _ in range(5000)]     # wrong mean
collapsed = [random.gauss(0, 0.2) for _ in range(5000)]     # mode collapse: too little spread
print("good      FID %.3f" % fid_1d(real, good))
print("shifted   FID %.3f" % fid_1d(real, shifted))
print("collapsed FID %.3f" % fid_1d(real, collapsed))
