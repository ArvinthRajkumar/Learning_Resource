PRAGMA foreign_keys = ON;
CREATE TABLE copy (id INTEGER PRIMARY KEY, book_id INT NOT NULL, barcode TEXT NOT NULL UNIQUE);
CREATE TABLE loan (id INTEGER PRIMARY KEY, copy_id INT NOT NULL REFERENCES copy(id), member_id INT NOT NULL, borrowed_on TEXT NOT NULL, due_on TEXT NOT NULL, returned_on TEXT);
CREATE UNIQUE INDEX one_open_loan_per_copy ON loan(copy_id) WHERE returned_on IS NULL;
INSERT INTO copy VALUES (1,1,'B-1'),(2,2,'B-2'),(3,2,'B-3');
INSERT INTO loan VALUES (1,1,1,'2024-03-01','2024-03-15',NULL),(2,2,1,'2024-03-05','2024-03-19','2024-03-12');
INSERT INTO loan VALUES (3,1,2,'2024-03-16','2024-03-30',NULL);
