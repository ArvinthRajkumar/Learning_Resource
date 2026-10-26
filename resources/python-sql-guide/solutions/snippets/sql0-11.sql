SELECT COUNT(*) AS products,
       MIN(price) AS cheapest,
       MAX(price) AS dearest,
       SUM(price) AS total,
       ROUND(AVG(price), 2) AS average
FROM products;
