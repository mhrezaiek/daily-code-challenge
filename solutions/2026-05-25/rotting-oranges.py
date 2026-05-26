"""Rotting Oranges.

Multi-source BFS from every initially rotten orange. Each BFS layer represents
one minute of rotting; we return the layer count after all fresh oranges are
reached, or -1 if any fresh orange remains unreachable.
"""

from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    if not grid or not grid[0]:
        return 0
    rows, cols = len(grid), len(grid[0])
    queue: deque = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c, 0))
            elif grid[r][c] == 1:
                fresh += 1

    minutes = 0
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while queue:
        r, c, t = queue.popleft()
        minutes = t
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                fresh -= 1
                queue.append((nr, nc, t + 1))

    return -1 if fresh > 0 else minutes


# Time: O(rows * cols). Space: O(rows * cols) for the queue.


def _tests() -> None:
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0
    assert oranges_rotting([[0]]) == 0
    assert oranges_rotting([[1]]) == -1
    assert oranges_rotting([[2]]) == 0
    assert oranges_rotting([[2, 2], [1, 1], [0, 1], [2, 1]]) == 2


if __name__ == "__main__":
    _tests()
