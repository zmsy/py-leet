import unittest
from py_leet.merge_intervals import Solution
from typing import List


class TestMergeIntervals(unittest.TestCase):
    def runOne(self, vals: List[List[int]], result: List[List[int]]):
        sol = Solution()
        self.assertEqual(sol.merge(vals), result)

    def test1(self):
        self.runOne([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]])

    def test2(self):
        self.runOne([[1, 4], [4, 5]], [[1, 5]])

    def test3(self):
        self.runOne([[4, 7], [1, 4]], [[1, 7]])

    def test4(self):
        self.runOne([[1, 4], [2, 3]], [[1, 4]])

    def test5(self):
        self.runOne([[1, 4], [0, 2], [3, 5]], [[0, 5]])
