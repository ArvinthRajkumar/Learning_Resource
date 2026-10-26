SELECT o.id, c.name AS customer, p.name AS product, i.qty, i.qty * p.price AS line_total
FROM orders o
JOIN customers c   ON c.id = o.customer_id
JOIN order_items i ON i.order_id = o.id
JOIN products p    ON p.id = i.product_id
WHERE o.id IN (1, 6)
ORDER BY o.id, p.name;
