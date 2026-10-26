def simple_hash(key, size=7):
    total = 0
    for ch in key:
        total += ord(ch)        # add up character codes
    return total % size         # bucket index
