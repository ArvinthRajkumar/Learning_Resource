layers, head_dim, bytes_ = 32, 128, 2
for name, kv_heads in (("MHA (32 kv heads)", 32), ("GQA (8 kv heads)", 8), ("MQA (1 kv head)", 1)):
    per_token = 2 * layers * kv_heads * head_dim * bytes_
    print("%-18s %7.0f KiB per token, %5.1f GiB for 32k tokens x 8 sequences" % (name, per_token / 1024, per_token * 32768 * 8 / 2 ** 30))
