import zlib
from collections import defaultdict
from itertools import chain
docs = ["the cat sat on the mat", "the dog sat on the log", "the cat saw the dog"]
def mapper(doc): return [(w, 1) for w in doc.split()]
def combiner(pairs):                       # local pre-aggregation reduces shuffle volume
    local = defaultdict(int)
    for k, v in pairs: local[k] += v
    return list(local.items())
def shuffle(all_pairs, n_reducers=2):
    parts = [defaultdict(list) for _ in range(n_reducers)]
    for k, v in all_pairs: parts[zlib.crc32(k.encode()) % n_reducers][k].append(v)
    return parts
def reducer(k, vs): return k, sum(vs)
mapped = [combiner(mapper(d)) for d in docs]
raw = sum(len(mapper(d)) for d in docs); after = sum(len(m) for m in mapped)
parts = shuffle(chain.from_iterable(mapped))
result = dict(reducer(k, vs) for p in parts for k, vs in p.items())
print("top words:", sorted(result.items(), key=lambda kv: (-kv[1], kv[0]))[:4])
print(f"pairs shuffled: {raw} without combiner, {after} with combiner")
