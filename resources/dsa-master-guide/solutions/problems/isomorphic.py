def isomorphic(s, t):
    if len(s) != len(t):
        return False
    a_to_b, b_to_a = {}, {}
    for x, y in zip(s, t):
        if a_to_b.setdefault(x, y) != y or b_to_a.setdefault(y, x) != x:
            return False
    return True
