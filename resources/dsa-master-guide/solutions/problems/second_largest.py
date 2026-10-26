def second_largest(nums):
    first = second = float("-inf")
    for x in nums:
        if x > first:
            second = first     # old champion becomes runner-up
            first = x
        elif first > x > second:
            second = x
    return -1 if second == float("-inf") else second
