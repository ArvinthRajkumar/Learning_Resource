def insertion_sort_impl(nums):
    for i in range(1, len(nums)):
        key, j = nums[i], i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums
