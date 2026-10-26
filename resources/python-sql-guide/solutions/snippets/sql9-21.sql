CREATE TABLE contact (id INTEGER PRIMARY KEY, email TEXT, name TEXT);
INSERT INTO contact VALUES (1,'a@x.com','A'),(2,'b@x.com','B'),(3,'a@x.com','A2'),(4,'a@x.com','A3'),(5,'c@x.com','C');
SELECT email, COUNT(*) AS copies FROM contact GROUP BY email HAVING COUNT(*) > 1;
DELETE FROM contact WHERE id NOT IN (SELECT MIN(id) FROM contact GROUP BY email);
SELECT id, email FROM contact ORDER BY id;
