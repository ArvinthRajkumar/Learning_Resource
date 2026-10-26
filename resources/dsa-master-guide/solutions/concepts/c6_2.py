def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left, right = merge_sort(nums[:mid]), merge_sort(nums[mid:])
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:           # <= keeps the sort stable
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    return merged + left[i:] + right[j:]

def quick_sort(nums, lo=0, hi=None):
    if hi is None:
        hi = len(nums) - 1
    if lo < hi:
        pivot, i = nums[hi], lo - 1
        for j in range(lo, hi):
            if nums[j] <= pivot:          # belongs on the left side
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[hi] = nums[hi], nums[i + 1]
        quick_sort(nums, lo, i)           # left of pivot
        quick_sort(nums, i + 2, hi)       # right of pivot
    return nums
