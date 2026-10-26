SELECT department, name, salary FROM (
  SELECT d.name AS department, e.name, e.salary, RANK() OVER (PARTITION BY d.id ORDER BY e.salary DESC) AS r
  FROM employees e JOIN departments d ON d.id = e.dept_id)
WHERE r = 1 ORDER BY department, name;
