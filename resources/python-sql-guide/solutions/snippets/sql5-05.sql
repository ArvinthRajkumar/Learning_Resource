SELECT d.name, ROUND(AVG(e.salary), 0) AS avg_salary
FROM employees e JOIN departments d ON d.id = e.dept_id
GROUP BY d.id
ORDER BY avg_salary DESC
LIMIT 1;
