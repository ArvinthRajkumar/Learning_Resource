class Vec:
    __slots__ = ("x", "y")
    def __init__(self, x, y): self.x, self.y = x, y
    def __repr__(self): return f"Vec({self.x}, {self.y})"
    def __add__(self, o): return Vec(self.x + o.x, self.y + o.y)
    def __eq__(self, o): return isinstance(o, Vec) and (self.x, self.y) == (o.x, o.y)
    def __hash__(self): return hash((self.x, self.y))
    def __bool__(self): return bool(self.x or self.y)
    def __len__(self): return 2
v = Vec(1, 2)
print(v + Vec(3, 4), "| equal:", v == Vec(1, 2), "| usable in a set:", len({v, Vec(1, 2)}) == 1, "| truthiness:", bool(Vec(0, 0)), "| no __dict__:", not hasattr(v, "__dict__"))
