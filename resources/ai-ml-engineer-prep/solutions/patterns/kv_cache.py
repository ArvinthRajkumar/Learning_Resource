"""KV cache and weight memory calculators."""

DTYPE_BYTES = {"fp32": 4, "fp16": 2, "bf16": 2, "fp8": 1, "int8": 1, "int4": 0.5}
GiB = 1024 ** 3
GB = 1000 ** 3


def kv_cache_bytes(layers: int, kv_heads: int, head_dim: int, seq_len: int,
                   batch: int, bytes_per_elem: float) -> float:
    """2 (K and V) x layers x kv_heads x head_dim x seq_len x batch x bytes.

    kv_heads is the number of KEY/VALUE heads: equal to the query heads for
    MHA, 1 for MQA, and a small group count for GQA (for example 8).
    """
    return 2 * layers * kv_heads * head_dim * seq_len * batch * bytes_per_elem


def kv_bytes_per_token(layers: int, kv_heads: int, head_dim: int, bytes_per_elem: float) -> float:
    return 2 * layers * kv_heads * head_dim * bytes_per_elem


def weight_bytes(params: float, dtype: str) -> float:
    """Weights only. Real int4 formats also store scales/zero-points (a few % more)."""
    return params * DTYPE_BYTES[dtype]


def max_tokens_in_cache(free_bytes: float, layers: int, kv_heads: int, head_dim: int,
                        bytes_per_elem: float) -> int:
    """How many tokens (summed over all sequences in the batch) fit in free memory."""
    return int(free_bytes // kv_bytes_per_token(layers, kv_heads, head_dim, bytes_per_elem))
