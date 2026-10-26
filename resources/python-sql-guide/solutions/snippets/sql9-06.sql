INSERT INTO products VALUES (8, 'Monitor', 'electronics', 250);
SELECT p.name FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.id
WHERE oi.order_id IS NULL;
