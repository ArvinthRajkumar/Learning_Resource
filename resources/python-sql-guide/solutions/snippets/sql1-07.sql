SELECT c.name, p.category
FROM (SELECT name FROM customers WHERE id <= 2) c
CROSS JOIN (SELECT DISTINCT category FROM products) p
ORDER BY c.name, p.category;
