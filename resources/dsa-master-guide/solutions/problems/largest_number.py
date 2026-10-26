from functools import cmp_to_key

def largest_number(nums):
    strs = [str(x) for x in nums]
    strs.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
    result = "".join(strs)
    return "0" if result[0] == "0" else result   # all zeros
