from dataclasses import dataclass, field, replace

@dataclass(order=True, frozen=True)
class Item:
    name: str
    price: float
    tags: tuple = ()

@dataclass
class Cart:
    items: list = field(default_factory=list)    # never use [] directly
    def total(self): return sum(i.price for i in self.items)

a, b = Item("pen", 2.5), Item("book", 12.0, ("paper",))
cart = Cart([a, b])
print(a, cart.total(), a < b, replace(a, price=3))
