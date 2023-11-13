import unittest
from py_leet.evaluate_reverse_polish_notation import Solution


class TestEvaluateReversePolishNotation(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.evalRPN(["2", "1", "+", "3", "*"]), 9)

    def test2(self):
        sol = Solution()
        self.assertEqual(sol.evalRPN(["4", "13", "5", "/", "+"]), 6)

    def test3(self):
        sol = Solution()
        self.assertEqual(
            sol.evalRPN(
                ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
            ),
            22,
        )
