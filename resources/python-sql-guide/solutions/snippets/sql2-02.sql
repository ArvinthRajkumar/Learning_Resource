SELECT name, dept_id, salary,
       AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg,
       salary - AVG(salary) OVER (PARTITION BY dept_id) AS vs_avg
FROM employees
WHERE dept_id IS NOT NULL
ORDER BY dept_id, salary DESC;
