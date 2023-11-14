from __future__ import annotations
from typing import Optional, List


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional[TreeNode] = None,
        right: Optional[TreeNode] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


def tree_from_array(values: Optional[List[int | None]]) -> Optional[TreeNode]:
    if not values or not values[0]:
        return None

    root = TreeNode(values[0])
    queue: List[Optional[TreeNode]] = [root]

    i = 1
    while i < len(values):
        current = queue.pop(0)
        if current is None:
            break

        left_val = values[i]
        if left_val is not None:
            current.left = TreeNode(left_val)
            queue.append(current.left)
        i += 1

        right_val = values[i] if i < len(values) else None
        if right_val is not None:
            current.right = TreeNode(right_val)
            queue.append(current.right)
        i += 1

    return root
