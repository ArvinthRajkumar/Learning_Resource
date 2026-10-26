CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE TABLE books   (id INTEGER PRIMARY KEY, title TEXT NOT NULL, published INTEGER);
CREATE TABLE book_authors (
    book_id   INTEGER NOT NULL REFERENCES books(id)   ON DELETE CASCADE,
    author_id INTEGER NOT NULL REFERENCES authors(id) ON DELETE RESTRICT,
    role      TEXT NOT NULL DEFAULT 'author',
    PRIMARY KEY (book_id, author_id)
);
INSERT INTO authors VALUES (1, 'Ada'), (2, 'Ben');
INSERT INTO books VALUES (1, 'Joint Work', 2020);
INSERT INTO book_authors (book_id, author_id) VALUES (1, 1), (1, 2);
SELECT b.title, GROUP_CONCAT(a.name, ' & ') AS authors
FROM books b JOIN book_authors ba ON ba.book_id = b.id JOIN authors a ON a.id = ba.author_id
GROUP BY b.id;
