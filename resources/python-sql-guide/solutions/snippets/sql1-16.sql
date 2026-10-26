SELECT id FROM customers
EXCEPT
SELECT customer_id FROM orders
ORDER BY 1;
