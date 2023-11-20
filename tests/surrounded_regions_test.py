import unittest
from py_leet.surrounded_regions import Solution


class TestSurroundedRegions(unittest.TestCase):
    def test1(self):
        sol = Solution()
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "O", "X"],
            ["X", "O", "X", "X"],
        ]
        output = [
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "X", "X", "X"],
            ["X", "O", "X", "X"],
        ]
        sol.solve(board)
        self.assertEqual(board, output)

    def test2(self):
        sol = Solution()
        board = [
            ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
            ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
            ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
            ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
            ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
            ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
            ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
            ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
            ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
        ]
        output = [
            ["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
            ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
            ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["O", "X", "X", "X", "X", "X", "X", "X", "X", "O"],
            ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X", "O", "O"],
            ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
        ]
        sol.solve(board)
        self.assertEqual(board, output)
