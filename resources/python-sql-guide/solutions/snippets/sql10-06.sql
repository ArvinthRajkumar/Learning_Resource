CREATE TABLE stg_orders (order_id INT, amount REAL, updated_at TEXT);
CREATE TABLE fact_orders (order_id INTEGER PRIMARY KEY, amount REAL, updated_at TEXT);
INSERT INTO stg_orders VALUES (1, 10, '2024-03-01'), (2, 20, '2024-03-01');
INSERT INTO fact_orders SELECT * FROM stg_orders WHERE true ON CONFLICT(order_id) DO UPDATE SET amount = excluded.amount, updated_at = excluded.updated_at;
-- next day: order 2 corrected, order 3 new, order 1 unchanged and re-sent
DELETE FROM stg_orders;
INSERT INTO stg_orders VALUES (1, 10, '2024-03-01'), (2, 25, '2024-03-02'), (3, 30, '2024-03-02');
INSERT INTO fact_orders SELECT * FROM stg_orders WHERE true ON CONFLICT(order_id) DO UPDATE SET amount = excluded.amount, updated_at = excluded.updated_at;
INSERT INTO fact_orders SELECT * FROM stg_orders WHERE true ON CONFLICT(order_id) DO UPDATE SET amount = excluded.amount, updated_at = excluded.updated_at;   -- rerun: idempotent
SELECT * FROM fact_orders ORDER BY order_id;
