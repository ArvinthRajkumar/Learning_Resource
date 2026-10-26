import hashlib
def h(k): return int(hashlib.md5(k.encode()).hexdigest(), 16)
keys = ["user%d" % i for i in range(10000)]
before = {k: h(k) % 4 for k in keys}
after = {k: h(k) % 5 for k in keys}
moved = sum(1 for k in keys if before[k] != after[k])
print("moved when going from 4 to 5 shards:", moved, "of", len(keys), "(%.0f%%)" % (100 * moved / len(keys)))
