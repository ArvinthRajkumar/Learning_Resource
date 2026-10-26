SELECT name, price FROM products
WHERE price BETWEEN 100 AND 500
   OR name LIKE 'P%'
ORDER BY price DESC;
