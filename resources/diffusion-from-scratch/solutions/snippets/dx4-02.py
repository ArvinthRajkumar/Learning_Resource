# A rank-1 update changes the output only along one direction: W' = W + b a^T
W = [[1.0, 0.0], [0.0, 1.0]]
b = [0.5, -0.5]        # d_out x 1
a = [1.0, 2.0]         # 1 x d_in
Wp = [[W[i][j] + b[i] * a[j] for j in range(2)] for i in range(2)]
x = [3.0, 1.0]
print("base output   :", [sum(W[i][j] * x[j] for j in range(2)) for i in range(2)])
print("with LoRA     :", [sum(Wp[i][j] * x[j] for j in range(2)) for i in range(2)])
print("delta  = b (a.x):", [bi * sum(aj * xj for aj, xj in zip(a, x)) for bi in b])
