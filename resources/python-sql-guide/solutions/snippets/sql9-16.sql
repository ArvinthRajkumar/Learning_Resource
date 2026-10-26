SELECT c.name, MIN(o.order_date) AS first_order, MAX(o.order_date) AS last_order,
       CAST(julianday(MAX(o.order_date)) - julianday(MIN(o.order_date)) AS INT) AS days_between
FROM customers c JOIN orders o ON o.customer_id = c.id AND o.status = 'paid'
GROUP BY c.id HAVING COUNT(*) > 1;
