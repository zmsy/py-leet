import unittest
from typing import List, Optional
from py_leet.binary_tree_right_side_view import Solution
from py_leet import tree_from_array


class TestBinaryTreeRightSideView(unittest.TestCase):
    def runOne(self, tree_input: List[Optional[int]], result: List[int]):
        sol = Solution()
        tree = tree_from_array(tree_input)
        self.assertEqual(sol.rightSideView(tree), result)

    def test1(self):
        self.runOne([1, 2, 3, None, 5, None, 4], [1, 3, 4])

    def test2(self):
        self.runOne([1, 2, 3, 4, None, None, None, 5], [1, 3, 4, 5])
