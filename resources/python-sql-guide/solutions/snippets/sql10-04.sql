CREATE TABLE dim_customer (customer_key INTEGER PRIMARY KEY AUTOINCREMENT, customer_id TEXT, name TEXT, country TEXT, valid_from TEXT, valid_to TEXT, is_current INT);
INSERT INTO dim_customer (customer_id, name, country, valid_from, valid_to, is_current) VALUES ('C-1', 'Ana', 'IN', '2023-01-01', '9999-12-31', 1);
CREATE TABLE fact_sales (sale_date TEXT, customer_key INT, revenue REAL);
INSERT INTO fact_sales VALUES ('2023-06-01', 1, 100);
-- Ana moves to the US on 2024-01-01: close the current row and insert a new version
UPDATE dim_customer SET valid_to = '2023-12-31', is_current = 0 WHERE customer_id = 'C-1' AND is_current = 1;
INSERT INTO dim_customer (customer_id, name, country, valid_from, valid_to, is_current) VALUES ('C-1', 'Ana', 'US', '2024-01-01', '9999-12-31', 1);
INSERT INTO fact_sales VALUES ('2024-03-01', 2, 250);
SELECT customer_key, customer_id, country, valid_from, valid_to, is_current FROM dim_customer ORDER BY customer_key;
SELECT d.country AS country_at_time_of_sale, SUM(f.revenue) AS revenue
FROM fact_sales f JOIN dim_customer d ON d.customer_key = f.customer_key GROUP BY d.country ORDER BY d.country;
