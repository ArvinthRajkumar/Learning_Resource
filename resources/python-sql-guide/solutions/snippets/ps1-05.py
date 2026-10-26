from itertools import groupby
def rle(s):
    return "".join(f"{len(list(g))}{ch}" for ch, g in groupby(s))
def unrle(s):
    import re
    return "".join(ch * int(n) for n, ch in re.findall(r"(\d+)(\D)", s))
enc = rle("aaabccdddd")
print(enc, unrle(enc) == "aaabccdddd")
