import math
# y = sigmoid(w * x + b), loss = (y - t)^2 for one example
x, t = 2.0, 1.0
w, b = 0.3, -0.1
z = w * x + b
y = 1 / (1 + math.exp(-z))
loss = (y - t) ** 2
# chain rule: dL/dw = dL/dy * dy/dz * dz/dw
dL_dy = 2 * (y - t)
dy_dz = y * (1 - y)
dz_dw = x
grad_w = dL_dy * dy_dz * dz_dw
def L(w_):
    return (1 / (1 + math.exp(-(w_ * x + b))) - t) ** 2
numeric = (L(w + 1e-6) - L(w - 1e-6)) / 2e-6
print("chain rule", round(grad_w, 6), "numeric", round(numeric, 6))
