CREATE TABLE customers (id INTEGER PRIMARY KEY, name TEXT NOT NULL, city TEXT, signup_date TEXT);
INSERT INTO customers VALUES
 (1,'Ada','London','2023-01-05'),(2,'Ben','Paris','2023-02-11'),(3,'Chloe','London','2023-03-02'),
 (4,'Dev','Mumbai','2023-03-20'),(5,'Eli',NULL,'2023-04-08'),(6,'Fay','Paris','2023-05-17'),
 (7,'Gus','Berlin','2023-06-01'),(8,'Hana','Mumbai','2023-06-21');
CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT NOT NULL, category TEXT, price REAL NOT NULL);
INSERT INTO products VALUES
 (1,'Laptop','electronics',1200),(2,'Phone','electronics',800),(3,'Headphones','electronics',150),
 (4,'Desk','furniture',300),(5,'Chair','furniture',180),(6,'Notebook','stationery',5),(7,'Pen','stationery',2);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INTEGER REFERENCES customers(id), order_date TEXT NOT NULL, status TEXT NOT NULL);
INSERT INTO orders VALUES
 (1,1,'2024-01-10','paid'),(2,1,'2024-02-14','paid'),(3,2,'2024-01-20','paid'),(4,3,'2024-02-02','cancelled'),
 (5,3,'2024-02-25','paid'),(6,4,'2024-03-05','paid'),(7,2,'2024-03-12','paid'),(8,1,'2024-03-18','pending'),
 (9,5,'2024-03-22','paid'),(10,6,'2024-04-01','paid');
CREATE TABLE order_items (order_id INTEGER REFERENCES orders(id), product_id INTEGER REFERENCES products(id), qty INTEGER NOT NULL, PRIMARY KEY (order_id, product_id));
INSERT INTO order_items VALUES
 (1,1,1),(1,6,10),(2,3,2),(2,7,20),(3,2,1),(4,4,1),(5,5,2),(5,6,3),(6,2,1),(6,3,1),(7,1,1),(8,4,1),(8,5,1),(9,7,50),(10,6,5),(10,3,1);
