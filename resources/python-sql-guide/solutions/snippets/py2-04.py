class Vector:
    def __init__(self, x, y): self.x, self.y = x, y
    def __repr__(self): return f"Vector({self.x}, {self.y})"
    def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)
    def __mul__(self, k): return Vector(self.x * k, self.y * k)
    def __eq__(self, o): return isinstance(o, Vector) and (self.x, self.y) == (o.x, o.y)
    def __hash__(self): return hash((self.x, self.y))
    def __len__(self): return 2
    def __iter__(self): yield self.x; yield self.y
    def __bool__(self): return bool(self.x or self.y)
    def __getitem__(self, i): return (self.x, self.y)[i]

v = Vector(1, 2) + Vector(3, 4)
print(v, v * 2, v == Vector(4, 6), len(v), list(v), v[0], bool(Vector(0, 0)))
print({v: "ok"}[Vector(4, 6)])
