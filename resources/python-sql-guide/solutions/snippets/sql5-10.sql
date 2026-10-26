SELECT 'empty department' AS what, d.name FROM departments d
LEFT JOIN employees e ON e.dept_id = d.id WHERE e.id IS NULL
UNION ALL
SELECT 'no department', name FROM employees WHERE dept_id IS NULL;
