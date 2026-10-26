import json, csv, io
class JsonReader:
    def read(self, text): return json.loads(text)
class CsvReader:
    def read(self, text): return list(csv.DictReader(io.StringIO(text)))
READERS = {"json": JsonReader, "csv": CsvReader}
def make_reader(kind):
    try: return READERS[kind]()
    except KeyError: raise ValueError(f"unknown format {kind!r}; choose from {sorted(READERS)}") from None
print(make_reader("json").read('[{"a": 1}]'), make_reader("csv").read("a,b\n1,2"))
try: make_reader("xml")
except ValueError as e: print(e)
