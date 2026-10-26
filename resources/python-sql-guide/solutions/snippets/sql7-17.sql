-- Fan-out: joining users to both purchases and visits multiplies rows
SELECT SUM(p.amount) AS wrong_revenue
FROM events p JOIN events v ON v.user_id = p.user_id AND v.event = 'visit'
WHERE p.event = 'purchase';
