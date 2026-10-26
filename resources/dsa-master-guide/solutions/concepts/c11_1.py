def fib(n):
    if n < 2:                     # base cases: fib(0)=0, fib(1)=1
        return n
    return fib(n - 1) + fib(n - 2)

def sum_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)
