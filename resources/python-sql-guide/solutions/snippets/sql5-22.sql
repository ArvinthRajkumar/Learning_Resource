WITH ordered AS (
  SELECT user_id, started, ended,
         MAX(ended) OVER (PARTITION BY user_id ORDER BY started ROWS BETWEEN UNBOUNDED PRECEDING AND 1 PRECEDING) AS prev_max_end
  FROM sessions
), flagged AS (
  SELECT *, CASE WHEN prev_max_end IS NULL OR started > prev_max_end THEN 1 ELSE 0 END AS new_group FROM ordered
), grouped AS (
  SELECT *, SUM(new_group) OVER (PARTITION BY user_id ORDER BY started) AS g FROM flagged
)
SELECT user_id, MIN(started) AS merged_start, MAX(ended) AS merged_end
FROM grouped GROUP BY user_id, g ORDER BY user_id, merged_start;
