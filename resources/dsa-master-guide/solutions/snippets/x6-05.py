from itertools import combinations
# Verification is cheap, search is expensive: Subset Sum
def verify(nums, subset, target):  # O(n)
    return sum(subset) == target and all(x in nums for x in subset)
def search(nums, target):  # O(2^n)
    for r in range(len(nums) + 1):
        for c in combinations(nums, r):
            if sum(c) == target: return c
nums = [3, 34, 4, 12, 5, 2]
sol = search(nums, 9)
print("certificate:", sol, "| verified in linear time:", verify(nums, sol, 9))
