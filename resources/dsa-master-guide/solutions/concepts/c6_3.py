def counting_sort(nums):
    if not nums:
        return nums
    counts = [0] * (max(nums) + 1)
    for x in nums:
        counts[x] += 1                 # tally
    out = []
    for value, c in enumerate(counts):
        out.extend([value] * c)        # rebuild in order
    return out

def heap_sort(nums):
    n = len(nums)
    def sift_down(i, size):
        while True:
            big, l, r = i, 2 * i + 1, 2 * i + 2
            if l < size and nums[l] > nums[big]: big = l
            if r < size and nums[r] > nums[big]: big = r
            if big == i:
                return
            nums[i], nums[big] = nums[big], nums[i]
            i = big
    for i in range(n // 2 - 1, -1, -1):    # build max-heap
        sift_down(i, n)
    for end in range(n - 1, 0, -1):        # move max to the end
        nums[0], nums[end] = nums[end], nums[0]
        sift_down(0, end)
    return nums
