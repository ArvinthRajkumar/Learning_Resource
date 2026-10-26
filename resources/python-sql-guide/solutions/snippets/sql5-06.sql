SELECT name, dept_id, salary FROM (
  SELECT name, dept_id, salary, AVG(salary) OVER (PARTITION BY dept_id) AS dept_avg FROM employees
) WHERE salary > dept_avg ORDER BY dept_id, name;
