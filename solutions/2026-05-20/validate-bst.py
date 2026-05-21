"""Validate Binary Search Tree.

Recursively check every node against an open lower/upper bound interval. The
left subtree tightens the upper bound, the right subtree tightens the lower
bound. A node is valid only if its value lies strictly inside its bounds.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    # Time O(n), Space O(h) where h is the tree height.
    def check(
        node: Optional[TreeNode],
        low: Optional[int],
        high: Optional[int],
    ) -> bool:
        if node is None:
            return True
        if low is not None and node.val <= low:
            return False
        if high is not None and node.val >= high:
            return False
        return check(node.left, low, node.val) and check(node.right, node.val, high)

    return check(root, None, None)


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
    # Empty tree is valid.
    assert is_valid_bst(None) is True

    # Single node is valid.
    assert is_valid_bst(TreeNode(1)) is True

    # Simple valid BST: [2,1,3].
    assert is_valid_bst(_build([2, 1, 3])) is True

    # Invalid BST: root 5, but right subtree has 3.
    # Shape: 5 -> left=1, right=(4 -> left=3, right=6)
    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(invalid) is False

    # Duplicates not allowed (must be strict).
    dup = TreeNode(1, TreeNode(1))
    assert is_valid_bst(dup) is False

    # Negatives, valid.
    neg = TreeNode(-5, TreeNode(-10), TreeNode(0))
    assert is_valid_bst(neg) is True

    # Left-skewed strictly decreasing (valid).
    skew = TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))))
    assert is_valid_bst(skew) is True

    # Deep invalid: ancestor bound violation.
    # 10 -> left = (5 -> left=1, right=15). 15 > 10 so invalid.
    deep_invalid = TreeNode(10, TreeNode(5, TreeNode(1), TreeNode(15)), TreeNode(20))
    assert is_valid_bst(deep_invalid) is False


if __name__ == "__main__":
    _tests()
