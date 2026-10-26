import unittest

def slugify(text):
    return "-".join(text.lower().split())

class TestSlugify(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
    def test_extra_spaces(self):
        self.assertEqual(slugify("  a   b "), "a-b")
    def test_empty(self):
        self.assertEqual(slugify(""), "")
    def test_type_error(self):
        with self.assertRaises(AttributeError):
            slugify(None)

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestSlugify)
import io
result = unittest.TextTestRunner(verbosity=0, stream=io.StringIO()).run(suite)
print("ran", result.testsRun, "failures", len(result.failures), "errors", len(result.errors))
