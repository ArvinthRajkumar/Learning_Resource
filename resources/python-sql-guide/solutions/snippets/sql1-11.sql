SELECT category, ROUND(avg_price, 1) AS avg_price
FROM (SELECT category, AVG(price) AS avg_price FROM products GROUP BY category) t   -- derived table
WHERE avg_price > 100;
