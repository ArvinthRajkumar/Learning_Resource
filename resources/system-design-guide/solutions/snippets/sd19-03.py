class Account:
    def __init__(self): self.balance, self.version = 0, 0
    def apply(self, e):
        if e["type"] == "Deposited": self.balance += e["amount"]
        elif e["type"] == "Withdrawn": self.balance -= e["amount"]
        self.version += 1
class EventStore:
    def __init__(self): self.events = []
    def append(self, event, expected_version):
        if len(self.events) != expected_version: raise RuntimeError(f"conflict: expected v{expected_version}, store is at v{len(self.events)}")
        self.events.append(event)
    def rebuild(self, upto=None):
        acc = Account()
        for e in self.events[:upto]: acc.apply(e)
        return acc
store = EventStore()
store.append({"type": "Deposited", "amount": 100}, 0)
store.append({"type": "Withdrawn", "amount": 30}, 1)
store.append({"type": "Deposited", "amount": 5}, 2)
print("current balance:", store.rebuild().balance, "| balance after 2 events:", store.rebuild(2).balance)
try:
    store.append({"type": "Withdrawn", "amount": 999}, 1)       # stale writer
except RuntimeError as e:
    print("rejected:", e)
