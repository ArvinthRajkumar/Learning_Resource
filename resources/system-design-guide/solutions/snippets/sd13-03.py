def sliding_window_estimate(prev_count, curr_count, elapsed_fraction):
    return curr_count + prev_count * (1 - elapsed_fraction)
# limit 100/min; previous minute had 80 requests, this minute 30 so far, 25% through
print(sliding_window_estimate(80, 30, 0.25))   # 90.0, still under 100
