nums = [5, 2, 8]
nums.append(1)         # O(1)   [5, 2, 8, 1]
nums.pop()             # O(1)   removes last
nums.pop(0)            # O(n)   removes first, shifts the rest
nums.insert(1, 9)      # O(n)
nums.remove(9)         # O(n)   removes first occurrence
x = 8 in nums          # O(n)
nums.sort()            # O(n log n), in place
rev = nums[::-1]       # O(n), new list
total = sum(nums); mx = max(nums); mn = min(nums)   # each O(n)
