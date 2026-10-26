import os, tomllib
os.environ["APP_DEBUG"] = "1"
debug = os.environ.get("APP_DEBUG", "0") == "1"
cfg = tomllib.loads("""
[database]
host = "localhost"
port = 5432
""")
print(debug, cfg["database"]["port"])
