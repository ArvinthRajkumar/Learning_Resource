WITH RECURSIVE org AS (
    SELECT id, name, manager_id, 0 AS depth, name AS path
    FROM employees WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id, o.depth + 1, o.path || ' > ' || e.name
    FROM employees e
    JOIN org o ON e.manager_id = o.id
)
SELECT depth, path FROM org ORDER BY path;
