import sys
class Plain:
    def __init__(self): self.a, self.b = 1, 2
class Slim:
    __slots__ = ("a", "b")
    def __init__(self): self.a, self.b = 1, 2
print("slots saves per-instance dict:", not hasattr(Slim(), "__dict__"))
