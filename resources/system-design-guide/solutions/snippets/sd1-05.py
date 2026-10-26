new_per_month = 100_000_000
write_qps = new_per_month / (30 * 86_400)
read_qps = write_qps * 100
records_10y = new_per_month * 12 * 10
storage_tb = records_10y * 500 / 1e12
reads_per_day = read_qps * 86_400
cache_gb = reads_per_day * 0.2 * 500 / 1e9
print(round(write_qps), round(read_qps))
print(records_10y, round(storage_tb, 1), "TB")
print(round(reads_per_day / 1e6), "M reads/day;", round(cache_gb), "GB cache")
