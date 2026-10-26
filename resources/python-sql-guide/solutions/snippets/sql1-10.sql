SELECT name FROM customers
WHERE id IN (SELECT customer_id FROM orders WHERE status = 'paid')   -- list subquery
ORDER BY name;
