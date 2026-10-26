WITH t AS (
  SELECT user_id, started,
         LAG(ended) OVER (PARTITION BY user_id ORDER BY started) AS prev_end
  FROM sessions),
m AS (
  SELECT user_id, started,
         CASE WHEN prev_end IS NULL OR (julianday(started) - julianday(prev_end)) * 1440 > 30 THEN 1 ELSE 0 END AS new_session
  FROM t)
SELECT user_id, started,
       SUM(new_session) OVER (PARTITION BY user_id ORDER BY started) AS session_no
FROM m
ORDER BY user_id, started;
