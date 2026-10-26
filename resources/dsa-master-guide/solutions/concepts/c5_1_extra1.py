def binary_search_rec(nums, target, lo, hi):
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if nums[mid] == target:
        return mid
    if nums[mid] < target:
        return binary_search_rec(nums, target, mid + 1, hi)
    return binary_search_rec(nums, target, lo, mid - 1)

from bisect import bisect_left, bisect_right
a = [1, 2, 2, 2, 5]
print(bisect_left(a, 2), bisect_right(a, 2))   # 1 4  -> first index, one past last index
