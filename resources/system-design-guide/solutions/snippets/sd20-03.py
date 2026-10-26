class Lazy:
    """Miniature lazy pipeline: transformations record steps, an action runs them."""
    def __init__(self, data, steps=()): self.data, self.steps = data, tuple(steps)
    def map(self, f): return Lazy(self.data, self.steps + (("map", f),))
    def filter(self, f): return Lazy(self.data, self.steps + (("filter", f),))
    def collect(self):
        out = []
        for x in self.data:                       # one pass: narrow steps are pipelined
            keep = True
            for kind, f in self.steps:
                if kind == "map": x = f(x)
                elif not f(x): keep = False; break
            if keep: out.append(x)
        return out
pipeline = Lazy(range(10)).map(lambda x: x * x).filter(lambda x: x % 2 == 0).map(lambda x: x + 1)
print("steps recorded, nothing computed yet:", len(pipeline.steps))
print("action runs the DAG:", pipeline.collect())
