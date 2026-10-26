def factorial(n):
    if n <= 1:                 # base case: stop
        return 1
    return n * factorial(n - 1)   # recursive case: smaller problem
