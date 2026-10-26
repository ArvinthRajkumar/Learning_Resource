from collections import OrderedDict, defaultdict
class EventEmitter:
    def __init__(self): self.handlers = defaultdict(list)
    def on(self, event, fn): self.handlers[event].append(fn); return lambda: self.handlers[event].remove(fn)    # returns an unsubscribe function
    def once(self, event, fn):
        def wrapper(*a):
            off(); return fn(*a)
        off = self.on(event, wrapper)
    def emit(self, event, *args): return [fn(*args) for fn in list(self.handlers[event])]                       # copy: handlers may unsubscribe
em, log = EventEmitter(), []
off = em.on("data", lambda x: log.append(("always", x)))
em.once("data", lambda x: log.append(("once", x)))
em.emit("data", 1); em.emit("data", 2); off(); em.emit("data", 3)
print(log)
def lru_memo(capacity):
    def deco(fn):
        cache = OrderedDict()
        def wrapper(*args):
            if args in cache: cache.move_to_end(args); return cache[args]
            val = fn(*args); cache[args] = val
            if len(cache) > capacity: cache.popitem(last=False)
            return val
        wrapper.cache = cache
        return wrapper
    return deco
calls = []
@lru_memo(2)
def square(x): calls.append(x); return x * x
square(2); square(3); square(2); square(4); square(3)
print("underlying calls (3 was evicted when 4 arrived):", calls)
