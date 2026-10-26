def numbers():
    for n in range(1, 11):
        yield n
def squares(it):
    for n in it:
        yield n * n
def evens(it):
    for n in it:
        if n % 2 == 0:
            yield n
print(sum(evens(squares(numbers()))))     # nothing is stored in a list
