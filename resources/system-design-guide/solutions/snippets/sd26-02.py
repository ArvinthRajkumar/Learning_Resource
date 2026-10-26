import math
def estimate(users, actions_per_user, bytes_per_action, read_write_ratio, retention_years=5, peak=3):
    writes_day = users * actions_per_user
    write_qps = writes_day / 86400
    read_qps = write_qps * read_write_ratio
    storage_tb = writes_day * bytes_per_action * 365 * retention_years / 1e12
    bandwidth_mbps = (write_qps + read_qps) * bytes_per_action * 8 / 1e6
    return dict(write_qps=round(write_qps), peak_write_qps=round(write_qps * peak), read_qps=round(read_qps), peak_read_qps=round(read_qps * peak),
                storage_tb=round(storage_tb, 1), bandwidth_mbps=round(bandwidth_mbps))
print("URL shortener (100M new URLs/day? no: 100M/month):", estimate(users=3_300_000, actions_per_user=1, bytes_per_action=500, read_write_ratio=100))
print("Chat (50M users, 40 msgs each, 200 B):          ", estimate(users=50_000_000, actions_per_user=40, bytes_per_action=200, read_write_ratio=1))
print("Photo app (10M users, 2 photos, 2 MB, 20 views):", estimate(users=10_000_000, actions_per_user=2, bytes_per_action=2_000_000, read_write_ratio=20))
