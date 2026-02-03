import unittest
from py_leet.peak_in_mountain_array import Solution


class TestPeakInMountainArray(unittest.TestCase):
    sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.peakIndexInMountainArray([0, 1, 0]), 1)

    def test2(self):
        self.assertEqual(self.sol.peakIndexInMountainArray([0, 2, 1, 0]), 1)

    def test3(self):
        self.assertEqual(self.sol.peakIndexInMountainArray([0, 10, 5, 2]), 1)

    def test4(self):
        self.assertEqual(
            self.sol.peakIndexInMountainArray([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]), 5
        )
