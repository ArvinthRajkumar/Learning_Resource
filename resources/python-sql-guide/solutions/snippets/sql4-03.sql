CREATE TABLE t (id INTEGER PRIMARY KEY, email TEXT, country TEXT, score INTEGER, created TEXT);
WITH RECURSIVE n(i) AS (SELECT 1 UNION ALL SELECT i + 1 FROM n WHERE i < 5000)
INSERT INTO t SELECT i, 'user' || i || '@x.com', CASE i % 4 WHEN 0 THEN 'US' WHEN 1 THEN 'UK' WHEN 2 THEN 'FR' ELSE 'DE' END, i % 100, date('2024-01-01', '+' || (i % 365) || ' days') FROM n;
CREATE INDEX idx_country_score ON t(country, score);
EXPLAIN QUERY PLAN SELECT id FROM t WHERE country = 'FR' AND score > 90;
