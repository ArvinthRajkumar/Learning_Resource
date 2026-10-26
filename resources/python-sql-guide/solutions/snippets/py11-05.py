import traceback
def parse_age(record): return int(record["age"])
def average_age(records): return sum(parse_age(r) for r in records) / len(records)
try:
    average_age([{"age": "30"}, {"age": "x"}, {"age": "40"}])
except Exception as e:
    frames = [f.name for f in traceback.extract_tb(e.__traceback__)]
    print("call chain:", " -> ".join(frames))
    print(f"{type(e).__name__}: {e}")
