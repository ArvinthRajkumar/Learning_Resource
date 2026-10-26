CREATE TABLE dim_customer (customer_key INTEGER PRIMARY KEY, name TEXT, segment TEXT, country TEXT);
CREATE TABLE dim_product (product_key INTEGER PRIMARY KEY, category TEXT);
CREATE TABLE fact_sales (customer_key INT, product_key INT, revenue REAL, cost REAL);
INSERT INTO dim_customer VALUES (1,'Ana','retail','IN'),(2,'Bo','wholesale','US'),(3,'Cy','retail','US');
INSERT INTO dim_product VALUES (1,'stationery'),(2,'furniture');
INSERT INTO fact_sales VALUES (1,1,15,6),(2,2,300,180),(3,1,25,10),(1,1,20,8),(2,1,140,60),(3,2,600,360);
-- margin is a ratio: compute it from additive parts, never average stored ratios
SELECT c.country, c.segment, SUM(f.revenue) AS revenue,
       ROUND(100.0 * SUM(f.revenue - f.cost) / SUM(f.revenue), 1) AS margin_pct
FROM fact_sales f JOIN dim_customer c ON c.customer_key = f.customer_key
GROUP BY c.country, c.segment ORDER BY revenue DESC;
