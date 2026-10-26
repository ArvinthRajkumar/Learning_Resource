SELECT event, COUNT(*) AS n, COUNT(DISTINCT user_id) AS users, SUM(amount) AS revenue
FROM events
GROUP BY event
ORDER BY n DESC;
