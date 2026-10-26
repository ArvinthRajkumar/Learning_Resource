CREATE TABLE customer_totals AS
SELECT c.id AS customer_id, COALESCE(SUM(i.qty * p.price), 0) AS spent
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.status = 'paid'
LEFT JOIN order_items i ON i.order_id = o.id
LEFT JOIN products p ON p.id = i.product_id
GROUP BY c.id;
SELECT COUNT(*) AS rows_created, SUM(spent) AS total FROM customer_totals;
