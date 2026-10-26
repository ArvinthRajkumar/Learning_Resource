SELECT c.name, COUNT(o.id) AS paid_orders
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.id AND o.status = 'paid'   -- condition in ON
GROUP BY c.id, c.name
ORDER BY c.id;
