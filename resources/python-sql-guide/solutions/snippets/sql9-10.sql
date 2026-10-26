WITH totals AS (
  SELECT o.id AS order_id, SUM(oi.qty * p.price) AS total
  FROM orders o JOIN order_items oi ON oi.order_id = o.id JOIN products p ON p.id = oi.product_id
  WHERE o.status = 'paid' GROUP BY o.id)
SELECT order_id, total FROM totals WHERE total > (SELECT AVG(total) FROM totals) ORDER BY total DESC;
