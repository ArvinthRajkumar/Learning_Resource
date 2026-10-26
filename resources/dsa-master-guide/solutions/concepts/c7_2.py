def pair_exists(nums, target):
    seen = set()
    for x in nums:
        if target - x in seen:     # partner already seen
            return True
        seen.add(x)
    return False
