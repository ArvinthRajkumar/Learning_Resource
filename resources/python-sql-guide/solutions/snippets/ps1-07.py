def deep_merge(a, b):
    out = dict(a)
    for k, v in b.items():
        if k in out and isinstance(out[k], dict) and isinstance(v, dict):
            out[k] = deep_merge(out[k], v)
        else:
            out[k] = v
    return out
print(deep_merge({"a": 1, "b": {"x": 1, "y": 2}}, {"b": {"y": 3, "z": 4}, "c": 5}))
