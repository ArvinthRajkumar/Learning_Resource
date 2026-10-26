n = 27
steps = 0
while n != 1:
    n = n // 2 if n % 2 == 0 else 3 * n + 1
    steps += 1
print("steps:", steps)

for i in range(10):
    if i % 2 == 0:
        continue          # skip evens
    if i > 6:
        break             # stop the loop
    print(i, end=" ")
else:
    print("never printed because we broke out")
print()
