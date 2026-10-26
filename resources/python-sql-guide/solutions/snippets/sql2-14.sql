CREATE TABLE tasks (id INTEGER PRIMARY KEY, title TEXT, done INTEGER DEFAULT 0);
INSERT INTO tasks (title) VALUES ('write'), ('test'), ('ship');
UPDATE tasks SET done = 1 WHERE title IN ('write', 'test') RETURNING id, title, done;
