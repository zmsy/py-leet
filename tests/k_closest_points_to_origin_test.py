import unittest
from py_leet.k_closest_points_to_origin import Solution

class TestKClosestPointsToOrigin(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.kClosest([[1,3],[-2,2]], 1), [[-2, 2]])
