def jump_game_ii(nums):
    jumps = cur_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:             # must jump now
            jumps += 1
            cur_end = farthest
    return jumps
