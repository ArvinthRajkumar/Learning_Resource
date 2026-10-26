SELECT category, SUM(price) AS total,
       ROUND(100.0 * SUM(price) / SUM(SUM(price)) OVER (), 1) AS pct_of_all
FROM products
GROUP BY category
ORDER BY total DESC;
