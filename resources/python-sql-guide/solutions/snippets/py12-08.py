from typing import Optional, Iterable, Callable, TypeVar, Protocol
T = TypeVar("T")
def first(items: Iterable[T], default: Optional[T] = None) -> Optional[T]:
    return next(iter(items), default)
def apply_all(fns: list[Callable[[int], int]], x: int) -> list[int]:
    return [f(x) for f in fns]
class Shape(Protocol):
    def area(self) -> float: ...
class Sq:
    def __init__(self, s: float): self.s = s
    def area(self) -> float: return self.s ** 2
def total_area(shapes: list[Shape]) -> float: return sum(s.area() for s in shapes)
print(first([]), first("xyz"), apply_all([lambda v: v + 1, lambda v: v * 2], 5), total_area([Sq(2), Sq(3)]))
print("hints are metadata only:", first.__annotations__["default"])
