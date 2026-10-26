SELECT name, dept_id, salary,
       ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS row_num,
       RANK()       OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rnk,
       DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS dense_rnk,
       NTILE(2)     OVER (PARTITION BY dept_id ORDER BY salary DESC) AS half
FROM employees
WHERE dept_id IN (1, 3)
ORDER BY dept_id, salary DESC, name;
