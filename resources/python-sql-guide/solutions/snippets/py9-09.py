class EventBus:
    def __init__(self): self.handlers = {}
    def subscribe(self, event, fn): self.handlers.setdefault(event, []).append(fn)
    def publish(self, event, payload):
        for fn in self.handlers.get(event, []): fn(payload)
log = []
bus = EventBus()
bus.subscribe("order.paid", lambda o: log.append(f"email receipt for {o['id']}"))
bus.subscribe("order.paid", lambda o: log.append(f"update stock for {o['id']}"))
bus.publish("order.paid", {"id": 7}); bus.publish("order.cancelled", {"id": 8})
print(log)
