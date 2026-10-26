WITH g AS (
  SELECT user_id, day, julianday(day) - ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY day) AS grp FROM logins
), streaks AS (
  SELECT user_id, MIN(day) AS start_day, MAX(day) AS end_day, COUNT(*) AS len FROM g GROUP BY user_id, grp
)
SELECT user_id, start_day, end_day, len FROM (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY len DESC, start_day) AS r FROM streaks
) WHERE r = 1 ORDER BY user_id;
