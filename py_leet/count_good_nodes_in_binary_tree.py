from py_leet import TreeNode
from typing import Optional


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good_nodes = 0

        def recurse(node: Optional[TreeNode], val: int) -> None:
            nonlocal good_nodes
            if node is None:
                return

            if val <= node.val:
                good_nodes += 1

            recurse(node.left, max(val, node.val))
            recurse(node.right, max(val, node.val))

        recurse(root, 0)
        return good_nodes
