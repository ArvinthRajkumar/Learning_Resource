x = "global"
def outer():
    x = "enclosing"
    def inner():
        nonlocal x
        x = "changed by inner"
    inner()
    return x
print(outer(), x)
