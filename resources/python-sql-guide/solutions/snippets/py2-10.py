from typing import Optional, Callable, Iterable, TypeVar, Protocol

T = TypeVar("T")

def first(items: Iterable[T]) -> Optional[T]:
    for x in items:
        return x
    return None

def apply(fn: Callable[[int], int], xs: list[int]) -> list[int]:
    return [fn(x) for x in xs]

class Drawable(Protocol):
    def draw(self) -> str: ...

class Box:
    def draw(self) -> str: return "[]"

def render(d: Drawable) -> str: return d.draw()

print(first([]), first("abc"), apply(lambda n: n + 1, [1, 2]), render(Box()))
