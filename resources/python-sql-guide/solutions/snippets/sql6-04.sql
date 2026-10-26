SELECT COUNT(*) FILTER (WHERE status = 'paid') AS paid, COUNT(*) FILTER (WHERE status <> 'paid') AS other
FROM orders;
