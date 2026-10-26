funcs = [lambda: i for i in range(3)]
print("late binding closure bug:", [f() for f in funcs])
funcs = [lambda i=i: i for i in range(3)]
print("fixed with a default argument:", [f() for f in funcs])
xs = [2, 4, 6, 8, 9]
for x in xs:
    if x % 2 == 0: xs.remove(x)
print("removing every even number while iterating leaves some behind:", xs)
print("correct:", [x for x in [2, 4, 6, 8, 9] if x % 2 != 0])
