"""Search a 2D Matrix.

Determine whether a target value exists in a row-sorted matrix where each
row's first value is greater than the previous row's last value. Treats the
matrix as a flattened sorted array and runs a single binary search.
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # Time: O(log(m * n)), Space: O(1)
    if not matrix or not matrix[0]:
        return False
    rows = len(matrix)
    cols = len(matrix[0])
    lo = 0
    hi = rows * cols - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        value = matrix[mid // cols][mid % cols]
        if value == target:
            return True
        if value < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


def _tests() -> None:
    assert search_matrix([], 1) is False
    assert search_matrix([[]], 1) is False
    assert search_matrix([[1]], 1) is True
    assert search_matrix([[1]], 2) is False
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(matrix, 3) is True
    assert search_matrix(matrix, 13) is False
    assert search_matrix(matrix, 60) is True
    assert search_matrix(matrix, 1) is True
    assert search_matrix([[-5, -3, 0], [2, 4, 6]], -3) is True


if __name__ == "__main__":
    _tests()
