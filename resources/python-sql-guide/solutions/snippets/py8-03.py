x = "global"
def outer():
    x = "enclosing"
    def inner():
        return x                 # found in the enclosing scope
    return inner()
def broken():
    try:
        print(x)                 # x is assigned later in this function, so it is local, and not yet bound
        x = "local"
    except UnboundLocalError as e:
        return f"UnboundLocalError: {e}"
def counter():
    n = 0
    def inc():
        nonlocal n               # rebind the enclosing variable
        n += 1
        return n
    return inc
c = counter(); c(); c()
print(outer(), "|", broken(), "| closure state:", c())
