import unittest
from py_leet.longest_substring_without_repeating_characters import Solution


class TestLastStoneWeight(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("abcabcbb"), 3)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("bbbbb"), 1)

    def test3(self):
        sol = Solution()
        self.assertEqual(sol.lengthOfLongestSubstring("pwwkew"), 3)
