CREATE TABLE room (id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE);
CREATE TABLE booking (id INTEGER PRIMARY KEY, room_id INT NOT NULL REFERENCES room(id), guest TEXT NOT NULL,
                      start_day TEXT NOT NULL, end_day TEXT NOT NULL, CHECK (end_day > start_day));
CREATE INDEX idx_booking_room_dates ON booking(room_id, start_day, end_day);
CREATE TRIGGER no_overlap BEFORE INSERT ON booking
BEGIN
  SELECT RAISE(ABORT, 'room already booked for those dates')
  WHERE EXISTS (SELECT 1 FROM booking b WHERE b.room_id = NEW.room_id AND b.start_day < NEW.end_day AND NEW.start_day < b.end_day);
END;
INSERT INTO room VALUES (1,'Sea view'),(2,'Garden');
INSERT INTO booking VALUES (1,1,'Ana','2024-05-01','2024-05-05'),(2,1,'Bo','2024-05-05','2024-05-08'),(3,2,'Cy','2024-05-02','2024-05-04');
INSERT INTO booking VALUES (4,1,'Di','2024-05-04','2024-05-06');
