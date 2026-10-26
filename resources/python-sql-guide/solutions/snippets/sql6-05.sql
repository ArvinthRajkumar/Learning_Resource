SELECT customer_id, order_date, status FROM (
  SELECT customer_id, order_date, status, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC) AS rn FROM orders)
WHERE rn = 1 ORDER BY customer_id;
