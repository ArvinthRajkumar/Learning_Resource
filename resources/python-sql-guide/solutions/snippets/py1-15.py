import re
text = "Order #123 shipped on 2024-03-05; order #456 on 2024-04-11."
print(re.findall(r"#(\d+)", text))
m = re.search(r"(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})", text)
print(m.group("y"), m.group("m"), m.groupdict())
print(re.sub(r"\d{4}-\d{2}-\d{2}", "<date>", text))
print(re.split(r"[;,]\s*", "a; b, c"))
pat = re.compile(r"^[\w.+-]+@[\w-]+\.[\w.]+$")
print(bool(pat.match("ada@example.com")), bool(pat.match("not an email")))
