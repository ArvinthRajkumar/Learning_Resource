def insert(root, word):
    node = root
    for ch in word:
        node = node.setdefault(ch, {})
    node["$"] = True
