SELECT c.name,
       SUM(o.status = 'paid') AS paid,
       SUM(o.status = 'pending') AS pending,
       SUM(o.status = 'cancelled') AS cancelled
FROM customers c LEFT JOIN orders o ON o.customer_id = c.id
GROUP BY c.id, c.name
ORDER BY c.id;
