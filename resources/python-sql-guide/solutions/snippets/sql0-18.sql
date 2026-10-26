ALTER TABLE customers ADD COLUMN vip INTEGER DEFAULT 0;
UPDATE customers SET vip = 1 WHERE id IN (1, 3);
SELECT name, vip FROM customers WHERE vip = 1;
