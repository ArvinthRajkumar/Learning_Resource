WITH RECURSIVE d(day) AS (SELECT '2024-02-26' UNION ALL SELECT date(day, '+1 day') FROM d WHERE day < '2024-03-04')
SELECT day,
       CAST(strftime('%Y%m%d', day) AS INT) AS date_key,
       strftime('%w', day) AS weekday_num,
       CASE strftime('%w', day) WHEN '0' THEN 'Sun' WHEN '6' THEN 'Sat' ELSE 'weekday' END AS day_type,
       strftime('%W', day) AS week_of_year,
       strftime('%Y-%m', day) AS year_month
FROM d;
