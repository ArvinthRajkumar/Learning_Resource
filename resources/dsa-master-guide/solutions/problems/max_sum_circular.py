def max_sum_circular(nums):
    cur_max = cur_min = 0
    best_max, best_min = nums[0], nums[0]
    for x in nums:
        cur_max = max(x, cur_max + x)
        best_max = max(best_max, cur_max)
        cur_min = min(x, cur_min + x)
        best_min = min(best_min, cur_min)
    total = sum(nums)
    return best_max if best_max < 0 else max(best_max, total - best_min)
