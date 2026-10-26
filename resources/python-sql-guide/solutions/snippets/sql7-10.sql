SELECT day, amount,
       ROUND(AVG(amount) OVER (ORDER BY day ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 1) AS moving_avg_3,
       amount - LAG(amount) OVER (ORDER BY day) AS change,
       ROUND(100.0 * (amount - LAG(amount) OVER (ORDER BY day)) / LAG(amount) OVER (ORDER BY day), 1) AS change_pct,
       SUM(amount) OVER (ORDER BY day) AS cumulative
FROM daily_sales;
