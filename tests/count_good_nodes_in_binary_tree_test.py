import unittest
from py_leet import tree_from_array
from py_leet.count_good_nodes_in_binary_tree import Solution


class TestCountGoodNodesInABinaryTree(unittest.TestCase):
    def test1(self):
        sol = Solution()
        root = tree_from_array([3, 1, 4, 3, None, 1, 5])
        self.assertEqual(sol.goodNodes(root), 4)  # type: ignore

    def test2(self):
        sol = Solution()
        root = tree_from_array([2, None, 4, 10, 8, None, None, 4])
        self.assertEqual(sol.goodNodes(root), 4)  # type: ignore
