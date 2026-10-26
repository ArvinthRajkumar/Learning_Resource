import random, zlib
random.seed(0)
keys = ["hot"] * 8000 + [f"k{i}" for i in range(2000)]
def load(keys, n=4, salt=1):
    buckets = [0] * n
    for k in keys:
        kk = f"{k}#{random.randrange(salt)}" if k == "hot" else k
        buckets[zlib.crc32(kk.encode()) % n] += 1
    return buckets
print("no salting :", load(keys, 4, 1), "-> one reducer carries most of the data")
print("salted x 16:", load(keys, 4, 16), "-> spread across reducers (then a small second aggregation)")
