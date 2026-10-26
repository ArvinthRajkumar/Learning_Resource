SELECT 7 / 2 AS integer_division, 7 / 2.0 AS decimal_division, 7 % 3 AS remainder,
       'ab' || 'cd' AS concatenated, date('2024-01-31', '+1 month') AS add_month,
       group_concat('x') AS agg;
