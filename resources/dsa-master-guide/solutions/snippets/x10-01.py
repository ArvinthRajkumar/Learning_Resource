def cross(o, a, b): return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
def orient(p, q, r):
    c = cross(p, q, r)
    return "left turn (counter-clockwise)" if c > 0 else "right turn (clockwise)" if c < 0 else "collinear"
print(orient((0, 0), (4, 0), (4, 3)), "|", orient((0, 0), (4, 0), (4, -3)), "|", orient((0, 0), (2, 2), (5, 5)))
def polygon_area2(pts):                                                  # shoelace formula: twice the area, exact integer
    return sum(pts[i][0] * pts[(i + 1) % len(pts)][1] - pts[(i + 1) % len(pts)][0] * pts[i][1] for i in range(len(pts)))
square = [(0, 0), (4, 0), (4, 4), (0, 4)]
print("twice the area of a 4x4 square:", polygon_area2(square), "| clockwise order gives a negative value:", polygon_area2(square[::-1]))
