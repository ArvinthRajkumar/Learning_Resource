CREATE TABLE dim_date (date_key INTEGER PRIMARY KEY, full_date TEXT, year INT, quarter INT, month INT, month_name TEXT, is_weekend INT);
CREATE TABLE dim_customer (customer_key INTEGER PRIMARY KEY, customer_id TEXT, name TEXT, segment TEXT, country TEXT);
CREATE TABLE dim_product (product_key INTEGER PRIMARY KEY, sku TEXT, name TEXT, category TEXT, brand TEXT);
CREATE TABLE fact_sales (
  date_key INT REFERENCES dim_date, customer_key INT REFERENCES dim_customer, product_key INT REFERENCES dim_product,
  quantity INT, revenue REAL, cost REAL);
INSERT INTO dim_date VALUES (20240101,'2024-01-01',2024,1,1,'January',0),(20240102,'2024-01-02',2024,1,1,'January',0),(20240203,'2024-02-03',2024,1,2,'February',1),(20240310,'2024-03-10',2024,1,3,'March',1);
INSERT INTO dim_customer VALUES (1,'C-100','Ana','retail','IN'),(2,'C-200','Bo','wholesale','US'),(3,'C-300','Cy','retail','US');
INSERT INTO dim_product VALUES (1,'P-1','Pen','stationery','Acme'),(2,'P-2','Desk','furniture','Woodly'),(3,'P-3','Notebook','stationery','Acme');
INSERT INTO fact_sales VALUES
 (20240101,1,1,10,15,6),(20240101,2,2,1,300,180),(20240102,3,3,5,25,10),(20240203,1,3,4,20,8),(20240203,2,1,100,140,60),(20240310,3,2,2,600,360),(20240310,1,1,20,30,12);
SELECT d.month_name, p.category, SUM(f.revenue) AS revenue, SUM(f.revenue - f.cost) AS profit
FROM fact_sales f
JOIN dim_date d ON d.date_key = f.date_key
JOIN dim_product p ON p.product_key = f.product_key
GROUP BY d.month, d.month_name, p.category
ORDER BY d.month, p.category;
