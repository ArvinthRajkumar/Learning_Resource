SELECT substr(u.signup_date, 1, 7) AS cohort,
       COUNT(DISTINCT u.id) AS users,
       COALESCE(SUM(e.amount), 0) AS revenue,
       ROUND(1.0 * COALESCE(SUM(e.amount), 0) / COUNT(DISTINCT u.id), 1) AS revenue_per_user
FROM users u LEFT JOIN events e ON e.user_id = u.id AND e.event = 'purchase'
GROUP BY cohort
ORDER BY cohort;
