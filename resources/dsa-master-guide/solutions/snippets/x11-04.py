import random
random.seed(2)
class MinStack:
    def __init__(self): self.s = []                                      # (value, min of stack up to here)
    def push(self, x): self.s.append((x, min(x, self.s[-1][1]) if self.s else x))
    def pop(self): return self.s.pop()[0]
    def top(self): return self.s[-1][0]
    def get_min(self): return self.s[-1][1]
ms, ref = MinStack(), []
for _ in range(2000):
    if ref and random.random() < 0.45: assert ms.pop() == ref.pop()
    else: x = random.randint(-50, 50); ms.push(x); ref.append(x)
    if ref: assert ms.get_min() == min(ref) and ms.top() == ref[-1]
print("min stack verified against recomputing min over a plain list")
