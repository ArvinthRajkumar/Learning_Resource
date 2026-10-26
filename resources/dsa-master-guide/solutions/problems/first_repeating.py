def first_repeating(nums):
    seen = set()
    answer = -1
    for x in reversed(nums):
        if x in seen:
            answer = x            # overwritten until we reach the left-most one
        else:
            seen.add(x)
    return answer
