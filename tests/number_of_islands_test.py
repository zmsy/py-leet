import unittest
from typing import List
from py_leet.number_of_islands import Solution


class TestNumberOfIslands(unittest.TestCase):
    def runOne(self, grid: List[List[str]], result: int):
        sol = Solution()
        self.assertEqual(sol.numIslands(grid), result)

    def test1(self):
        grid = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        self.runOne(grid, 1)

    def test2(self):
        grid = [
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
        self.runOne(grid, 3)
