CREATE TABLE acct (name TEXT PRIMARY KEY, balance INTEGER NOT NULL CHECK (balance >= 0));
INSERT INTO acct VALUES ('alice', 100), ('bob', 20);
BEGIN;
UPDATE acct SET balance = balance - 30 WHERE name = 'alice';
UPDATE acct SET balance = balance + 30 WHERE name = 'bob';
SELECT * FROM acct ORDER BY name;
ROLLBACK;
SELECT * FROM acct ORDER BY name;
