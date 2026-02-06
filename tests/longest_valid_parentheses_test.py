import unittest
from py_leet.longest_valid_parentheses import Solution


class TestLongestValidParentheses(unittest.TestCase):
    def test1(self):
        sol = Solution()
        result = sol.longestValidParentheses("(()")
        self.assertEqual(result, 2)

    def test2(self):
        sol = Solution()
        result = sol.longestValidParentheses(")()())")
        self.assertEqual(result, 4)

    def test3(self):
        sol = Solution()
        result = sol.longestValidParentheses("")
        self.assertEqual(result, 0)
