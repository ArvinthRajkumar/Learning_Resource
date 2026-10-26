SELECT c.name, COUNT(DISTINCT p.category) AS categories
FROM customers c
JOIN orders o ON o.customer_id = c.id AND o.status = 'paid'
JOIN order_items i ON i.order_id = o.id
JOIN products p ON p.id = i.product_id
GROUP BY c.id HAVING COUNT(DISTINCT p.category) >= 2
ORDER BY categories DESC, c.name;
