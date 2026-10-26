SELECT customer_id,
       COUNT(*) AS total,
       SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) AS paid,
       SUM(status = 'cancelled') AS cancelled
FROM orders
GROUP BY customer_id
ORDER BY customer_id;
