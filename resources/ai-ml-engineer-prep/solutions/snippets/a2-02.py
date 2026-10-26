def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
A = [[1, 2], [3, 4]]
B = [[0, 1], [1, 0]]
print("AB =", matmul(A, B))
print("BA =", matmul(B, A))
rot = [[0, -1], [1, 0]]            # rotate by 90 degrees
print("rotate (1, 0):", [sum(rot[i][j] * [1, 0][j] for j in range(2)) for i in range(2)])
