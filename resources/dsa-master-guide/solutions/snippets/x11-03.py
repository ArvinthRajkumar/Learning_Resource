import bisect, random
random.seed(1)
class TimeMap:
    def __init__(self): self.data = {}                                  # key -> (timestamps, values)
    def set(self, key, value, ts):
        times, vals = self.data.setdefault(key, ([], []))
        times.append(ts); vals.append(value)                            # timestamps arrive in increasing order
    def get(self, key, ts):
        if key not in self.data: return ""
        times, vals = self.data[key]
        i = bisect.bisect_right(times, ts)
        return vals[i - 1] if i else ""
tm = TimeMap()
tm.set("k", "a", 1); tm.set("k", "b", 4); tm.set("k", "c", 9)
assert [tm.get("k", t) for t in (0, 1, 3, 4, 8, 100)] == ["", "a", "a", "b", "b", "c"] and tm.get("zzz", 5) == ""
history = []
for ts in range(1, 200, 3):
    v = random.randint(0, 9); tm.set("r", v, ts); history.append((ts, v))
for q in range(0, 210, 7):
    expected = next((v for ts, v in reversed(history) if ts <= q), "")
    assert tm.get("r", q) == expected
print("TimeMap verified against a linear scan of the history")
