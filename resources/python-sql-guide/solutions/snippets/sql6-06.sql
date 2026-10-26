-- QUALIFY (Snowflake/BigQuery) simulated with a subquery: the most expensive product per category
SELECT category, name, price FROM (
  SELECT category, name, price, RANK() OVER (PARTITION BY category ORDER BY price DESC) AS r FROM products)
WHERE r = 1 ORDER BY category;
