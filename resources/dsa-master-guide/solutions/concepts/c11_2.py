def gen_subsets(nums, start, path, res):
    res.append(path[:])                     # every path is a subset
    for i in range(start, len(nums)):
        path.append(nums[i])                # choose
        gen_subsets(nums, i + 1, path, res) # explore
        path.pop()                          # un-choose

def subsets(nums):
    res = []
    gen_subsets(nums, 0, [], res)
    return res
