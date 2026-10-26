import tempfile, os
path = os.path.join(tempfile.mkdtemp(), "notes.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write("line one\n")
    f.writelines(["line two\n", "line three\n"])
with open(path, encoding="utf-8") as f:
    for line in f:                    # lazy, one line at a time
        print(line.rstrip())
print(open(path, encoding="utf-8").read().count("line"))
