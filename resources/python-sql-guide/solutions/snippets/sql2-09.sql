WITH numbered AS (
    SELECT user_id, day,
           julianday(day) - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY day) AS grp
    FROM logins
)
SELECT user_id, MIN(day) AS streak_start, MAX(day) AS streak_end, COUNT(*) AS days
FROM numbered
GROUP BY user_id, grp
ORDER BY user_id, streak_start;
