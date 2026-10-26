import functools, time
def retry(times=3, exceptions=(Exception,)):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a, **kw):
            for attempt in range(1, times + 1):
                try: return fn(*a, **kw)
                except exceptions as e:
                    if attempt == times: raise
        return wrapper
    return deco
calls = {"n": 0}
@retry(times=3, exceptions=(ConnectionError,))
def fetch():
    calls["n"] += 1
    if calls["n"] < 3: raise ConnectionError("flaky")
    return "ok"
print(fetch(), "after", calls["n"], "attempts | name preserved:", fetch.__name__)
