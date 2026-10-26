CREATE TABLE room (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE booking (id INTEGER PRIMARY KEY, room_id INT, start_day TEXT, end_day TEXT);
INSERT INTO room VALUES (1,'Sea view'),(2,'Garden'),(3,'Attic');
INSERT INTO booking VALUES (1,1,'2024-05-01','2024-05-05'),(2,2,'2024-05-02','2024-05-04'),(3,3,'2024-04-20','2024-04-25');
SELECT r.name AS free_room FROM room r
WHERE NOT EXISTS (SELECT 1 FROM booking b WHERE b.room_id = r.id AND b.start_day < '2024-05-04' AND '2024-05-03' < b.end_day)
ORDER BY r.name;
