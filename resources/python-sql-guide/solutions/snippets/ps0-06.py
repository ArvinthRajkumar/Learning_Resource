ALLOWED_SORT = {"name": "name", "age": "age"}
def order_clause(user_col, direction):
    col = ALLOWED_SORT[user_col]                 # KeyError for anything unexpected
    d = "DESC" if direction == "desc" else "ASC"
    return f"ORDER BY {col} {d}"
print(order_clause("age", "desc"))
try:
    order_clause("age; DROP TABLE users", "asc")
except KeyError:
    print("rejected")
