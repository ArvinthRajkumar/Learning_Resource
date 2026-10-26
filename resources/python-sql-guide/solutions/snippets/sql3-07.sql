CREATE TABLE prices (sku TEXT PRIMARY KEY, price INTEGER);
CREATE TABLE price_audit (sku TEXT, old_price INTEGER, new_price INTEGER);
CREATE TRIGGER trg_price_audit AFTER UPDATE OF price ON prices
BEGIN
    INSERT INTO price_audit VALUES (OLD.sku, OLD.price, NEW.price);
END;
INSERT INTO prices VALUES ('pen', 2);
UPDATE prices SET price = 3 WHERE sku = 'pen';
SELECT * FROM price_audit;
