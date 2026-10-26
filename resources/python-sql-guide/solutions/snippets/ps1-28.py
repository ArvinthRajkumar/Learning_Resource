def f():
    try:
        return "try"
    finally:
        print("finally runs")
print(f())
