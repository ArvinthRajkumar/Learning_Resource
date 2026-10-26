def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return sum(int(d) ** power for d in digits) == n
