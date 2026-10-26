# Vanishing gradients: the sigmoid's derivative is at most 0.25, so gradients shrink geometrically with depth.
for depth in (2, 5, 10, 20):
    print("depth %2d: gradient factor at most %.2e" % (depth, 0.25 ** depth))
