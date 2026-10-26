def find_duplicate_number(nums):
    slow = fast = nums[0]
    while True:                        # phase 1: meet inside the cycle
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]                     # phase 2: find the cycle start
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
