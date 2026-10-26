people = [("ana", 30), ("bo", 25), ("cy", 30), ("di", 25)]
print("by age desc then name:", sorted(people, key=lambda p: (-p[1], p[0])))
words = ["10", "9", "100"]
print("numeric versus lexicographic:", sorted(words), sorted(words, key=int))
import functools
def cmp(a, b): return -1 if a + b > b + a else 1                          # largest number from digits
print("largest number:", "".join(sorted(["3", "30", "34", "5", "9"], key=functools.cmp_to_key(cmp))))
print("stable sort keeps the original order of equal keys:", sorted([("b", 1), ("a", 1), ("c", 0)], key=lambda t: t[1]))
