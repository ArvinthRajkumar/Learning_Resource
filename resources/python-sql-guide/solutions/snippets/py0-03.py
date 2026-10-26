for value in (42, 3.14, "text", True, None, [1, 2], (1, 2), {"a": 1}, {1, 2}):
    print(repr(value), "->", type(value).__name__)
