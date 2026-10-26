import json
data = {"name": "Ada", "langs": ["py", "sql"], "active": True, "score": None}
text = json.dumps(data, indent=2, sort_keys=True)
print(text)
print(json.loads(text)["langs"])
