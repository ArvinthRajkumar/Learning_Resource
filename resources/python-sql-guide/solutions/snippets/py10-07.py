import re
from statistics import median
raw = [{"id": "1", "price": "$1,200.50", "country": " India", "joined": "03/01/2024"},
       {"id": "2", "price": "n/a",       "country": "IN",     "joined": "2024-03-02"},
       {"id": "2", "price": "90",        "country": "india ", "joined": "2024-03-02"},
       {"id": "3", "price": "-5",        "country": "US",     "joined": "2024-03-04"}]
COUNTRY = {"india": "IN", "in": "IN", "us": "US"}
def parse_price(s):
    cleaned = re.sub(r"[^0-9.\-]", "", s)
    return float(cleaned) if cleaned not in ("", "-", ".") else None
def parse_date(s):
    m = re.fullmatch(r"(\d{2})/(\d{2})/(\d{4})", s)
    return f"{m[3]}-{m[1]}-{m[2]}" if m else s                                # assume MM/DD/YYYY here, a documented decision
clean = []
for r in raw:
    price = parse_price(r["price"])
    clean.append({"id": int(r["id"]), "price": price if price is not None and price >= 0 else None,
                  "country": COUNTRY[r["country"].strip().lower()], "joined": parse_date(r["joined"])})
seen, deduped = set(), []
for r in clean:                                                                # keep the first row per id
    if r["id"] not in seen: seen.add(r["id"]); deduped.append(r)
fill = median(r["price"] for r in deduped if r["price"] is not None)
for r in deduped: r["price_filled"] = r["price"] if r["price"] is not None else fill
for r in deduped: print(r)
