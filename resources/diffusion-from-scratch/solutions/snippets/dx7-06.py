params = 2e9                  # a 2-billion-parameter denoiser
tokens_per_image = 1024       # latent patches
images = 1e9                  # images seen during training (e.g. many epochs over a dataset)
flops = 6 * params * tokens_per_image * images
a100 = 312e12 * 0.4           # about 40 percent utilisation of an A100 in bf16
gpu_seconds = flops / a100
print("total FLOPs: %.2e" % flops)
print("A100 GPU-days: %.0f" % (gpu_seconds / 86400))
print("on 512 GPUs: %.1f days" % (gpu_seconds / 86400 / 512))
