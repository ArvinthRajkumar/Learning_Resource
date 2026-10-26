CREATE TABLE stock (sku TEXT PRIMARY KEY, qty INTEGER NOT NULL);
INSERT INTO stock VALUES ('pen', 10);
INSERT INTO stock (sku, qty) VALUES ('pen', 5), ('book', 3)
ON CONFLICT (sku) DO UPDATE SET qty = stock.qty + excluded.qty;
SELECT * FROM stock ORDER BY sku;
