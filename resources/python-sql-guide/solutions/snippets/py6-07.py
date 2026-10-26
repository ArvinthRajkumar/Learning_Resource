import textwrap, string
name, score, ratio = "Ada", 93.456, 0.8725
print(f"{name:>8}|{name:<8}|{name:^8}|")
print(f"{score:.1f} | {score:10.2f} | {ratio:.1%} | {1234567.891:,.2f} | {255:#x} {255:08b} | {42:+d}")
width = 10
print(f"{'dynamic':>{width}} | {3.14159:.{2}f} | {name!r} | {name=}")
long = "Python's standard library gives you batteries for almost every common task, from files to dates to hashing."
print(textwrap.fill(long, width=40))
print(textwrap.shorten(long, width=40, placeholder="..."))
print(string.ascii_lowercase[:5], string.digits, "| Template:", string.Template("Hi $who, you owe $$${amt}").substitute(who="Bo", amt=5))
