import uuid
class Server:
    def __init__(self): self.items, self.seen = {}, set()
    def apply(self, op):
        if op["id"] in self.seen: return "duplicate ignored"               # idempotent by operation id
        self.seen.add(op["id"]); self.items[op["item"]] = op["value"]; return "applied"
class Client:
    def __init__(self, server): self.server, self.local, self.outbox, self.online = server, {}, [], False
    def set(self, item, value):
        self.local[item] = value                                          # optimistic: UI updates at once
        self.outbox.append({"id": str(uuid.uuid4())[:8], "item": item, "value": value})
    def sync(self):
        if not self.online: return "offline: nothing sent, %d queued" % len(self.outbox)
        results = []
        for op in list(self.outbox):
            results.append(self.server.apply(op))
            if len(results) == 1: results.append(self.server.apply(op))      # simulate an ack lost -> the client retries the same op
            self.outbox.remove(op)
        return results
srv = Server(); cl = Client(srv)
cl.set("note", "draft 1"); cl.set("note", "draft 2"); cl.set("title", "Trip")
print(cl.sync(), "| local view:", cl.local)
cl.online = True
print(cl.sync(), "| server state:", srv.items)
