import json
doc = '{"user": {"id": 7, "tags": ["a", "b"]}, "score": 9.5, "active": true, "note": null}'
data = json.loads(doc)
print(data["user"]["tags"], data["active"], data["note"], type(data["score"]).__name__)
print(json.dumps(data, sort_keys=True, separators=(",", ":")))
print(json.dumps({"name": "café", "n": 1}, ensure_ascii=False), "|", json.dumps({"name": "café"}))
try:
    json.loads("{'bad': 'quotes'}")
except json.JSONDecodeError as e:
    print("invalid JSON:", e.msg, "at column", e.colno)
try:
    json.dumps({"when": __import__("datetime").date(2024, 1, 1)})
except TypeError as e:
    print("not serialisable:", e)
