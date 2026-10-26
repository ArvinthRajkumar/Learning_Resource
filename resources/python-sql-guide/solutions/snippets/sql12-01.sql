PRAGMA foreign_keys = ON;
CREATE TABLE author (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE book (id INTEGER PRIMARY KEY, isbn TEXT NOT NULL UNIQUE, title TEXT NOT NULL, year INT CHECK (year BETWEEN 1400 AND 2100));
CREATE TABLE book_author (book_id INT NOT NULL REFERENCES book(id), author_id INT NOT NULL REFERENCES author(id), PRIMARY KEY (book_id, author_id));
CREATE TABLE copy (id INTEGER PRIMARY KEY, book_id INT NOT NULL REFERENCES book(id), barcode TEXT NOT NULL UNIQUE);
CREATE TABLE member (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL UNIQUE);
CREATE TABLE loan (
  id INTEGER PRIMARY KEY, copy_id INT NOT NULL REFERENCES copy(id), member_id INT NOT NULL REFERENCES member(id),
  borrowed_on TEXT NOT NULL, due_on TEXT NOT NULL, returned_on TEXT,
  CHECK (due_on > borrowed_on), CHECK (returned_on IS NULL OR returned_on >= borrowed_on));
-- a copy can have at most one open (unreturned) loan: a partial unique index enforces it
CREATE UNIQUE INDEX one_open_loan_per_copy ON loan(copy_id) WHERE returned_on IS NULL;
CREATE INDEX idx_loan_member ON loan(member_id);
INSERT INTO author VALUES (1,'Le Guin'),(2,'Pratchett'),(3,'Gaiman');
INSERT INTO book VALUES (1,'111','A Wizard of Earthsea',1968),(2,'222','Good Omens',1990),(3,'333','Guards! Guards!',1989);
INSERT INTO book_author VALUES (1,1),(2,2),(2,3),(3,2);
INSERT INTO copy VALUES (1,1,'B-1'),(2,2,'B-2'),(3,2,'B-3'),(4,3,'B-4');
INSERT INTO member VALUES (1,'Ana','ana@x.org'),(2,'Bo','bo@x.org');
INSERT INTO loan VALUES (1,1,1,'2024-03-01','2024-03-15',NULL),(2,2,1,'2024-03-05','2024-03-19','2024-03-12'),(3,3,2,'2024-03-10','2024-03-24',NULL);
SELECT m.name, b.title, l.due_on FROM loan l JOIN member m ON m.id = l.member_id JOIN copy c ON c.id = l.copy_id JOIN book b ON b.id = c.book_id
WHERE l.returned_on IS NULL AND l.due_on < '2024-03-20' ORDER BY l.due_on;
