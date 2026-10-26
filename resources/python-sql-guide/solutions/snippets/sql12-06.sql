PRAGMA foreign_keys = ON;
CREATE TABLE user (id INTEGER PRIMARY KEY, handle TEXT NOT NULL UNIQUE);
CREATE TABLE follow (follower_id INT NOT NULL REFERENCES user(id), followee_id INT NOT NULL REFERENCES user(id), since TEXT NOT NULL,
                     PRIMARY KEY (follower_id, followee_id), CHECK (follower_id <> followee_id));
CREATE INDEX idx_follow_followee ON follow(followee_id, follower_id);   -- the reverse lookup: who follows X
CREATE TABLE post (id INTEGER PRIMARY KEY, author_id INT NOT NULL REFERENCES user(id), body TEXT NOT NULL, created TEXT NOT NULL);
CREATE INDEX idx_post_author_created ON post(author_id, created DESC);
INSERT INTO user VALUES (1,'ana'),(2,'bo'),(3,'cy'),(4,'di');
INSERT INTO follow VALUES (1,2,'2024-01-01'),(1,3,'2024-01-02'),(2,1,'2024-01-03'),(3,1,'2024-01-04'),(4,1,'2024-01-05'),(2,3,'2024-01-06');
INSERT INTO post VALUES (1,2,'bo post 1','2024-03-01'),(2,3,'cy post 1','2024-03-02'),(3,2,'bo post 2','2024-03-03'),(4,4,'di post','2024-03-04'),(5,1,'ana post','2024-03-05');
-- feed for ana: posts by people ana follows, newest first
SELECT u.handle, p.body, p.created FROM post p JOIN follow f ON f.followee_id = p.author_id JOIN user u ON u.id = p.author_id
WHERE f.follower_id = 1 ORDER BY p.created DESC LIMIT 10;
