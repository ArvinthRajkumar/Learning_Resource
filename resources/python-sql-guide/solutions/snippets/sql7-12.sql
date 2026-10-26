WITH r AS (
  SELECT amount,
         ROW_NUMBER() OVER (ORDER BY amount) AS rn,
         COUNT(*) OVER () AS n
  FROM events WHERE event = 'purchase')
SELECT
  MIN(CASE WHEN rn >= 0.5 * n THEN amount END) AS p50,
  MIN(CASE WHEN rn >= 0.9 * n THEN amount END) AS p90,
  MIN(amount) AS min_amount, MAX(amount) AS max_amount, ROUND(AVG(amount), 1) AS mean
FROM r;
