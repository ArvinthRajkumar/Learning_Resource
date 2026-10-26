import functools, time

def timed(fn):
    @functools.wraps(fn)                 # keep name and docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        wrapper.last = time.perf_counter() - start
        return result
    return wrapper

@timed
def work(n):
    """Add numbers."""
    return sum(range(n))

print(work(1000), work.__name__, work.__doc__, work.last >= 0)
