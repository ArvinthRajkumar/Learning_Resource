CREATE TABLE events (id INTEGER PRIMARY KEY, payload TEXT);
INSERT INTO events VALUES
 (1, '{"type":"click","user":{"id":7,"plan":"pro"},"tags":["a","b"]}'),
 (2, '{"type":"view","user":{"id":9,"plan":"free"},"tags":[]}');
SELECT id,
       json_extract(payload, '$.type') AS type,
       json_extract(payload, '$.user.plan') AS plan,
       json_array_length(payload, '$.tags') AS n_tags
FROM events
WHERE json_extract(payload, '$.user.id') = 7;
