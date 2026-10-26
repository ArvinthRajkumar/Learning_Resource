WITH f AS (
  SELECT COUNT(DISTINCT CASE WHEN event = 'visit'       THEN user_id END) AS v,
         COUNT(DISTINCT CASE WHEN event = 'add_to_cart' THEN user_id END) AS c,
         COUNT(DISTINCT CASE WHEN event = 'purchase'    THEN user_id END) AS p
  FROM events)
SELECT v, c, p,
       ROUND(100.0 * c / v, 1) AS visit_to_cart_pct,
       ROUND(100.0 * p / c, 1) AS cart_to_purchase_pct,
       ROUND(100.0 * p / v, 1) AS overall_pct
FROM f;
