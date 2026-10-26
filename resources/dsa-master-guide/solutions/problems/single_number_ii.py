def single_number_ii(nums):
    result = 0
    for bit in range(32):
        count = sum((x >> bit) & 1 for x in nums)
        if count % 3:
            result |= 1 << bit
    return result - (1 << 32) if result >= 1 << 31 else result
