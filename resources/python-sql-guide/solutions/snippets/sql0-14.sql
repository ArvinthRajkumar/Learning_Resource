SELECT customer_id, COUNT(*) AS orders
FROM orders
WHERE status = 'paid'
GROUP BY customer_id
HAVING COUNT(*) >= 2
ORDER BY orders DESC;
