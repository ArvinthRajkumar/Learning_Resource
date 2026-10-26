CREATE TABLE people (id INTEGER PRIMARY KEY, sex TEXT);
INSERT INTO people VALUES (1, 'm'), (2, 'f'), (3, 'm');
UPDATE people SET sex = CASE sex WHEN 'm' THEN 'f' WHEN 'f' THEN 'm' END;
SELECT * FROM people ORDER BY id;
