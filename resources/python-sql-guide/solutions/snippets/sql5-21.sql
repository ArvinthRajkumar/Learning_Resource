SELECT day, amount FROM (
  SELECT day, amount, LAG(amount) OVER (ORDER BY day) AS prev FROM daily_sales
) WHERE amount > prev ORDER BY day;
