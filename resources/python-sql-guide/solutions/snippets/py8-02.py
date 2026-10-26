a = int("256"); b = int("256")
c = int("100000"); d = int("100000")
print("256 shared:", a is b, "| 100000 shared:", c is d, "| values equal either way:", a == b, c == d)
s1 = "hello world"; s2 = "".join(["hello", " ", "world"])
print("equal strings, different objects:", s1 == s2, s1 is s2)
import sys
print("interned explicitly:", sys.intern(s1) is sys.intern(s2))
