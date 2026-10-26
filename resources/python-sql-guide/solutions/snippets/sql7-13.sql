SELECT CASE WHEN amount < 40 THEN '1: under 40'
            WHEN amount < 90 THEN '2: 40 to 89'
            ELSE '3: 90 and over' END AS bucket,
       COUNT(*) AS purchases, SUM(amount) AS revenue
FROM events WHERE event = 'purchase'
GROUP BY bucket
ORDER BY bucket;
