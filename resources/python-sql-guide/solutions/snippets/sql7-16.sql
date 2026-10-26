WITH assigned AS (
  SELECT id AS user_id, CASE WHEN id % 2 = 0 THEN 'control' ELSE 'variant' END AS grp FROM users),
conv AS (
  SELECT user_id, MAX(event = 'purchase') AS bought FROM events GROUP BY user_id)
SELECT a.grp, COUNT(*) AS users, SUM(COALESCE(c.bought, 0)) AS buyers,
       ROUND(100.0 * SUM(COALESCE(c.bought, 0)) / COUNT(*), 1) AS conversion_pct
FROM assigned a LEFT JOIN conv c ON c.user_id = a.user_id
GROUP BY a.grp;
