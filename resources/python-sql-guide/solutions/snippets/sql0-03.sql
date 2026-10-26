SELECT name,
       price,
       price * 1.2 AS price_with_tax,
       UPPER(category) AS category_uc
FROM products;
