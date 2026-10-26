WITH rfm AS (
  SELECT user_id,
         CAST(julianday('2024-05-01') - julianday(MAX(ts)) AS INT) AS recency_days,
         COUNT(*) AS frequency,
         SUM(amount) AS monetary
  FROM events WHERE event = 'purchase'
  GROUP BY user_id)
SELECT user_id, recency_days, frequency, monetary,
       NTILE(3) OVER (ORDER BY recency_days DESC) AS r_score,
       NTILE(3) OVER (ORDER BY frequency) AS f_score,
       NTILE(3) OVER (ORDER BY monetary) AS m_score
FROM rfm
ORDER BY monetary DESC;
