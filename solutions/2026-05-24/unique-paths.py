"""Unique Paths.

Count distinct paths from the top-left to the bottom-right of an m x n grid
when only right and down moves are allowed. Solved with bottom-up dynamic
programming using a single row of size n.
"""


def unique_paths(m: int, n: int) -> int:
    # Time: O(m * n), Space: O(n)
    if m <= 0 or n <= 0:
        return 0
    row = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[n - 1]


def _tests() -> None:
    assert unique_paths(1, 1) == 1
    assert unique_paths(2, 2) == 2
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(7, 3) == 28
    assert unique_paths(1, 10) == 1
    assert unique_paths(0, 5) == 0


if __name__ == "__main__":
    _tests()
