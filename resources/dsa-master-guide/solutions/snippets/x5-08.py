MOD = 10**9 + 7
def mat_mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % MOD for j in range(len(B[0]))] for i in range(len(A))]
def mat_pow(A, p):
    n = len(A)
    R = [[int(i == j) for j in range(n)] for i in range(n)]
    while p:
        if p & 1: R = mat_mul(R, A)
        A = mat_mul(A, A)
        p >>= 1
    return R
def fib(n): return mat_pow([[1, 1], [1, 0]], n)[0][1]
a, b = 0, 1
for _ in range(90): a, b = b, a + b
assert fib(90) == a % MOD
# walks of length 3 on a triangle graph
tri = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
print("fib(90) mod p =", fib(90), "| fib(10**18) mod p =", fib(10**18), "| closed walks of length 3 per vertex:", [mat_pow(tri, 3)[i][i] for i in range(3)])
