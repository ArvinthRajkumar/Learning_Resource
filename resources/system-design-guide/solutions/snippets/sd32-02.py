class ChangeLog:
    def __init__(self): self.seq, self.entries = 0, []
    def record(self, op, key, value=None):
        self.seq += 1; self.entries.append((self.seq, op, key, value))
    def since(self, token, limit=3):
        page = [e for e in self.entries if e[0] > token][:limit]
        return page, (page[-1][0] if page else token), len(page) == limit            # entries, next token, more pages?
log = ChangeLog()
for k, v in [("a", 1), ("b", 2), ("c", 3)]: log.record("put", k, v)
log.record("delete", "b"); log.record("put", "d", 4); log.record("put", "a", 10)
state, token, more = {}, 0, True
while more:
    page, token, more = log.since(token)
    for seq, op, key, value in page:
        if op == "put": state[key] = value
        else: state.pop(key, None)
    print("fetched", [(s, o, k) for s, o, k, _ in page], "-> token", token)
print("final client state:", state, "| matches replaying the full log:", state == {"a": 10, "c": 3, "d": 4})
