SELECT dept_id, name, salary
FROM (
    SELECT dept_id, name, salary,
           DENSE_RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) AS r
    FROM employees WHERE dept_id IS NOT NULL
) t
WHERE r <= 2
ORDER BY dept_id, salary DESC, name;
