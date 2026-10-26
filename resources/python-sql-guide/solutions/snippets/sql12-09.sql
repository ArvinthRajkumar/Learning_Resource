CREATE TABLE stock_movement (id INTEGER PRIMARY KEY, product_id INT, warehouse_id INT, delta INT);
CREATE TRIGGER no_negative_stock BEFORE INSERT ON stock_movement
BEGIN
  SELECT RAISE(ABORT, 'insufficient stock')
  WHERE (SELECT COALESCE(SUM(delta), 0) FROM stock_movement WHERE product_id = NEW.product_id AND warehouse_id = NEW.warehouse_id) + NEW.delta < 0;
END;
INSERT INTO stock_movement (product_id, warehouse_id, delta) VALUES (1, 1, 50);
INSERT INTO stock_movement (product_id, warehouse_id, delta) VALUES (1, 1, -60);
