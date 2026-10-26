SELECT COUNT(*) AS all_rows, COUNT(city) AS with_city, COUNT(DISTINCT city) AS cities
FROM customers;
