"""Maximum Depth of Binary Tree.

Approach: recursive DFS. The depth of an empty tree is 0; otherwise it is
1 + the max of the left and right subtree depths. Runs in O(n) time and
O(h) stack space where h is the tree height.
"""
from __future__ import annotations

from typing import List, Optional


class TreeNode:
    __slots__ = ("val", "left", "right")

    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def _build(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a level-order list with None for missing nodes."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue: List[TreeNode] = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])  # type: ignore[arg-type]
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])  # type: ignore[arg-type]
            queue.append(node.right)
        i += 1
    return root


def _tests() -> None:
    # 1. Empty tree.
    assert max_depth(None) == 0

    # 2. Single node.
    assert max_depth(TreeNode(1)) == 1

    # 3. Canonical balanced example: [3,9,20,null,null,15,7] -> depth 3.
    assert max_depth(_build([3, 9, 20, None, None, 15, 7])) == 3

    # 4. Left-skewed tree of depth 4.
    assert max_depth(_build([1, 2, None, 3, None, 4, None])) == 4

    # 5. Right-skewed tree of depth 4.
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert max_depth(root) == 4

    # 6. Perfectly balanced of depth 3.
    assert max_depth(_build([1, 2, 3, 4, 5, 6, 7])) == 3

    # 7. Unbalanced where left side is deeper.
    assert max_depth(_build([1, 2, 3, 4, None, None, None, 5])) == 4

    print("max-depth-bt: all tests passed")


if __name__ == "__main__":
    _tests()
