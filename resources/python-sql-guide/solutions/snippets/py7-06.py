import json, threading, urllib.request, urllib.error
from http.server import BaseHTTPRequestHandler, HTTPServer
ITEMS = {"1": {"id": 1, "name": "pen"}}
class Handler(BaseHTTPRequestHandler):
    def _send(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json"); self.send_header("Content-Length", str(len(body))); self.end_headers()
        self.wfile.write(body)
    def do_GET(self):
        key = self.path.rsplit("/", 1)[-1]
        if self.path.startswith("/items/") and key in ITEMS: self._send(200, ITEMS[key])
        else: self._send(404, {"error": "not found"})
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        try:
            obj = json.loads(self.rfile.read(length))
            ITEMS[str(len(ITEMS) + 1)] = {"id": len(ITEMS) + 1, **obj}
            self._send(201, ITEMS[str(len(ITEMS))])
        except (json.JSONDecodeError, TypeError):
            self._send(400, {"error": "invalid JSON"})
    def log_message(self, *a): pass
server = HTTPServer(("127.0.0.1", 0), Handler)
port = server.server_address[1]
threading.Thread(target=server.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{port}"
def call(method, path, body=None):
    req = urllib.request.Request(base + path, method=method, data=json.dumps(body).encode() if body is not None else None, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=3) as r: return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e: return e.code, json.loads(e.read())
print(call("GET", "/items/1"))
print(call("GET", "/items/99"))
print(call("POST", "/items", {"name": "book"}))
print(call("GET", "/items/2"))
server.shutdown()
