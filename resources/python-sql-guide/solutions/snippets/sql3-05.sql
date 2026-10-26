CREATE TABLE doc (id INTEGER PRIMARY KEY, body TEXT, version INTEGER NOT NULL DEFAULT 1);
INSERT INTO doc (id, body) VALUES (1, 'draft');
-- two editors both read version 1; the first save wins
UPDATE doc SET body = 'edit A', version = version + 1 WHERE id = 1 AND version = 1;
SELECT changes() AS rows_updated_first;
