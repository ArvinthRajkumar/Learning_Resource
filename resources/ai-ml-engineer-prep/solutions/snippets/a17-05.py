def ring_allreduce_seconds(bytes_total, gpus, link_gbps):
    per_gpu = 2 * bytes_total * (gpus - 1) / gpus
    return per_gpu / (link_gbps * 1e9)
grads = 7e9 * 2                                                                   # bf16 gradients of a 7B model: 14 GB
for name, bw in [("PCIe (32 GB/s)", 32), ("InfiniBand node link (50 GB/s)", 50), ("NVLink (450 GB/s)", 450)]:
    print(f"all-reduce of 14 GB over 8 GPUs on {name:>30}: {ring_allreduce_seconds(grads, 8, bw) * 1000:7.0f} ms")
step_compute = 6 * 7e9 * 4096 * 8 / (8 * 312e12 * 0.4)                           # one step with a global batch of 8 sequences of 4096 tokens
print(f"compute per step on 8 GPUs at 40% MFU: {step_compute * 1000:.0f} ms -> communication must overlap with backward compute or it dominates")
