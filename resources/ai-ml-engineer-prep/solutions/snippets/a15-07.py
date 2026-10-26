triples = [("ana", "parent_of", "bo"), ("bo", "parent_of", "cy"), ("bo", "parent_of", "di"), ("cy", "lives_in", "pune"), ("di", "lives_in", "goa"), ("ana", "lives_in", "pune")]
parents = {}
for h, r, t in triples:
    if r == "parent_of": parents.setdefault(h, []).append(t)
grandparents = sorted((g, c) for g, kids in parents.items() for p in kids for c in parents.get(p, []))
print("inferred grandparent_of:", grandparents)
lives = {h: t for h, r, t in triples if r == "lives_in"}
print("grandchildren who live where the grandparent lives:", [(g, c) for g, c in grandparents if lives.get(g) == lives.get(c)])
