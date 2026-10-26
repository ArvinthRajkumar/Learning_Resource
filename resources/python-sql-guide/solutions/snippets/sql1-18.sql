SELECT name,
       LENGTH(name) AS len,
       UPPER(name) AS up,
       SUBSTR(name, 1, 3) AS first3,
       REPLACE(name, 'a', '*') AS replaced,
       name || ' (' || city || ')' AS label,
       INSTR(name, 'a') AS pos_a
FROM customers
WHERE city IS NOT NULL
LIMIT 3;
