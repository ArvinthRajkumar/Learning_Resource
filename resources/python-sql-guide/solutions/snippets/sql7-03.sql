SELECT
  COUNT(DISTINCT CASE WHEN event = 'visit'       THEN user_id END) AS visited,
  COUNT(DISTINCT CASE WHEN event = 'add_to_cart' THEN user_id END) AS added_to_cart,
  COUNT(DISTINCT CASE WHEN event = 'purchase'    THEN user_id END) AS purchased
FROM events;
