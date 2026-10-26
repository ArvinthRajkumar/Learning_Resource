class Positive:
    def __set_name__(self, owner, name): self.name = "_" + name
    def __get__(self, obj, owner=None): return self if obj is None else getattr(obj, self.name)
    def __set__(self, obj, value):
        if value <= 0: raise ValueError("must be positive")
        setattr(obj, self.name, value)
class Product:
    price = Positive()
    def __init__(self, price): self.price = price
p = Product(5)
try: p.price = -1
except ValueError as e: print("validation via descriptor:", e, "| price still", p.price)
class Registry:
    items = []
    def __init_subclass__(cls, **kw): Registry.items.append(cls.__name__)
class Plugin1(Registry): pass
class Plugin2(Registry): pass
print("subclasses registered automatically:", Registry.items, "| type of a class:", type(Product).__name__)
