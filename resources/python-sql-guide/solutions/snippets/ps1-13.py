import re
def normalise(raw, default_country="1"):
    digits = re.sub(r"\D", "", raw)
    if len(digits) == 10:
        digits = default_country + digits
    if not re.fullmatch(r"\d{11,15}", digits):
        raise ValueError(f"invalid phone: {raw!r}")
    return "+" + digits
for p in ["(555) 123-4567", "+44 20 7946 0958", "12-34"]:
    try:
        print(normalise(p))
    except ValueError as e:
        print(e)
