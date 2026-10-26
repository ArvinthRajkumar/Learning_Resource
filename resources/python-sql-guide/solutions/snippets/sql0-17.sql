UPDATE products SET price = price * 1.10 WHERE category = 'stationery';
DELETE FROM order_items WHERE qty > 40;
INSERT INTO products (id, name, category, price) VALUES (8, 'Marker', 'stationery', 3);
SELECT name, category, price FROM products WHERE category = 'stationery' ORDER BY id;
