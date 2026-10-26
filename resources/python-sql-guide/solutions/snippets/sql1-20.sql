SELECT order_date,
       strftime('%Y-%m', order_date) AS month,
       strftime('%w', order_date) AS weekday_num,
       date(order_date, '+30 days') AS plus_30,
       julianday('2024-04-01') - julianday(order_date) AS days_ago
FROM orders
WHERE id <= 3;
