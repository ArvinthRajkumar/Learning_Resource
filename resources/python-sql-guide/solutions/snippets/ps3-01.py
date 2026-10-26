a = [1, 2]
b = a             # two labels on one list
b.append(3)
print("a is", a, "because both names point at the same list")
a = [9]           # moves the label a, leaving b alone
print("after rebinding a:", a, "| b is still", b)
