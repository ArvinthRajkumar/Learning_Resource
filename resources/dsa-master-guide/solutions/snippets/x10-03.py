import random
def inside(poly, p):
    x, y, c = p[0], p[1], False
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y):                                          # the edge straddles the horizontal line through p
            x_cross = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < x_cross: c = not c
    return c
square = [(0, 0), (10, 0), (10, 10), (0, 10)]
concave = [(0, 0), (10, 0), (10, 10), (5, 3), (0, 10)]                       # a notch cut into the top
print("square:", inside(square, (5, 5)), inside(square, (11, 5)), "| concave notch point (5, 8) is outside:", not inside(concave, (5, 8)), "| (5, 2) inside:", inside(concave, (5, 2)))
