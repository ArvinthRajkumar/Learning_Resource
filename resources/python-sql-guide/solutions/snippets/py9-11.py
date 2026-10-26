TRANSITIONS = {("created", "pay"): "paid", ("paid", "ship"): "shipped", ("shipped", "deliver"): "delivered",
               ("created", "cancel"): "cancelled", ("paid", "cancel"): "refunded"}
class Order:
    def __init__(self): self.state = "created"
    def fire(self, event):
        nxt = TRANSITIONS.get((self.state, event))
        if nxt is None: raise ValueError(f"cannot {event} from {self.state}")
        self.state = nxt; return self
o = Order().fire("pay").fire("ship")
print(o.state)
try: o.fire("cancel")
except ValueError as e: print("rejected:", e)
