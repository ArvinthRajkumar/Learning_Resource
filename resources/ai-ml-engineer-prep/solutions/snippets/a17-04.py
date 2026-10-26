peak_flops, bandwidth = 312e12, 2.0e12                       # A100-class: 312 TFLOP/s bf16, 2 TB/s HBM
print(f"ridge point: {peak_flops / bandwidth:.0f} FLOPs per byte (below this an operation is memory bound)")
def matmul_intensity(m, k, n, bytes_per=2):
    flops = 2 * m * k * n; moved = bytes_per * (m * k + k * n + m * n); return flops / moved
for name, (m, k, n) in [("training matmul, batch 4096 tokens", (4096, 4096, 4096)), ("decoding, 1 token at a time", (1, 4096, 4096)), ("decoding, batch of 64 tokens", (64, 4096, 4096))]:
    I = matmul_intensity(m, k, n); perf = min(peak_flops, bandwidth * I)
    print(f"{name:>36}: intensity {I:7.1f} FLOP/byte -> {perf / 1e12:6.1f} TFLOP/s ({'compute' if I >= peak_flops / bandwidth else 'memory'} bound)")
