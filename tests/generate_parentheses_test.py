import unittest
from py_leet.generate_parentheses import Solution


class TestDecodeWays(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(
            sol.generateParenthesis(3),
            ["((()))", "(()())", "(())()", "()(())", "()()()"],
        )

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.generateParenthesis(1), ["()"])
