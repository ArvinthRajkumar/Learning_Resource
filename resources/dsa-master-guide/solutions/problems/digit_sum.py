def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10   # last digit
        n //= 10          # drop the last digit
    return total
