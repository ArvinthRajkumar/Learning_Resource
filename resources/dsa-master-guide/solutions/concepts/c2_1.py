def ops_linear(n):
    ops = 0
    for i in range(n):          # n iterations
        ops += 1
    return ops

def ops_quadratic(n):
    ops = 0
    for i in range(n):          # n x n iterations
        for j in range(n):
            ops += 1
    return ops

def ops_log(n):
    ops = 0
    while n > 1:                # halves each time
        n //= 2
        ops += 1
    return ops
