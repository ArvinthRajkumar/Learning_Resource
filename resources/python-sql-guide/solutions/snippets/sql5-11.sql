SELECT d.name, COUNT(e.id) AS headcount
FROM departments d LEFT JOIN employees e ON e.dept_id = d.id
GROUP BY d.id ORDER BY headcount DESC, d.name;
