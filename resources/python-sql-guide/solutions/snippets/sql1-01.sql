SELECT o.id AS order_id, c.name, o.order_date, o.status
FROM orders AS o
JOIN customers AS c ON c.id = o.customer_id
ORDER BY o.id
LIMIT 5;
