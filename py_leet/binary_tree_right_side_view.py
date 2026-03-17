from . import TreeNode
from typing import Optional, List
from dataclasses import dataclass


@dataclass
class QueueEntry:
    node: TreeNode
    level: int


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # every entry is the treenode and its specific level
        queue: List[QueueEntry] = [QueueEntry(root, 0)]
        view: List[int] = []

        # general algorithm
        # bfs through the tree, and at every level keep track of the right-most
        # value
        while queue:
            level = queue[0].level

            # initialize a variable that tracks the right-most entry
            right = queue[0].node.val

            # loop until this level is completed
            while queue and queue[0].level == level:
                entry = queue.pop(0)  # take from the start of the array = bfs
                right = entry.node.val

                # always traverse left-side first for left-to-right side
                if entry.node.left:
                    queue.append(QueueEntry(entry.node.left, level + 1))
                if entry.node.right:
                    queue.append(QueueEntry(entry.node.right, level + 1))

            # now that we're done looping through this level, append the current
            # 'right' val to represent the right-most value
            view.append(right)

        return view
