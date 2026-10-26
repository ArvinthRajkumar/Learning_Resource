WITH RECURSIVE days(d) AS (
    SELECT '2024-03-01'
    UNION ALL
    SELECT date(d, '+1 day') FROM days WHERE d < '2024-03-09'
)
SELECT d, COALESCE(s.amount, 0) AS amount
FROM days
LEFT JOIN daily_sales s ON s.day = d
ORDER BY d;
