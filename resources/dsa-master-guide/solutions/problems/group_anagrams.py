from collections import defaultdict

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        groups["".join(sorted(w))].append(w)   # canonical key
    return sorted(sorted(g) for g in groups.values())
