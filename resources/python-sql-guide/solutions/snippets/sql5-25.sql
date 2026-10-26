WITH RECURSIVE chain AS (
  SELECT id, name FROM employees WHERE manager_id = 1
  UNION ALL
  SELECT e.id, e.name FROM employees e JOIN chain c ON e.manager_id = c.id
)
SELECT COUNT(*) AS total_reports FROM chain;
