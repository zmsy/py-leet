from __future__ import annotations
from typing import Optional, List, Any, Deque
from collections import deque


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


def print_matrix(vals: List[List[Any]]) -> None:
    print("\n" + "\n".join("".join(map(str, row)) for row in vals))


def assert_equals(left: Any, right: Any) -> None:
    if left != right:
        raise AssertionError(f"assertEquals error: {left} does not equal {right}.")


# ListNode class definition for iterating.
class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# Graph node for graph problems.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# Initialize a graph from an adjacency list.
def graph_from_adjacency_list(adjacency_list: List[List[int]]) -> List[Node]:
    nodes = [Node(i + 1) for i in range(len(adjacency_list))]

    for i, neighbors in enumerate(adjacency_list):
        for neighbor_index in neighbors:
            nodes[i].neighbors.append(nodes[neighbor_index - 1])

    return nodes


# Derive the adjacency list from a graph.
def adjacency_list_from_graph(graph: List[Node]) -> List[List[int]]:
    return [[neighbor.val for neighbor in node.neighbors] for node in graph]


# Initialize a linked list from an array of values.
def linked_list_from_array(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def array_from_linked_list(node: Optional[ListNode]) -> List[int]:
    result: List[int] = []
    while node:
        result.append(node.val)
        node = node.next
    return result


def array_from_tree(root: Optional[TreeNode]) -> List[Optional[int]]:
    if not root:
        return []

    result: List[Optional[int]] = []
    queue: Deque[Optional[TreeNode]] = deque([root])

    while queue:
        current = queue.popleft()
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)

    while result and result[-1] is None:
        result.pop()

    return result


def tree_diagram_string(
    root: Optional[TreeNode],
    prefix: str = "",
    is_left: bool = True,
    result: str = "",
) -> str:
    if not root:
        return result

    if root.right:
        result = tree_diagram_string(
            root.right,
            prefix + ("│   " if is_left else "    "),
            False,
            result,
        )

    result += prefix + ("└── " if is_left else "┌── ") + str(root.val) + "\n"

    if root.left:
        result = tree_diagram_string(
            root.left,
            prefix + ("    " if is_left else "│   "),
            True,
            result,
        )

    return result
