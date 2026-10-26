CREATE TABLE person (id INTEGER PRIMARY KEY, email TEXT);
INSERT INTO person (email) VALUES ('a@x.com'), ('b@x.com'), ('a@x.com'), ('c@x.com'), ('b@x.com'), ('a@x.com');
SELECT email, COUNT(*) AS n FROM person GROUP BY email HAVING COUNT(*) > 1 ORDER BY email;
