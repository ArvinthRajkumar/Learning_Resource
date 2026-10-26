SELECT COUNT(*) AS events, MIN(ts) AS first_event, MAX(ts) AS last_event,
       SUM(amount IS NULL AND event = 'purchase') AS purchases_without_amount,
       SUM(user_id NOT IN (SELECT id FROM users)) AS orphan_events
FROM events;
