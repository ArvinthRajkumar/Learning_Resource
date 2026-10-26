SELECT u.plan,
       COUNT(DISTINCT u.id) AS users,
       COUNT(DISTINCT CASE WHEN e.event = 'purchase' THEN u.id END) AS buyers,
       ROUND(100.0 * COUNT(DISTINCT CASE WHEN e.event = 'purchase' THEN u.id END) / COUNT(DISTINCT u.id), 1) AS buyer_pct,
       COALESCE(SUM(e.amount), 0) AS revenue
FROM users u LEFT JOIN events e ON e.user_id = u.id
GROUP BY u.plan
ORDER BY revenue DESC;
