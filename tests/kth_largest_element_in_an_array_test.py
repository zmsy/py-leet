import unittest
from py_leet.kth_largest_element_in_an_array import Solution
from typing import List


class TestMergeIntervals(unittest.TestCase):
    def runOne(self, vals: List[int], k: int, result: int):
        sol = Solution()
        self.assertEqual(sol.findKthLargest(vals, k), result)

    def test1(self):
        self.runOne([3, 2, 1, 5, 6, 4], 2, 5)
