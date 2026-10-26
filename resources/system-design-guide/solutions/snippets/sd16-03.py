# Concurrent edits on "cat": A inserts 'X' at 1, B inserts 'Y' at 0.
def apply(text, op):
    kind, pos, ch = op
    return text[:pos] + ch + text[pos:] if kind == "ins" else text[:pos] + text[pos + 1:]

def transform(op, other):
    """Adjust op so it can be applied after 'other' has already been applied."""
    kind, pos, ch = op
    okind, opos, _ = other
    if okind == "ins" and opos <= pos:
        pos += 1
    elif okind == "del" and opos < pos:
        pos -= 1
    return (kind, pos, ch)

a = ("ins", 1, "X")
b = ("ins", 0, "Y")
# naive: apply in different orders without transform -> diverge
print("naive A then B:", apply(apply("cat", a), b), "| B then A:", apply(apply("cat", b), a))
# with transform both converge
print("OT   A then B':", apply(apply("cat", a), transform(b, a)), "| B then A':", apply(apply("cat", b), transform(a, b)))
