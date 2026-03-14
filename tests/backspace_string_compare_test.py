import unittest
from py_leet.backspace_string_compare import Solution


class TestBackspaceStringCompare(unittest.TestCase):
    def runOne(self, a: str, b: str, result: bool):
        sol = Solution()
        self.assertEqual(
            sol.backspaceCompare(
                a,
                b,
            ),
            result,
        )

    def test1(self):
        self.runOne("ab#c", "ad#c", True)

    def test2(self):
        self.runOne("ab##", "c#d#", True)

    def test3(self):
        self.runOne("a#c", "b", False)

    def test4(self):
        self.runOne("y#fo##f", "y#f#o##f", True)
