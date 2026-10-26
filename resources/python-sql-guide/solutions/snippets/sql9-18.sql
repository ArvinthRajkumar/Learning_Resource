SELECT day, amount FROM (
  SELECT day, amount, LAG(amount) OVER (ORDER BY day) AS prev,
         AVG(amount) OVER (ORDER BY day ROWS BETWEEN 3 PRECEDING AND 1 PRECEDING) AS prior_avg
  FROM daily_sales)
WHERE amount > prev AND amount > prior_avg;
