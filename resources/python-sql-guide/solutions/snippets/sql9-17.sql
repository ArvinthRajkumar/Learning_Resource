WITH d AS (
  SELECT user_id, day, julianday(day) - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY day) AS grp FROM logins),
s AS (SELECT user_id, grp, COUNT(*) AS streak FROM d GROUP BY user_id, grp)
SELECT user_id, MAX(streak) AS longest_streak FROM s GROUP BY user_id ORDER BY user_id;
