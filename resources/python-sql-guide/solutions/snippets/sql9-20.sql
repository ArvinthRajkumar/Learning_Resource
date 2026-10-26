WITH RECURSIVE chain AS (
  SELECT id, name, manager_id, 0 AS level, name AS path FROM employees WHERE manager_id IS NULL
  UNION ALL
  SELECT e.id, e.name, e.manager_id, c.level + 1, c.path || ' > ' || e.name
  FROM employees e JOIN chain c ON e.manager_id = c.id)
SELECT level, name, path FROM chain ORDER BY path;
