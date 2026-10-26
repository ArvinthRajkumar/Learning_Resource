from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...

class Square(Shape):
    def __init__(self, s): self.s = s
    def area(self): return self.s ** 2

try:
    Shape()
except TypeError:
    print("cannot instantiate an abstract class")
print(Square(3).area())
