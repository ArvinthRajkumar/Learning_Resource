from dataclasses import dataclass, field, replace
@dataclass(frozen=True)
class Query:
    table: str
    columns: tuple = ("*",)
    where: tuple = ()
    limit: int | None = None
    def select(self, *cols): return replace(self, columns=cols)
    def filter(self, cond): return replace(self, where=self.where + (cond,))
    def take(self, n): return replace(self, limit=n)
    def sql(self):
        s = f"SELECT {', '.join(self.columns)} FROM {self.table}"
        if self.where: s += " WHERE " + " AND ".join(self.where)
        return s + (f" LIMIT {self.limit}" if self.limit is not None else "")
base = Query("users")
print(base.select("id", "name").filter("age > 18").filter("active = 1").take(10).sql())
print(base.sql(), "(the original is unchanged: frozen dataclass)")
