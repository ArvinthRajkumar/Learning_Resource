import hashlib
def partition(key, n=4):
    return int(hashlib.md5(key.encode()).hexdigest(), 16) % n
events = [("alice", "login"), ("bob", "login"), ("alice", "buy"), ("alice", "logout"), ("bob", "buy")]
parts = {}
for key, ev in events:
    parts.setdefault(partition(key), []).append((key, ev))
for p in sorted(parts):
    print("partition", p, parts[p])     # per key, the order is preserved
