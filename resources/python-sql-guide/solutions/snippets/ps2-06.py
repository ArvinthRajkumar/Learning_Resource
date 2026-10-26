import sqlite3, unittest
def add_user(db, email):
    try:
        db.execute("INSERT INTO users(email) VALUES (?)", (email.strip().lower(),)); return True
    except sqlite3.IntegrityError:
        return False
class AddUserTests(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE)")
    def test_adds_and_normalises(self):
        self.assertTrue(add_user(self.db, "  Ada@Example.COM "))
        self.assertEqual(self.db.execute("SELECT email FROM users").fetchall(), [("ada@example.com",)])
    def test_rejects_duplicates_case_insensitively(self):
        add_user(self.db, "a@x.com")
        self.assertFalse(add_user(self.db, "A@X.com"))
    def test_rejects_null(self):
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.execute("INSERT INTO users(email) VALUES (NULL)")
suite = unittest.defaultTestLoader.loadTestsFromTestCase(AddUserTests)
import io
result = unittest.TextTestRunner(stream=io.StringIO(), verbosity=0).run(suite)
print("tests run:", result.testsRun, "| failures:", len(result.failures), "| errors:", len(result.errors))
