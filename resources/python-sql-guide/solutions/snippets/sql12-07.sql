CREATE TABLE user (id INTEGER PRIMARY KEY, handle TEXT);
CREATE TABLE follow (follower_id INT, followee_id INT, PRIMARY KEY (follower_id, followee_id));
INSERT INTO user VALUES (1,'ana'),(2,'bo'),(3,'cy'),(4,'di');
INSERT INTO follow VALUES (1,2),(1,3),(2,1),(3,1),(4,1),(2,3);
SELECT a.handle AS person, b.handle AS mutual_friend
FROM follow f1 JOIN follow f2 ON f2.follower_id = f1.followee_id AND f2.followee_id = f1.follower_id
JOIN user a ON a.id = f1.follower_id JOIN user b ON b.id = f1.followee_id WHERE f1.follower_id < f1.followee_id ORDER BY 1, 2;
SELECT u.handle, (SELECT COUNT(*) FROM follow f WHERE f.followee_id = u.id) AS followers, (SELECT COUNT(*) FROM follow f WHERE f.follower_id = u.id) AS following FROM user u ORDER BY followers DESC, u.handle;
