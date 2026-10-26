from collections import deque

def sliding_window_max(nums, k):
    dq, res = deque(), []              # dq holds indices, values decreasing
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:             # front slid out of the window
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
