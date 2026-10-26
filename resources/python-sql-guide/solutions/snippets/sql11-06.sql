CREATE TABLE ev (id INTEGER PRIMARY KEY, user_id INT, kind TEXT, ts TEXT, payload TEXT);
WITH RECURSIVE n(i) AS (SELECT 1 UNION ALL SELECT i + 1 FROM n WHERE i < 5000)
INSERT INTO ev SELECT i, i % 100, CASE i % 3 WHEN 0 THEN 'view' WHEN 1 THEN 'click' ELSE 'buy' END, date('2024-01-01', '+' || (i % 200) || ' days'), 'x' FROM n;
CREATE INDEX idx_user_kind_ts ON ev(user_id, kind, ts);
EXPLAIN QUERY PLAN SELECT * FROM ev WHERE user_id = 7 AND kind = 'buy' AND ts >= '2024-03-01';
EXPLAIN QUERY PLAN SELECT * FROM ev WHERE kind = 'buy';
EXPLAIN QUERY PLAN SELECT user_id, kind, ts FROM ev WHERE user_id = 7;
