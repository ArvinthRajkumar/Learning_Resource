WITH activity AS (
  SELECT DISTINCT u.id AS user_id,
         substr(u.signup_date, 1, 7) AS cohort,
         (CAST(substr(e.ts, 1, 4) AS INT) - CAST(substr(u.signup_date, 1, 4) AS INT)) * 12
         + CAST(substr(e.ts, 6, 2) AS INT) - CAST(substr(u.signup_date, 6, 2) AS INT) AS month_n
  FROM users u JOIN events e ON e.user_id = u.id)
SELECT cohort,
       COUNT(DISTINCT CASE WHEN month_n = 0 THEN user_id END) AS m0,
       COUNT(DISTINCT CASE WHEN month_n = 1 THEN user_id END) AS m1,
       COUNT(DISTINCT CASE WHEN month_n = 2 THEN user_id END) AS m2
FROM activity
GROUP BY cohort
ORDER BY cohort;
