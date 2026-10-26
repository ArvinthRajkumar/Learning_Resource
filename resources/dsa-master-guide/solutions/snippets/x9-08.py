import random
random.seed(8)
def reservoir(stream, k):
    res = []
    for i, x in enumerate(stream):
        if i < k: res.append(x)
        else:
            j = random.randint(0, i)                                  # keep x with probability k / (i + 1)
            if j < k: res[j] = x
    return res
counts = {x: 0 for x in range(10)}
for _ in range(20000):
    for x in reservoir(range(10), 3): counts[x] += 1
print("reservoir sampling selects each of 10 items about 6000 times (3/10 of 20000):", sorted(counts.values())[0] > 5700 and sorted(counts.values())[-1] < 6300)
def freivalds(A, B, C, rounds=10):
    n = len(A)
    for _ in range(rounds):
        r = [random.randint(0, 1) for _ in range(n)]
        Br = [sum(B[i][j] * r[j] for j in range(n)) for i in range(n)]
        ABr = [sum(A[i][j] * Br[j] for j in range(n)) for i in range(n)]
        Cr = [sum(C[i][j] * r[j] for j in range(n)) for i in range(n)]
        if ABr != Cr: return False
    return True
A = [[1, 2], [3, 4]]; B = [[0, 1], [1, 0]]; C_good = [[2, 1], [4, 3]]; C_bad = [[2, 1], [4, 4]]
print("Freivalds accepts the correct product:", freivalds(A, B, C_good), "| rejects a wrong one:", not freivalds(A, B, C_bad))
inside = sum(random.random() ** 2 + random.random() ** 2 <= 1 for _ in range(200_000))
print("Monte Carlo estimate of pi:", round(4 * inside / 200_000, 2))
