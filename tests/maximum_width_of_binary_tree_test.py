import unittest
from py_leet.maximum_width_of_binary_tree import Solution
from py_leet import tree_from_array


class TestMaximumWidthOfBinaryTreet(unittest.TestCase):
    def test1(self):
        sol = Solution()
        tree = tree_from_array([1, 3, 2, 5, 3, None, 9])
        self.assertEqual(sol.widthOfBinaryTree(tree), 4)

    def test2(self):
        sol = Solution()
        tree = tree_from_array([1, 3, 2, 5, None, None, 9, 6, None, 7])
        self.assertEqual(sol.widthOfBinaryTree(tree), 7)
