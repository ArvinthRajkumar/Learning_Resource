WITH rev AS (
  SELECT user_id, SUM(amount) AS revenue FROM events WHERE event = 'purchase' GROUP BY user_id)
SELECT user_id, revenue,
       ROUND(100.0 * SUM(revenue) OVER (ORDER BY revenue DESC, user_id) / SUM(revenue) OVER (), 1) AS cumulative_pct
FROM rev
ORDER BY revenue DESC, user_id;
