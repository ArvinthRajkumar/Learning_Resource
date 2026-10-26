"""Parameter count of a Llama-style decoder (no biases, RMSNorm, SwiGLU MLP)."""


def llama_params(vocab: int, d: int, layers: int, ffn: int, n_heads: int, n_kv_heads: int,
                 tied_embeddings: bool = False) -> int:
    """Count every weight:

    per layer:
      attention  q: d x d, o: d x d, k and v: d x (n_kv_heads x head_dim) each
      MLP (SwiGLU) gate, up: d x ffn, down: ffn x d  -> 3 x d x ffn
      2 RMSNorm weight vectors of size d
    plus the token embedding (vocab x d), the LM head (vocab x d unless tied)
    and the final norm (d).
    Rule of thumb for MHA with ffn = 4d: about 12 x layers x d^2 + embeddings.
    """
    head_dim = d // n_heads
    kv_dim = n_kv_heads * head_dim
    attn = 2 * d * d + 2 * d * kv_dim
    mlp = 3 * d * ffn
    per_layer = attn + mlp + 2 * d
    embed = vocab * d * (1 if tied_embeddings else 2)
    return layers * per_layer + embed + d
