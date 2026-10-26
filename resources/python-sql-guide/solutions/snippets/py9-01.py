# Before: nested, flag argument, unclear names
def p(d, f):
    if d:
        if f:
            return [x * 2 for x in d if x > 0]
        else:
            return [x for x in d if x > 0]
    else:
        return []
# After: guard clause, two intention-revealing functions
def positives(values): return [v for v in values if v > 0]
def doubled_positives(values): return [v * 2 for v in positives(values)]
print(p([3, -1, 4], True), doubled_positives([3, -1, 4]), positives([]), p([3, -1, 4], False) == positives([3, -1, 4]))
