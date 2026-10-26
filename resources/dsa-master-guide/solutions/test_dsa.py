"""Run every example in the DSA guide.

Each solution file under solutions/ is executed (with its prelude when it needs
ListNode or TreeNode helpers) and every recorded call must return the recorded
value. Template and snippet files are compiled, and run when they stand alone.

Usage:  python3 resources/dsa-master-guide/solutions/test_dsa.py
"""
import contextlib
import io
import pathlib
import sys
import unittest

from dsa_cases import CASES, SNIPPETS

HERE = pathlib.Path(__file__).resolve().parent


def load(rel, prelude=None):
    ns = {"__name__": "guide"}
    if prelude and prelude != "compile-only":
        src = (HERE / "preludes" / ("%s.py" % prelude)).read_text(encoding="utf8")
        exec(compile(src, prelude, "exec"), ns)
    src = (HERE / rel).read_text(encoding="utf8")
    with contextlib.redirect_stdout(io.StringIO()):   # some examples print while they run
        exec(compile(src, rel, "exec"), ns)
    return ns


class GuideExamples(unittest.TestCase):
    def test_cases(self):
        total = 0
        for rel, (prelude, pairs) in sorted(CASES.items()):
            ns = load(rel, prelude)
            for call, expected in pairs:
                got = eval(call, ns)
                self.assertEqual(got, expected, "%s: %s" % (rel, call))
                total += 1
        print("checked %d calls in %d files" % (total, len(CASES)))

    def test_snippets_and_templates(self):
        for rel, prelude in SNIPPETS:
            if prelude == "compile-only":
                compile((HERE / rel).read_text(encoding="utf8"), rel, "exec")
            else:
                load(rel, prelude)
        for f in sorted((HERE / "patterns").glob("*.py")):
            compile(f.read_text(encoding="utf8"), f.name, "exec")


if __name__ == "__main__":
    sys.path.insert(0, str(HERE))
    unittest.main(verbosity=0)
