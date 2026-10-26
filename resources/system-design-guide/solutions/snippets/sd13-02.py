import string
ALPHABET = string.digits + string.ascii_lowercase + string.ascii_uppercase
def b62(n):
    if n == 0: return ALPHABET[0]
    s = ""
    while n: n, r = divmod(n, 62); s = ALPHABET[r] + s
    return s
def unb62(s):
    n = 0
    for ch in s: n = n * 62 + ALPHABET.index(ch)
    return n
for n in (0, 61, 62, 123456789, 3521614606207):
    print(n, b62(n), unb62(b62(n)) == n)
