from collections import Counter, defaultdict
words = "the cat and the hat and the bat".split()
print(Counter(words).most_common(2))
groups = defaultdict(list)
for w in words:
    groups[len(w)].append(w)
print(dict(groups))
