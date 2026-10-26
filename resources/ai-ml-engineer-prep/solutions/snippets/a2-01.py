import math
a, b = [1.0, 2.0, 3.0], [4.0, 0.0, -1.0]
dot = sum(x * y for x, y in zip(a, b))
norm = lambda v: math.sqrt(sum(x * x for x in v))
print("dot", dot, "norms", round(norm(a), 3), round(norm(b), 3))
print("cosine", round(dot / (norm(a) * norm(b)), 3))
print("cosine of a with 2a:", round(sum(x * 2 * x for x in a) / (norm(a) * norm([2 * x for x in a])), 3))
