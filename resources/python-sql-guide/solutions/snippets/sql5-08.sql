WITH sold AS (
  SELECT p.category, p.name, SUM(i.qty) AS units
  FROM order_items i JOIN products p ON p.id = i.product_id
  JOIN orders o ON o.id = i.order_id AND o.status = 'paid'
  GROUP BY p.id
)
SELECT category, name, units FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY units DESC, name) AS r FROM sold
) WHERE r = 1 ORDER BY category;
