CREATE TABLE t (id INTEGER PRIMARY KEY, created TEXT);
WITH RECURSIVE n(i) AS (SELECT 1 UNION ALL SELECT i + 1 FROM n WHERE i < 3000)
INSERT INTO t SELECT i, date('2023-01-01', '+' || i || ' days') FROM n;
CREATE INDEX idx_created ON t(created);
EXPLAIN QUERY PLAN SELECT * FROM t WHERE strftime('%Y', created) = '2024';
