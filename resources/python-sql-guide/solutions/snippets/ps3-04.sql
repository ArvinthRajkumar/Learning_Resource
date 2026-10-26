SELECT city, COUNT(*) AS customers        -- 5. compute
FROM customers                              -- 1. take the table
WHERE city IS NOT NULL                      -- 2. filter rows
GROUP BY city                               -- 3. make groups
HAVING COUNT(*) > 1                         -- 4. filter groups
ORDER BY customers DESC, city;              -- 6. sort
