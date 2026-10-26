SELECT p.name, p.category, p.price
FROM products p
WHERE p.price = (SELECT MAX(p2.price) FROM products p2 WHERE p2.category = p.category)
ORDER BY p.category;
