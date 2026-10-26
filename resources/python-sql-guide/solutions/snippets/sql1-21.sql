SELECT c.name,
       COALESCE(SUM(i.qty * p.price), 0) AS spent
FROM customers c
LEFT JOIN orders o     ON o.customer_id = c.id AND o.status = 'paid'
LEFT JOIN order_items i ON i.order_id = o.id
LEFT JOIN products p    ON p.id = i.product_id
GROUP BY c.id, c.name
ORDER BY spent DESC, c.name;
