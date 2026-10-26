SELECT name, salary,
       ROUND(AVG(salary) OVER (PARTITION BY dept_id)) AS dept_avg,
       salary - ROUND(AVG(salary) OVER (PARTITION BY dept_id)) AS diff
FROM employees WHERE dept_id IS NOT NULL
ORDER BY dept_id, salary DESC;
