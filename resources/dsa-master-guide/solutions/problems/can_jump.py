def can_jump(nums):
    farthest = 0
    for i, x in enumerate(nums):
        if i > farthest:
            return False          # unreachable position
        farthest = max(farthest, i + x)
    return True
