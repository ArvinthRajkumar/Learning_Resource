WITH paid_totals AS (
    SELECT o.customer_id, SUM(i.qty * p.price) AS spent
    FROM orders o
    JOIN order_items i ON i.order_id = o.id
    JOIN products p    ON p.id = i.product_id
    WHERE o.status = 'paid'
    GROUP BY o.customer_id
),
averages AS (
    SELECT AVG(spent) AS avg_spent FROM paid_totals
)
SELECT c.name, t.spent
FROM paid_totals t
JOIN customers c ON c.id = t.customer_id
CROSS JOIN averages a
WHERE t.spent > a.avg_spent
ORDER BY t.spent DESC;
