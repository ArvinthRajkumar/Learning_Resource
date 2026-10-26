SELECT name, dept_id, salary,
       ROUND(AVG(salary) OVER (PARTITION BY dept_id)) AS dept_avg,
       RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank_in_dept
FROM employees WHERE dept_id = 1 ORDER BY rank_in_dept, name;
