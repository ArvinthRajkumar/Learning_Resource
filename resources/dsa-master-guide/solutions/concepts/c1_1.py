def summarize(line):
    nums = list(map(int, line.split()))   # "3 5 8 10" -> [3, 5, 8, 10]
    total = 0                             # sum of even numbers
    for x in nums:
        if x % 2 == 0:
            total += x
    return total, len(nums), max(nums)
