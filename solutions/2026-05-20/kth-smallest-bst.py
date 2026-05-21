"""Kth Smallest Element in a BST.

Perform an iterative inorder traversal using an explicit stack. Because an
inorder walk of a BST visits nodes in ascending order, the k-th popped node
is the answer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    # Time O(h + k), Space O(h) where h is tree height.
    if root is None or k <= 0:
        raise ValueError("root must be non-empty and k must be positive")

    stack: List[TreeNode] = []
    node: Optional[TreeNode] = root
    remaining = k
    while stack or node is not None:
        while node is not None:
            stack.append(node)
            node = node.left
        node = stack.pop()
        remaining -= 1
        if remaining == 0:
            return node.val
        node = node.right

    raise ValueError("k is larger than the number of nodes in the tree")


def _build(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None
    root = TreeNode(values[0])  # type: ignore[arg-type]
    queue: List[TreeNode] = [root]
    i = 1
    while queue and i < len(values):
        current = queue.pop(0)
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])  # type: ignore[arg-type]
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])  # type: ignore[arg-type]
            queue.append(current.right)
        i += 1
    return root


def _tests() -> None:
    # Single node tree.
    assert kth_smallest(TreeNode(7), 1) == 7

    # Balanced BST: [3,1,4,null,2], inorder = [1,2,3,4].
    root = _build([3, 1, 4, None, 2])
    assert kth_smallest(root, 1) == 1
    assert kth_smallest(root, 2) == 2
    assert kth_smallest(root, 3) == 3
    assert kth_smallest(root, 4) == 4

    # Left-skewed tree: 5 -> 4 -> 3 -> 2 -> 1.
    skew = TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))))
    assert kth_smallest(skew, 1) == 1
    assert kth_smallest(skew, 5) == 5

    # Right-skewed tree: 1 -> 2 -> 3.
    right_skew = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert kth_smallest(right_skew, 2) == 2

    # Negative values.
    neg = TreeNode(-5, TreeNode(-10), TreeNode(0))
    assert kth_smallest(neg, 1) == -10
    assert kth_smallest(neg, 3) == 0

    # Invalid k (too large) raises.
    try:
        kth_smallest(TreeNode(1), 5)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for k larger than tree")

    # Invalid arguments raise.
    try:
        kth_smallest(None, 1)
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError for empty tree")


if __name__ == "__main__":
    _tests()
