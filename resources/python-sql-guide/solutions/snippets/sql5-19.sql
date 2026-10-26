WITH monthly AS (
  SELECT strftime('%Y-%m', o.order_date) AS month, SUM(i.qty * p.price) AS revenue
  FROM orders o JOIN order_items i ON i.order_id = o.id JOIN products p ON p.id = i.product_id
  WHERE o.status = 'paid' GROUP BY month
)
SELECT month, revenue,
       LAG(revenue) OVER (ORDER BY month) AS prev,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month), 1) AS growth_pct
FROM monthly ORDER BY month;
