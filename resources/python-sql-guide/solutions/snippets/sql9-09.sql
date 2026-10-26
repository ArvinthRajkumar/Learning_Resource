SELECT a.name AS person_a, b.name AS person_b, d.name AS department
FROM employees a JOIN employees b ON a.dept_id = b.dept_id AND a.id < b.id
JOIN departments d ON d.id = a.dept_id
ORDER BY d.name, a.name, b.name;
