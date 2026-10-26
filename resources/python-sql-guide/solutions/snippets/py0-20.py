def safe_div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "cannot divide by zero"
    except TypeError as e:
        return "bad types: %s" % e
    else:
        return result            # only when no exception
    finally:
        print("done")            # always runs

print(safe_div(6, 3))
print(safe_div(1, 0))
print(safe_div(1, "a"))
