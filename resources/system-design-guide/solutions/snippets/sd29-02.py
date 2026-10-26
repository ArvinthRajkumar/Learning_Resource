import hashlib
class Server:
    def __init__(self): self.body, self.hits, self.bytes_sent = b"console.log('v1')" * 100, 0, 0
    def etag(self): return hashlib.md5(self.body).hexdigest()[:8]
    def get(self, if_none_match=None):
        self.hits += 1
        if if_none_match == self.etag(): return 304, b""
        self.bytes_sent += len(self.body); return 200, self.body
class BrowserCache:
    def __init__(self, server): self.server, self.etag, self.body, self.fetched_at = server, None, None, None
    def fetch(self, now, max_age=60):
        if self.body is not None and now - self.fetched_at < max_age: return "fresh cache hit (no network)"
        status, body = self.server.get(self.etag)
        if status == 304: self.fetched_at = now; return "304 revalidated (no body)"
        self.body, self.etag, self.fetched_at = body, self.server.etag(), now; return f"200 downloaded {len(body)} bytes"
srv = Server(); b = BrowserCache(srv)
for t in (0, 10, 70, 80, 140):
    print(f"t={t:>3}s:", b.fetch(t))
srv.body = b"console.log('v2')" * 100
print("t=200s after the file changed:", b.fetch(200))
print("server saw", srv.hits, "requests and sent", srv.bytes_sent, "bytes for 6 browser loads")
