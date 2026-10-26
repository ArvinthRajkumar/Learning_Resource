WITH RECURSIVE spine(day) AS (
  SELECT '2024-03-01' UNION ALL SELECT date(day, '+1 day') FROM spine WHERE day < '2024-03-10')
SELECT s.day, COALESCE(l.logins, 0) AS logins
FROM spine s
LEFT JOIN (SELECT day, COUNT(*) AS logins FROM logins GROUP BY day) l ON l.day = s.day
ORDER BY s.day;
