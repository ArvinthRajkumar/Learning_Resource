CREATE TABLE copy (id INTEGER PRIMARY KEY, book_id INT, barcode TEXT);
CREATE TABLE loan (id INTEGER PRIMARY KEY, copy_id INT, returned_on TEXT);
INSERT INTO copy VALUES (1,1,'B-1'),(2,2,'B-2'),(3,2,'B-3');
INSERT INTO loan VALUES (1,1,NULL),(2,2,'2024-03-12');
SELECT c.book_id, COUNT(*) AS available_copies
FROM copy c WHERE NOT EXISTS (SELECT 1 FROM loan l WHERE l.copy_id = c.id AND l.returned_on IS NULL)
GROUP BY c.book_id ORDER BY c.book_id;
