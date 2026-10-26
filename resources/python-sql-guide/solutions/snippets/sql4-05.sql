CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT, deleted INTEGER DEFAULT 0);
CREATE UNIQUE INDEX uq_email_live ON users(lower(email)) WHERE deleted = 0;   -- partial + expression
INSERT INTO users (email) VALUES ('Ada@x.com');
SELECT name FROM sqlite_master WHERE type = 'index' ORDER BY name;
