class Circle:
    def __init__(self, r): self._r = r
    @property
    def radius(self): return self._r
    @radius.setter
    def radius(self, v):
        if v < 0: raise ValueError("radius must be non-negative")
        self._r = v
    @property
    def area(self): return 3.14159 * self._r ** 2     # computed on access

c = Circle(2)
c.radius = 3
print(c.radius, round(c.area, 2))
try:
    c.radius = -1
except ValueError as e:
    print("error:", e)
