import random
random.seed(1)
def matmul(A, B): return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]
X = [[random.randint(-3, 3) for _ in range(4)] for _ in range(3)]
W1 = [[random.randint(-3, 3) for _ in range(6)] for _ in range(4)]          # first layer: split by columns
W2 = [[random.randint(-3, 3) for _ in range(4)] for _ in range(6)]          # second layer: split by rows
full = matmul(matmul(X, W1), W2)
W1_a, W1_b = [r[:3] for r in W1], [r[3:] for r in W1]                       # "GPU a" and "GPU b" each hold half the columns
W2_a, W2_b = W2[:3], W2[3:]                                                 # and the matching half of the rows
part_a = matmul(matmul(X, W1_a), W2_a)                                      # computed independently on each device
part_b = matmul(matmul(X, W1_b), W2_b)
combined = [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(part_a, part_b)]      # the single all-reduce (a sum)
print("tensor-parallel result equals the single-device result:", combined == full)
