SELECT strftime('%Y-%m', order_date) AS month,
       SUM(CASE WHEN status = 'paid' THEN 1 ELSE 0 END) AS paid,
       SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) AS pending,
       SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled
FROM orders
GROUP BY month
ORDER BY month;
