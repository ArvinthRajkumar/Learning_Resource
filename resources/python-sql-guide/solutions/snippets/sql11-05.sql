CREATE TABLE t (id INTEGER PRIMARY KEY, status TEXT, user_id INT, created TEXT);
WITH RECURSIVE n(i) AS (SELECT 1 UNION ALL SELECT i + 1 FROM n WHERE i < 20000)
INSERT INTO t SELECT i, CASE WHEN i % 1000 = 0 THEN 'rare' ELSE 'common' END, i % 500, date('2024-01-01', '+' || (i % 365) || ' days') FROM n;
CREATE INDEX idx_status ON t(status);
ANALYZE;
EXPLAIN QUERY PLAN SELECT * FROM t WHERE status = 'common';
