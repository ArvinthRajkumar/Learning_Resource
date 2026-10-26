SELECT c.city, GROUP_CONCAT(c.name, ', ') AS customers
FROM customers c
WHERE c.city IS NOT NULL
GROUP BY c.city
ORDER BY c.city;
