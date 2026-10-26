class ExpensiveReport:
    def __init__(self): print("(building the report: slow)"); self.rows = [1, 2, 3]
class LazyReport:                                       # proxy: build only when first used
    def __init__(self): self._real = None
    def __getattr__(self, name):
        if self._real is None: self._real = ExpensiveReport()
        return getattr(self._real, name)
r = LazyReport()
print("created the proxy, nothing built yet")
print(r.rows, r.rows)
