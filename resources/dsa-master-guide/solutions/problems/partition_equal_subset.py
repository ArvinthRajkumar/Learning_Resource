def partition_equal_subset(nums):
    total = sum(nums)
    if total % 2:
        return False
    half = total // 2
    reach = [True] + [False] * half
    for x in nums:
        for s in range(half, x - 1, -1):      # backwards: each number used once
            if reach[s - x]:
                reach[s] = True
    return reach[half]
