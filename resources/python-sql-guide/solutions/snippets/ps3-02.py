import functools, time
def timed(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        wrapper.last_seconds = time.perf_counter() - start                     # the "backpack": wrapper remembers fn
        return result
    return wrapper
@timed
def add(a, b): return a + b
print(add(2, 3), "| name preserved by wraps:", add.__name__, "| measured something:", add.last_seconds >= 0)
