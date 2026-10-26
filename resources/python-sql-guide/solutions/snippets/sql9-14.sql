SELECT category, name, revenue FROM (
  SELECT p.category, p.name, SUM(oi.qty * p.price) AS revenue,
         ROW_NUMBER() OVER (PARTITION BY p.category ORDER BY SUM(oi.qty * p.price) DESC) AS rn
  FROM order_items oi JOIN orders o ON o.id = oi.order_id AND o.status = 'paid'
  JOIN products p ON p.id = oi.product_id GROUP BY p.id)
WHERE rn <= 2 ORDER BY category, revenue DESC;
