def bubble_swaps(nums):
    nums = nums[:]
    swaps = 0
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swaps += 1
                swapped = True
        if not swapped:        # already sorted - stop early
            break
    return swaps
