import hashlib
def blocks(data, size=4):
    return [data[i:i + size] for i in range(0, len(data), size)]
def hashes(data):
    return [hashlib.sha1(b).hexdigest()[:6] for b in blocks(data)]
v1 = b"AAAABBBBCCCCDDDD"
v2 = b"AAAABBBBXXXXDDDD"          # only the third block changed
h1, h2 = hashes(v1), hashes(v2)
print(h1)
print(h2)
print("blocks to upload:", [i for i, (a, b) in enumerate(zip(h1, h2)) if a != b])
