import math
batch, batch_ms, peak_qps, headroom = 32, 40, 20000, 1.3
per_gpu = batch / (batch_ms / 1000)
print(f"per GPU: {per_gpu:.0f} req/s | GPUs for peak: {math.ceil(peak_qps / per_gpu)} | with 30% headroom: {math.ceil(peak_qps * headroom / per_gpu)}")
