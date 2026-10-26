def descend(lr, steps=20):
    x = 5.0                                                    # minimise f(x) = x^2 whose gradient is 2x
    for _ in range(steps): x -= lr * 2 * x
    return x
for lr in (0.01, 0.1, 0.5, 1.1):
    print(f"learning rate {lr:>4}: after 20 steps x = {descend(lr):12.4f}", "(diverged)" if abs(descend(lr)) > 5 else "")
