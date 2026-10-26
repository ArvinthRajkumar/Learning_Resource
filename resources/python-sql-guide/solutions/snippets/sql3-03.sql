CREATE VIEW order_totals AS
SELECT o.id AS order_id, o.customer_id, o.status, SUM(i.qty * p.price) AS total
FROM orders o
JOIN order_items i ON i.order_id = o.id
JOIN products p ON p.id = i.product_id
GROUP BY o.id;

SELECT c.name, ROUND(SUM(t.total), 2) AS paid_total
FROM order_totals t JOIN customers c ON c.id = t.customer_id
WHERE t.status = 'paid'
GROUP BY c.id
ORDER BY paid_total DESC
LIMIT 3;
