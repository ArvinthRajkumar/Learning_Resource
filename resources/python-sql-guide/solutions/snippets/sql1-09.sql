SELECT name, price
FROM products
WHERE price > (SELECT AVG(price) FROM products)      -- scalar subquery: one value
ORDER BY price DESC;
