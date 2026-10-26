CREATE TABLE doc (id INTEGER PRIMARY KEY, body TEXT, version INTEGER NOT NULL DEFAULT 1);
INSERT INTO doc (id, body) VALUES (1, 'draft');
UPDATE doc SET body = 'edit A', version = version + 1 WHERE id = 1 AND version = 1;
UPDATE doc SET body = 'edit B', version = version + 1 WHERE id = 1 AND version = 1;   -- stale version
SELECT changes() AS rows_updated_second, (SELECT body FROM doc) AS body;
