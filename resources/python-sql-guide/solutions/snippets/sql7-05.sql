WITH first_step AS (
  SELECT user_id, MIN(ts) AS t FROM events WHERE event = 'visit' GROUP BY user_id),
second AS (
  SELECT e.user_id, MIN(e.ts) AS t FROM events e JOIN first_step f ON f.user_id = e.user_id AND e.ts >= f.t
  WHERE e.event = 'add_to_cart' GROUP BY e.user_id),
third AS (
  SELECT e.user_id, MIN(e.ts) AS t FROM events e JOIN second s ON s.user_id = e.user_id AND e.ts >= s.t
  WHERE e.event = 'purchase' GROUP BY e.user_id)
SELECT (SELECT COUNT(*) FROM first_step) AS step1,
       (SELECT COUNT(*) FROM second) AS step2,
       (SELECT COUNT(*) FROM third) AS step3;
