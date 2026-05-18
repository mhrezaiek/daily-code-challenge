"""
Lowest Common Ancestor of a Binary Tree.

Approach: post-order recursion. At each node, search left and right subtrees
for either of the two target nodes. If both sides return non-None, the current
node is the LCA. Otherwise propagate the single non-None side upward. Runs in
O(n) time and O(h) auxiliary stack space, where h is the height of the tree.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TreeNode:
    val: int
    left: Optional["TreeNode"] = field(default=None)
    right: Optional["TreeNode"] = field(default=None)


def lowest_common_ancestor(
    root: Optional[TreeNode],
    p: TreeNode,
    q: TreeNode,
) -> Optional[TreeNode]:
    """Return the lowest common ancestor of nodes ``p`` and ``q`` in ``root``.

    Assumes ``p`` and ``q`` both exist in the tree rooted at ``root`` and that
    node identity (``is``) — not value equality — defines a match, matching
    the LeetCode contract.
    """
    # Time: O(n) — every node is visited at most once.
    # Space: O(h) — recursion stack proportional to tree height.
    if root is None or root is p or root is q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    if left is not None and right is not None:
        return root
    return left if left is not None else right


def _build_sample_tree() -> tuple[TreeNode, dict[int, TreeNode]]:
    """Build the canonical LeetCode example tree.

            3
           / \\
          5   1
         / \\ / \\
        6  2 0  8
          / \\
         7   4
    """
    nodes = {v: TreeNode(v) for v in (3, 5, 1, 6, 2, 0, 8, 7, 4)}
    nodes[3].left, nodes[3].right = nodes[5], nodes[1]
    nodes[5].left, nodes[5].right = nodes[6], nodes[2]
    nodes[1].left, nodes[1].right = nodes[0], nodes[8]
    nodes[2].left, nodes[2].right = nodes[7], nodes[4]
    return nodes[3], nodes


def _tests() -> None:
    root, nodes = _build_sample_tree()

    # 1. Classic LeetCode case: LCA(5, 1) == 3.
    assert lowest_common_ancestor(root, nodes[5], nodes[1]) is nodes[3]

    # 2. One node is an ancestor of the other: LCA(5, 4) == 5.
    assert lowest_common_ancestor(root, nodes[5], nodes[4]) is nodes[5]

    # 3. Both descendants on the same deep subtree: LCA(7, 4) == 2.
    assert lowest_common_ancestor(root, nodes[7], nodes[4]) is nodes[2]

    # 4. Across the root from very different subtrees: LCA(6, 8) == 3.
    assert lowest_common_ancestor(root, nodes[6], nodes[8]) is nodes[3]

    # 5. p == q: any node is its own ancestor.
    assert lowest_common_ancestor(root, nodes[7], nodes[7]) is nodes[7]

    # 6. Two-node tree, root is parent of leaf.
    a, b = TreeNode(1), TreeNode(2)
    a.left = b
    assert lowest_common_ancestor(a, a, b) is a

    # 7. Single-node tree.
    only = TreeNode(42)
    assert lowest_common_ancestor(only, only, only) is only

    print("lowest-common-ancestor: all tests passed")


if __name__ == "__main__":
    _tests()
