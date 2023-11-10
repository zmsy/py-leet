import unittest
from py_leet.palindromic_substrings import Solution

class TestPalindromicSubstrings(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.countSubstrings("abc"), 3)
    
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.countSubstrings("aaa"), 6)
