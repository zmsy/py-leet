import unittest
from py_leet.shortest_path_to_get_food import Solution


class TestShortestPathToGetFood(unittest.TestCase):
    def test1(self):
        sol = Solution()
        matrix = [
            ["X", "X", "X", "X", "X", "X"],
            ["X", "*", "O", "O", "O", "X"],
            ["X", "O", "O", "#", "O", "X"],
            ["X", "X", "X", "X", "X", "X"],
        ]
        self.assertEqual(sol.getFood(matrix), 3)
