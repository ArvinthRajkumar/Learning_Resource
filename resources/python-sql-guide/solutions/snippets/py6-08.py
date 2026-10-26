import hashlib, base64, struct, zlib, uuid, binascii
msg = "hello".encode("utf8")
print("sha256:", hashlib.sha256(msg).hexdigest()[:16], "... | md5 (non-security):", hashlib.md5(msg).hexdigest()[:16], "...")
print("base64:", base64.b64encode(msg).decode(), "| decoded:", base64.b64decode("aGVsbG8=").decode(), "| hex:", msg.hex())
packed = struct.pack("<IHf", 1_000_000, 7, 2.5)
print("struct bytes:", len(packed), "| unpacked:", struct.unpack("<IHf", packed))
data = b"abc" * 1000
print("zlib: ", len(data), "->", len(zlib.compress(data)), "bytes | crc32:", zlib.crc32(b"hello"))
print("uuid5 is deterministic:", uuid.uuid5(uuid.NAMESPACE_DNS, "example.com") == uuid.uuid5(uuid.NAMESPACE_DNS, "example.com"), "| uuid4 length:", len(str(uuid.uuid4())))
text = "héllo wörld"
print("utf-8 bytes:", len(text.encode("utf8")), "for", len(text), "characters |", text.encode("ascii", errors="replace"))
