hours_per_day = 1_000_000_000
mbps = 3
bytes_per_hour = mbps * 1e6 / 8 * 3600
total_pb = hours_per_day * bytes_per_hour / 1e15
print(round(bytes_per_hour / 1e9, 2), "GB per hour watched;", round(total_pb), "PB per day egress")
print(round(total_pb * 8 / 86_400 * 1000), "Tbps average")
