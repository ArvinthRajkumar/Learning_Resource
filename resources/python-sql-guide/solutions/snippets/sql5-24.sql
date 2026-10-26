CREATE TABLE person (id INTEGER PRIMARY KEY, email TEXT);
INSERT INTO person (email) VALUES ('a@x.com'), ('b@x.com'), ('a@x.com'), ('c@x.com'), ('b@x.com'), ('a@x.com');
DELETE FROM person WHERE id NOT IN (SELECT MIN(id) FROM person GROUP BY email);
SELECT id, email FROM person ORDER BY id;
