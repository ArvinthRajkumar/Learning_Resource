def chunk(text, size, overlap):
    words = text.split()
    step = size - overlap
    return [" ".join(words[i:i + size]) for i in range(0, max(1, len(words) - overlap), step)]
doc = " ".join("w%d" % i for i in range(1, 21))
for c in chunk(doc, 8, 2):
    print(c)
