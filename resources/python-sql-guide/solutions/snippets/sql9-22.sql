CREATE TABLE seq (id INTEGER PRIMARY KEY);
INSERT INTO seq VALUES (1),(2),(3),(7),(8),(12);
SELECT id + 1 AS gap_starts, next_id - 1 AS gap_ends FROM (
  SELECT id, LEAD(id) OVER (ORDER BY id) AS next_id FROM seq) WHERE next_id - id > 1;
