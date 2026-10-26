import sqlite3, unittest, io

def create_user(con, name):
    with con:
        cur = con.execute("INSERT INTO users (name) VALUES (?)", (name,))
    return cur.lastrowid

def count_users(con):
    return con.execute("SELECT COUNT(*) FROM users").fetchone()[0]

class UserRepoTest(unittest.TestCase):
    def setUp(self):                                  # fresh database for every test
        self.con = sqlite3.connect(":memory:")
        self.con.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT UNIQUE NOT NULL)")
    def tearDown(self):
        self.con.close()
    def test_create(self):
        uid = create_user(self.con, "ada")
        self.assertEqual(uid, 1)
        self.assertEqual(count_users(self.con), 1)
    def test_unique_name(self):
        create_user(self.con, "ada")
        with self.assertRaises(sqlite3.IntegrityError):
            create_user(self.con, "ada")
        self.assertEqual(count_users(self.con), 1)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(UserRepoTest)
res = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
print("tests run:", res.testsRun, "failures:", len(res.failures) + len(res.errors))
