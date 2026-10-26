import sqlite3
from dataclasses import dataclass
from datetime import date
from decimal import Decimal

@dataclass(frozen=True)
class Expense:
    id: int | None
    day: str
    category: str
    cents: int
    note: str = ""

class ExpenseRepo:
    def __init__(self, db):
        self.db = db
        db.execute("""CREATE TABLE IF NOT EXISTS expense (
            id INTEGER PRIMARY KEY, day TEXT NOT NULL, category TEXT NOT NULL, cents INTEGER NOT NULL CHECK (cents > 0), note TEXT NOT NULL DEFAULT '')""")
        db.execute("CREATE INDEX IF NOT EXISTS idx_expense_day ON expense(day)")
    def add(self, e):
        cur = self.db.execute("INSERT INTO expense(day, category, cents, note) VALUES (?,?,?,?)", (e.day, e.category, e.cents, e.note))
        return cur.lastrowid
    def between(self, start, end):
        rows = self.db.execute("SELECT id, day, category, cents, note FROM expense WHERE day >= ? AND day < ? ORDER BY day, id", (start, end))
        return [Expense(*r) for r in rows]
    def totals_by_category(self, start, end):
        return self.db.execute("SELECT category, SUM(cents), COUNT(*) FROM expense WHERE day >= ? AND day < ? GROUP BY category ORDER BY SUM(cents) DESC", (start, end)).fetchall()

class ExpenseService:
    CATEGORIES = {"food", "transport", "rent", "fun"}
    def __init__(self, repo): self.repo = repo
    def record(self, day, category, amount, note=""):
        date.fromisoformat(day)                                             # raises ValueError on bad dates
        if category not in self.CATEGORIES: raise ValueError(f"unknown category {category!r}")
        cents = int((Decimal(str(amount)) * 100).to_integral_value())       # exact money handling
        return self.repo.add(Expense(None, day, category, cents, note))
    def month_report(self, year, month):
        start = f"{year:04d}-{month:02d}-01"
        end = f"{year + (month == 12):04d}-{month % 12 + 1:02d}-01"
        rows = self.repo.totals_by_category(start, end)
        total = sum(r[1] for r in rows)
        lines = [f"{c:<10} {cents / 100:>8.2f}  {100 * cents / total:5.1f}%  ({n} items)" for c, cents, n in rows]
        return "\n".join(lines + [f"{'TOTAL':<10} {total / 100:>8.2f}"])

db = sqlite3.connect(":memory:", isolation_level=None)
svc = ExpenseService(ExpenseRepo(db))
for d, c, a, n in [("2024-03-02", "food", 12.50, "lunch"), ("2024-03-05", "transport", 40, "pass"), ("2024-03-09", "food", 8.25, "coffee"),
                   ("2024-03-15", "rent", 900, ""), ("2024-03-20", "fun", 30.10, "cinema"), ("2024-04-01", "food", 5, "outside the month")]:
    svc.record(d, c, a, n)
print(svc.month_report(2024, 3))
for bad in [("2024-13-01", "food", 5), ("2024-03-01", "gold", 5), ("2024-03-01", "food", -5)]:
    try: svc.record(*bad)
    except (ValueError, sqlite3.IntegrityError) as e: print("rejected", bad[:2], "->", type(e).__name__)
