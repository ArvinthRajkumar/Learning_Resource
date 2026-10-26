import math
def rotate(vec, pos, theta=0.1):
    out = []
    for i in range(0, len(vec), 2):
        a = pos * theta * (i // 2 + 1)
        x, y = vec[i], vec[i + 1]
        out += [x * math.cos(a) - y * math.sin(a), x * math.sin(a) + y * math.cos(a)]
    return out
q, k = [1.0, 0.5, -0.3, 0.8], [0.7, -0.2, 0.4, 0.9]
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
print("q at 5, k at 3  :", round(dot(rotate(q, 5), rotate(k, 3)), 6))
print("q at 12, k at 10:", round(dot(rotate(q, 12), rotate(k, 10)), 6))   # same relative offset 2
print("q at 5, k at 4  :", round(dot(rotate(q, 5), rotate(k, 4)), 6))     # different offset
