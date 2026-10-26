SELECT p.category, SUM(oi.qty * p.price) AS revenue,
       ROUND(100.0 * SUM(oi.qty * p.price) / SUM(SUM(oi.qty * p.price)) OVER (), 1) AS pct_of_total
FROM order_items oi JOIN orders o ON o.id = oi.order_id AND o.status = 'paid'
JOIN products p ON p.id = oi.product_id
GROUP BY p.category ORDER BY revenue DESC;
