from contextlib import contextmanager
import os

@contextmanager
def temp_env(**values):
    old = {k: os.environ.get(k) for k in values}
    os.environ.update({k: str(v) for k, v in values.items()})
    try:
        yield
    finally:
        for k, v in old.items():
            if v is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = v

with temp_env(MODE="test"):
    print(os.environ["MODE"])
print(os.environ.get("MODE"))
