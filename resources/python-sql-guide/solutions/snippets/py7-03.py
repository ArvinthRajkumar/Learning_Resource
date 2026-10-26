def validate_user(obj):
    errors = []
    if not isinstance(obj, dict): return ["body must be an object"]
    if not isinstance(obj.get("name"), str) or not obj["name"].strip(): errors.append("name: non-empty string required")
    age = obj.get("age")
    if not isinstance(age, int) or isinstance(age, bool) or not 0 <= age <= 150: errors.append("age: integer 0..150 required")
    email = obj.get("email", "")
    if "@" not in email or email.startswith("@") or email.endswith("@"): errors.append("email: invalid")
    extra = set(obj) - {"name", "age", "email"}
    if extra: errors.append(f"unknown fields: {sorted(extra)}")
    return errors
print(validate_user({"name": "Ada", "age": 36, "email": "ada@example.com"}))
print(validate_user({"name": " ", "age": True, "email": "nope", "admin": True}))
