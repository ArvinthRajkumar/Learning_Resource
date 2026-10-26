def memory_gb(params, bytes_per_param=16): return params * bytes_per_param / 1e9
for name, p in [("1B", 1e9), ("7B", 7e9), ("13B", 13e9), ("70B", 70e9)]:
    print(f"{name:>4} parameters: training states {memory_gb(p):>7.0f} GB | bf16 weights alone {memory_gb(p, 2):>6.0f} GB | 4-bit inference weights {memory_gb(p, 0.5):>6.1f} GB")
def activation_gb(layers, hidden, seq, batch, bytes_per=2, factor=34):
    return layers * seq * batch * hidden * factor * bytes_per / 1e9 / 2           # rough: about 34 x s x b x h bytes (fp16) per layer without checkpointing
print("activations for a 32-layer, 4096-wide model, seq 4096, micro-batch 1:", round(activation_gb(32, 4096, 4096, 1), 1), "GB without activation checkpointing")
