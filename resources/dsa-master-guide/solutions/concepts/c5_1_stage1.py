def search(nums, target):
    for i, x in enumerate(nums):
        if x == target:
            return i
    return -1
