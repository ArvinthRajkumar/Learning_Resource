dau = 100_000_000
reads_per_user, writes_per_user = 50, 0.2
sec = 86_400
read_qps = dau * reads_per_user / sec
write_qps = dau * writes_per_user / sec
print(round(read_qps), round(write_qps))
print("peak (x3):", round(read_qps * 3), round(write_qps * 3))
print("read:write =", round(read_qps / write_qps))
