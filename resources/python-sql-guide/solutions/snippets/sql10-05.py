import hashlib
current = {"C-1": {"key": 2, "hash": hashlib.md5(b"Ana|US").hexdigest()}, "C-2": {"key": 3, "hash": hashlib.md5(b"Bo|DE").hexdigest()}}
incoming = [("C-1", "Ana", "US"), ("C-2", "Bo", "FR"), ("C-3", "Cy", "IN")]          # C-1 unchanged, C-2 moved, C-3 is new
for cid, name, country in incoming:
    h = hashlib.md5(f"{name}|{country}".encode()).hexdigest()
    if cid not in current: print(cid, "-> INSERT new member")
    elif current[cid]["hash"] != h: print(cid, "-> CLOSE old version and INSERT new version (type 2)")
    else: print(cid, "-> no change")
