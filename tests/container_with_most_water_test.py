import unittest
from py_leet.container_with_most_water import Solution


class TestContainerWithMostWater(unittest.TestCase):
    """ """

    sol = Solution()

    def test1(self):
        result = self.sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
        self.assertEqual(result, 49)

    def test2(self):
        result = self.sol.maxArea([1, 1])
        self.assertEqual(result, 1)
