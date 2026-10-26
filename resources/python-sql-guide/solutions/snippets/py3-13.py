class Positive:
    def __set_name__(self, owner, name): self.name = "_" + name
    def __get__(self, obj, owner=None): return getattr(obj, self.name)
    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("must be positive")
        setattr(obj, self.name, value)

class Product:
    price = Positive()
    qty = Positive()
    def __init__(self, price, qty): self.price, self.qty = price, qty

p = Product(9.5, 3)
print(p.price, p.qty)
try:
    p.qty = 0
except ValueError as e:
    print("rejected:", e)
