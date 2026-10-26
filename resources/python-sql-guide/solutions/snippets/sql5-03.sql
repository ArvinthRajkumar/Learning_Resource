SELECT d.name AS department, e.name, e.salary
FROM employees e
JOIN departments d ON d.id = e.dept_id
WHERE e.salary = (SELECT MAX(salary) FROM employees WHERE dept_id = e.dept_id)
ORDER BY d.name, e.name;
