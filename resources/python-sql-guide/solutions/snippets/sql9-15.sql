SELECT c.name, o.order_date, SUM(oi.qty * p.price) AS order_total,
       SUM(SUM(oi.qty * p.price)) OVER (PARTITION BY c.id ORDER BY o.order_date) AS cumulative
FROM orders o JOIN customers c ON c.id = o.customer_id
JOIN order_items oi ON oi.order_id = o.id JOIN products p ON p.id = oi.product_id
WHERE o.status = 'paid'
GROUP BY c.id, o.id ORDER BY c.name, o.order_date;
