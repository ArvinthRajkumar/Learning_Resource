SELECT DISTINCT salary AS third_highest
FROM (SELECT salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS r FROM employees)
WHERE r = 3;
