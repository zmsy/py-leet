import unittest
from py_leet.roman_to_int import Solution


class TestKClosestPointsToOrigin(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.romanToInt("III"), 3)
