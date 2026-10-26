def describe(cmd):
    match cmd.split():
        case ["go", direction]:
            return "going " + direction
        case ["quit"]:
            return "bye"
        case _:
            return "unknown"
print(describe("go north"), describe("quit"), describe("jump"))
