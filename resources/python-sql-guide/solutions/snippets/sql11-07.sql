CREATE TABLE ticket (id INTEGER PRIMARY KEY, status TEXT, email TEXT);
WITH RECURSIVE n(i) AS (SELECT 1 UNION ALL SELECT i + 1 FROM n WHERE i < 3000)
INSERT INTO ticket SELECT i, CASE WHEN i % 50 = 0 THEN 'open' ELSE 'closed' END, 'User' || i || '@Example.com' FROM n;
CREATE INDEX idx_open ON ticket(id) WHERE status = 'open';
CREATE INDEX idx_email_lower ON ticket(lower(email));
EXPLAIN QUERY PLAN SELECT id FROM ticket WHERE status = 'open' ORDER BY id;
EXPLAIN QUERY PLAN SELECT * FROM ticket WHERE lower(email) = 'user42@example.com';
