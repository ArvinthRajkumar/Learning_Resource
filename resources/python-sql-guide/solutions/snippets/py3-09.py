from contextlib import contextmanager, suppress, ExitStack

@contextmanager
def tag(name):
    print(f"<{name}>", end="")
    try:
        yield
    finally:
        print(f"</{name}>")

with tag("b"):
    print("bold", end="")

with suppress(FileNotFoundError):
    open("/definitely/missing.txt")
print("continued")
