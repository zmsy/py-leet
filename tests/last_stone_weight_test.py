import unittest
from py_leet.last_stone_weight import Solution

class TestLastStoneWeight(unittest.TestCase):
    def test1(self):
        sol = Solution()
        self.assertEqual(sol.lastStoneWeight([2,7,4,1,8,1]), 1)
    
    def test2(self):
        sol = Solution()
        self.assertEqual(sol.lastStoneWeight([1]), 1)
