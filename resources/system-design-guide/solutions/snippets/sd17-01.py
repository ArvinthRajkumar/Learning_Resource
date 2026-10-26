from abc import ABC, abstractmethod

# Strategy: pricing algorithms are interchangeable
class Pricing(ABC):
    @abstractmethod
    def fee(self, hours): ...
class Hourly(Pricing):
    def fee(self, hours): return 5 * hours
class DayCap(Pricing):
    def fee(self, hours): return min(5 * hours, 30)

# Observer: listeners react to events
class EventBus:
    def __init__(self): self.subs = []
    def subscribe(self, fn): self.subs.append(fn)
    def publish(self, event):
        for fn in self.subs: fn(event)

bus = EventBus()
bus.subscribe(lambda e: print("email:", e))
bus.subscribe(lambda e: print("audit:", e))
bus.publish("order_placed")
print(Hourly().fee(10), DayCap().fee(10))
