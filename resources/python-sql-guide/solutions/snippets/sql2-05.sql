SELECT day, amount,
       SUM(amount) OVER (ORDER BY day) AS running_total,
       ROUND(AVG(amount) OVER (ORDER BY day ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 1) AS moving_avg_3,
       amount - LAG(amount) OVER (ORDER BY day) AS change_vs_prev,
       LEAD(amount) OVER (ORDER BY day) AS next_day
FROM daily_sales
ORDER BY day;
