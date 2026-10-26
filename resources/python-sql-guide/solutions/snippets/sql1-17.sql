SELECT name, price,
       CASE WHEN price >= 1000 THEN 'premium'
            WHEN price >= 100  THEN 'standard'
            ELSE 'budget' END AS tier
FROM products
ORDER BY price DESC;
