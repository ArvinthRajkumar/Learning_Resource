import math
vec = {"king": (0.9, 0.8), "queen": (0.85, 0.75), "man": (0.8, 0.3), "woman": (0.75, 0.25), "banana": (-0.5, 0.1)}
cos = lambda a, b: sum(x * y for x, y in zip(a, b)) / (math.hypot(*a) * math.hypot(*b))
for a, b in [("king", "queen"), ("man", "woman"), ("king", "banana")]: print(f"similarity({a}, {b}) = {cos(vec[a], vec[b]):+.2f}")
