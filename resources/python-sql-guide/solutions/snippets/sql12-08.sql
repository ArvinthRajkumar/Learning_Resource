PRAGMA foreign_keys = ON;
CREATE TABLE product (id INTEGER PRIMARY KEY, sku TEXT NOT NULL UNIQUE);
CREATE TABLE warehouse (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE);
CREATE TABLE stock_movement (
  id INTEGER PRIMARY KEY, product_id INT NOT NULL REFERENCES product(id), warehouse_id INT NOT NULL REFERENCES warehouse(id),
  delta INT NOT NULL CHECK (delta <> 0), reason TEXT NOT NULL CHECK (reason IN ('receipt','sale','return','adjustment','transfer')),
  ref TEXT, created TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP);
CREATE INDEX idx_move_prod_wh ON stock_movement(product_id, warehouse_id);
-- derived balance as a view
CREATE VIEW stock_level AS SELECT product_id, warehouse_id, SUM(delta) AS on_hand FROM stock_movement GROUP BY product_id, warehouse_id;
-- guard: a movement may not take stock below zero
CREATE TRIGGER no_negative_stock BEFORE INSERT ON stock_movement
BEGIN
  SELECT RAISE(ABORT, 'insufficient stock')
  WHERE (SELECT COALESCE(SUM(delta), 0) FROM stock_movement WHERE product_id = NEW.product_id AND warehouse_id = NEW.warehouse_id) + NEW.delta < 0;
END;
INSERT INTO product VALUES (1,'PEN'),(2,'DESK');
INSERT INTO warehouse VALUES (1,'North'),(2,'South');
INSERT INTO stock_movement (product_id, warehouse_id, delta, reason, ref) VALUES (1,1,100,'receipt','PO-1'),(1,1,-30,'sale','ORD-9'),(1,2,50,'receipt','PO-2'),(2,1,5,'receipt','PO-3'),(1,1,-20,'sale','ORD-10');
SELECT p.sku, w.name AS warehouse, s.on_hand FROM stock_level s JOIN product p ON p.id = s.product_id JOIN warehouse w ON w.id = s.warehouse_id ORDER BY p.sku, w.name;
