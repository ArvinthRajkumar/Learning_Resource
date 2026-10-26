SELECT u.name, u.signup_date, MIN(date(e.ts)) AS first_purchase
FROM users u JOIN events e ON e.user_id = u.id AND e.event = 'purchase'
GROUP BY u.id
HAVING julianday(MIN(date(e.ts))) - julianday(u.signup_date) <= 7
ORDER BY u.id;
