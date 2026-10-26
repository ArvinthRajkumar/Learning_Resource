def merge_fields(base, mine, theirs):
    merged, conflicts = {}, []
    for k in sorted(base.keys() | mine.keys() | theirs.keys()):
        b, m, t = base.get(k), mine.get(k), theirs.get(k)
        if m == t: merged[k] = m
        elif m == b: merged[k] = t                    # only the other side changed it
        elif t == b: merged[k] = m                    # only I changed it
        else: conflicts.append(k); merged[k] = t       # both changed differently: needs a rule or the user
    return merged, sorted(conflicts)
base = {"title": "Trip", "date": "May 1", "notes": "pack"}
mine = {"title": "Trip to Goa", "date": "May 1", "notes": "pack sunscreen"}
theirs = {"title": "Trip", "date": "May 3", "notes": "pack"}
print(merge_fields(base, mine, theirs))
print("both edited the notes differently:", merge_fields(base, mine, {"title": "Trip", "date": "May 1", "notes": "pack hat"}))
