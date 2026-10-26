def is_anagram(a, b):
    if len(a) != len(b):
        return False
    c = [0] * 26
    for x, y in zip(a, b):
        c[ord(x) - 97] += 1
        c[ord(y) - 97] -= 1
    return not any(c)
