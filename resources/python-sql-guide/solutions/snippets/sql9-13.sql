WITH r AS (SELECT salary, ROW_NUMBER() OVER (ORDER BY salary) AS rn, COUNT(*) OVER () AS n FROM employees)
SELECT AVG(salary) AS median_salary FROM r WHERE rn IN ((n + 1) / 2, (n + 2) / 2);
