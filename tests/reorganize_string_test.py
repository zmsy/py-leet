import unittest
from py_leet.reorganize_string import Solution


class TestReorganizeString(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.reorganizeString("aab"), "aba")
