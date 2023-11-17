import unittest
from py_leet.min_remove_to_make_valid import Solution


class TestMinRemoveToMakeValid(unittest.TestCase):
    def test1(self):
        sol = Solution()
        arg = "lee(t(c)o)de)"
        output = "lee(t(c)o)de"
        self.assertEqual(sol.minRemoveToMakeValid(arg), output)

    def test2(self):
        sol = Solution()
        arg = "a)b(c)d"
        output = "ab(c)d"
        self.assertEqual(sol.minRemoveToMakeValid(arg), output)

    def test3(self):
        sol = Solution()
        arg = "))(("
        output = ""
        self.assertEqual(sol.minRemoveToMakeValid(arg), output)
