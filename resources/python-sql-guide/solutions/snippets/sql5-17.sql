WITH totals AS (
  SELECT o.id, o.customer_id, SUM(i.qty * p.price) AS total
  FROM orders o JOIN order_items i ON i.order_id = o.id JOIN products p ON p.id = i.product_id
  WHERE o.status = 'paid' GROUP BY o.id
)
SELECT COALESCE(c.city, 'unknown') AS city, COUNT(*) AS orders, ROUND(AVG(t.total), 2) AS avg_order_value
FROM totals t JOIN customers c ON c.id = t.customer_id
GROUP BY c.city ORDER BY avg_order_value DESC;
