it = iter([10, 20])
print(next(it), next(it))
try:
    next(it)
except StopIteration:
    print("exhausted")

class Countdown:
    def __init__(self, n): self.n = n
    def __iter__(self): return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1
print(list(Countdown(3)))
