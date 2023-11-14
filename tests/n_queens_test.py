import unittest
from py_leet.n_queens import Solution


class TestNQueens(unittest.TestCase):
    def test1(self):
        sol = Solution()
        result = sol.solveNQueens(4)
        self.assertIn([".Q..", "...Q", "Q...", "..Q."], result)
        self.assertIn(["..Q.", "Q...", "...Q", ".Q.."], result)
