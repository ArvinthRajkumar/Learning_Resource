from collections import Counter
lines = ["to be or not to be", "to see or not to see"]
# map: emit (word, 1); shuffle+reduce: sum per word
pairs = [(w, 1) for line in lines for w in line.split()]
counts = Counter()
for w, n in pairs:
    counts[w] += n
print(sorted(counts.items()))
