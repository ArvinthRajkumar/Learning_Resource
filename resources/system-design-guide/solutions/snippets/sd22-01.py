import hashlib, hmac, os, time
def hash_password(pw, iterations=200_000):
    salt = os.urandom(16)
    return salt, iterations, hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, iterations)
def verify(pw, salt, iterations, digest):
    cand = hashlib.pbkdf2_hmac("sha256", pw.encode(), salt, iterations)
    return hmac.compare_digest(cand, digest)               # constant-time comparison
salt, it, dg = hash_password("correct horse battery staple")
print("right password:", verify("correct horse battery staple", salt, it, dg), "| wrong password:", verify("hunter2", salt, it, dg))
t = time.perf_counter(); hashlib.sha256(b"x").digest(); fast = time.perf_counter() - t
t = time.perf_counter(); hashlib.pbkdf2_hmac("sha256", b"x", salt, it); slow = time.perf_counter() - t
print("PBKDF2 (200k rounds) is slower than a single SHA-256:", slow > 100 * fast)
