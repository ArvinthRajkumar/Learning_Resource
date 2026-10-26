-- page 2 of products ordered by id, 3 per page, using the last id seen on page 1
SELECT id, name FROM products WHERE id > 3 ORDER BY id LIMIT 3;
