SELECT customer_id, id AS last_order, order_date, status FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date DESC, id DESC) AS rn FROM orders
) WHERE rn = 1 ORDER BY customer_id;
