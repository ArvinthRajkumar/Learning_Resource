SELECT category, COUNT(*) AS n, ROUND(AVG(price), 1) AS avg_price
FROM products
GROUP BY category
ORDER BY n DESC, category;
