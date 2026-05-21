"""Longest Consecutive Sequence.

Insert all values into a set, then for each value that has no predecessor in
the set (i.e. value - 1 is absent), walk forward counting consecutive
neighbors. Each element is visited at most twice, yielding O(n) overall.
"""

from __future__ import annotations

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    # Time O(n), Space O(n).
    if not nums:
        return 0

    seen = set(nums)
    best = 0
    for value in seen:
        if value - 1 in seen:
            continue
        current = value
        length = 1
        while current + 1 in seen:
            current += 1
            length += 1
        if length > best:
            best = length
    return best


def _tests() -> None:
    # Empty input.
    assert longest_consecutive([]) == 0

    # Single element.
    assert longest_consecutive([42]) == 1

    # Classic example: [100,4,200,1,3,2] -> sequence 1..4 of length 4.
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4

    # Duplicates should not inflate the length.
    assert longest_consecutive([1, 2, 2, 3, 3, 3, 4]) == 4

    # Negatives and zero.
    assert longest_consecutive([-3, -2, -1, 0, 1]) == 5

    # All identical values.
    assert longest_consecutive([7, 7, 7, 7]) == 1

    # Disjoint runs: [10,11,12] and [1,2]. Longest is 3.
    assert longest_consecutive([1, 2, 10, 11, 12]) == 3

    # Large gap, isolated points.
    assert longest_consecutive([1, 1000000, -1000000]) == 1


if __name__ == "__main__":
    _tests()
