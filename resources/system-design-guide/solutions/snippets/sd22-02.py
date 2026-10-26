import base64, hashlib, hmac, json, time
b64 = lambda b: base64.urlsafe_b64encode(b).rstrip(b"=").decode()
unb64 = lambda s: base64.urlsafe_b64decode(s + "=" * (-len(s) % 4))
def sign(payload, key):
    head = b64(json.dumps({"alg": "HS256", "typ": "JWT"}, separators=(",", ":")).encode())
    body = b64(json.dumps(payload, separators=(",", ":")).encode())
    sig = b64(hmac.new(key, f"{head}.{body}".encode(), hashlib.sha256).digest())
    return f"{head}.{body}.{sig}"
def verify(token, key, now):
    head, body, sig = token.split(".")
    if json.loads(unb64(head))["alg"] != "HS256": return "rejected: unexpected algorithm"
    good = b64(hmac.new(key, f"{head}.{body}".encode(), hashlib.sha256).digest())
    if not hmac.compare_digest(sig, good): return "rejected: bad signature"
    claims = json.loads(unb64(body))
    return "rejected: expired" if claims["exp"] < now else claims
key = b"server-secret-key"
tok = sign({"sub": "user42", "role": "admin", "exp": 1000}, key)
print("valid     :", verify(tok, key, now=500))
print("expired   :", verify(tok, key, now=2000))
h, b, s = tok.split(".")
forged_body = b64(json.dumps({"sub": "user42", "role": "superadmin", "exp": 9999}, separators=(",", ":")).encode())
print("tampered  :", verify(f"{h}.{forged_body}.{s}", key, now=500))
