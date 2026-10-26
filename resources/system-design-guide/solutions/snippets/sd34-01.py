import hashlib
def shard_for(key, n): return int(hashlib.md5(key.encode()).hexdigest(), 16) % n
keys = [f"user{i}" for i in range(10_000)]
before = {k: shard_for(k, 4) for k in keys}
after = {k: shard_for(k, 5) for k in keys}
moved = sum(before[k] != after[k] for k in keys)
print(f"mod-N hashing: adding a 5th shard moves {moved / len(keys):.0%} of all keys (that is why consistent hashing exists)")
