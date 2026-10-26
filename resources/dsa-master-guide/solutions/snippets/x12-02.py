import zlib
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
buckets = {}
for w in words: buckets.setdefault(zlib.crc32(w.encode()) % 4, []).append(w)         # 7 words, 4 hooks: collisions are normal
print("words per hook:", sorted(len(v) for v in buckets.values()), "| lookup still checks only one hook")
