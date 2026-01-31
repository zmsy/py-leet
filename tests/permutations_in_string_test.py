import unittest
from py_leet.permutations_in_string import Solution


class TestPermutationsInString(unittest.TestCase):
    """
    https://leetcode.com/problems/permutation-in-string/
    """

    sol = Solution()

    def test1(self):
        self.assertTrue(self.sol.checkInclusion("ab", "eidbaooo"))

    def test2(self):
        self.assertTrue(self.sol.checkInclusion("adc", "dcda"))
