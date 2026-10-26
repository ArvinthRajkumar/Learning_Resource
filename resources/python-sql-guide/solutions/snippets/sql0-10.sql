SELECT name,
       COALESCE(city, 'unknown') AS city,
       city IS NULL AS missing
FROM customers
WHERE id IN (4, 5);
