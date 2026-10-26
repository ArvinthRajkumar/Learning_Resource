nums = [5, 3, 8]
nums.append(1)            # add at the end
nums.insert(1, 99)        # insert at position
nums.extend([7, 7])
print(nums)
print(nums.pop(), nums.pop(0), nums)
nums.remove(99)           # remove first matching value
print(nums, len(nums), 8 in nums, nums.index(8), nums.count(7))
nums.sort(); print(nums)
nums.reverse(); print(nums)
print(nums[1:3], nums[::-1], nums[-1])
