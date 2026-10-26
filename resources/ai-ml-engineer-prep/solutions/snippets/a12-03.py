import json
schema = {"name": str, "age": int, "tags": list}
def validate(obj):
    errs = []
    for k, t in schema.items():
        if k not in obj: errs.append("missing " + k)
        elif not isinstance(obj[k], t): errs.append("%s should be %s" % (k, t.__name__))
    return errs
for raw in ('{"name": "Ada", "age": 36, "tags": ["x"]}', '{"name": "Ada", "age": "36"}', '{bad json'):
    try:
        print(validate(json.loads(raw)) or "valid")
    except json.JSONDecodeError:
        print("invalid JSON: retry with the error message")
