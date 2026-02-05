from typing import Optional, List, Tuple
from . import TreeNode


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Create a queue of nodes to visit. For
        """
        if not root:
            return 0

        # tuple[node, x-axis]
        self.q: List[Tuple[Optional[TreeNode], int]] = [(root, 0)]

        max_width = 0  # we always have a root node
        while self.q:
            max_width = max(max_width, self.q[-1][1] - self.q[0][1] + 1)
            qlen = len(self.q)
            for _ in range(qlen):
                (val, i) = self.q.pop(0)
                if val:
                    if val.left:
                        # subtract one from the left
                        self.q.append((val.left, 2 * i))
                    if val.right:
                        # add one to the right
                        self.q.append((val.right, (2 * i) + 1))

        return max_width
