import math
def wilson(wins, n, z=1.96):
    p = wins / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return round(centre - half, 3), round(centre + half, 3)
print("model A preferred in 62 of 100 comparisons ->", wilson(62, 100))
print("model A preferred in 620 of 1000 comparisons ->", wilson(620, 1000))
