-- Wrong: SUM(p.price) is repeated once per item, and orders are repeated per line
SELECT COUNT(*) AS rows_after_join, COUNT(DISTINCT o.id) AS real_orders
FROM orders o JOIN order_items i ON i.order_id = o.id;
