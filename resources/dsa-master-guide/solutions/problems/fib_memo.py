def fib_memo(n, memo={}):
    if n < 2:
        return n
    if n not in memo:
        memo[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo[n]
