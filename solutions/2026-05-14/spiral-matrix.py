"""Spiral Matrix.

Given an ``m x n`` matrix, return all of its elements in spiral order —
left across the top row, down the right column, right-to-left across the
bottom, then up the left column, and inward. We track four shrinking
boundaries (``top``, ``bottom``, ``left``, ``right``) and walk along
whichever edge has not yet been consumed, contracting after each pass.
"""
from __future__ import annotations

from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    """Return the elements of ``matrix`` in clockwise spiral order.

    Time:  O(m * n) — each cell is visited exactly once.
    Space: O(1) auxiliary (output not counted).
    """
    if not matrix or not matrix[0]:
        return []

    result: list[int] = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # Top row, left -> right.
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        # Right column, top -> bottom.
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        # Bottom row, right -> left (only if a distinct row remains).
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        # Left column, bottom -> top (only if a distinct column remains).
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1

    return result


def _tests() -> None:
    # 3x3 — canonical example.
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # 3x4 — wider than tall.
    assert spiral_order(
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    ) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    # Single row.
    assert spiral_order([[1, 2, 3, 4, 5]]) == [1, 2, 3, 4, 5]

    # Single column.
    assert spiral_order([[1], [2], [3], [4]]) == [1, 2, 3, 4]

    # Single cell.
    assert spiral_order([[42]]) == [42]

    # Empty matrix.
    assert spiral_order([]) == []

    # 4x4 — exercises the full inward spiral with an inner ring.
    assert spiral_order(
        [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7],
        ]
    ) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


if __name__ == "__main__":
    _tests()
