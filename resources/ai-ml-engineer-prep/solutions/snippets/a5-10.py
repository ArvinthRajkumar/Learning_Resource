def llama_like(layers, d, heads, kv_heads, ffn_mult, vocab):
    head_dim = d // heads
    attn = d * d + 2 * d * (kv_heads * head_dim) + d * d          # Q, K, V, O
    ffn = 3 * d * int(ffn_mult * d)                               # gated MLP: up, gate, down
    per_layer = attn + ffn
    return layers * per_layer + 2 * vocab * d                      # plus embeddings and output head
p = llama_like(layers=32, d=4096, heads=32, kv_heads=8, ffn_mult=3.5, vocab=128000)
print("about %.1f B parameters" % (p / 1e9))
