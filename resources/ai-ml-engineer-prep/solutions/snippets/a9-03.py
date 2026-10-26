import math
users = {"u1": [1.0, 0.0], "u2": [0.0, 1.0]}
items = {"i1": [0.9, 0.1], "i2": [0.1, 0.9], "i3": [0.7, 0.7]}
def top(user_vec, k=2):
    scored = sorted(items, key=lambda i: -sum(a * b for a, b in zip(user_vec, items[i])))
    return scored[:k]
for u, v in users.items():
    print(u, "->", top(v))
