SELECT c.name
FROM customers c
JOIN orders o ON o.customer_id = c.id AND o.status = 'paid'
JOIN order_items oi ON oi.order_id = o.id
JOIN products p ON p.id = oi.product_id AND p.category = 'electronics' AND p.price < 1000
GROUP BY c.id, c.name
HAVING COUNT(DISTINCT p.id) = (SELECT COUNT(*) FROM products WHERE category = 'electronics' AND price < 1000);
