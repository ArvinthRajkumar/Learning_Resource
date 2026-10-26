def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0                 # 9 + 1 -> 0 carry 1
    return [1] + digits               # all nines
