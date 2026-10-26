def has_duplicate_slow(nums):
    for i in range(len(nums)):              # n times
        for j in range(i + 1, len(nums)):   # up to n times
            if nums[i] == nums[j]:
                return True
    return False                            # O(n^2) time, O(1) space

def has_duplicate_fast(nums):
    seen = set()
    for x in nums:                          # n times
        if x in seen:                       # O(1) average
            return True
        seen.add(x)
    return False                            # O(n) time, O(n) space
