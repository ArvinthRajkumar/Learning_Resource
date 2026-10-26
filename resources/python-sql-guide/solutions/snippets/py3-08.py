class Timer:
    def __enter__(self):
        print("start")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("stop", "with error" if exc_type else "cleanly")
        return False          # do not suppress the exception

with Timer():
    print("working")
try:
    with Timer():
        raise ValueError("boom")
except ValueError:
    print("error propagated")
