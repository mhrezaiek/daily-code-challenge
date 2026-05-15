"""Two Sum.

Given an array of integers ``nums`` and an integer ``target``, return the
indices of the two numbers that add up to ``target``. We sweep the array
once and keep a hash map of ``value -> index`` of every element we have
already seen, so for each new element we can ask in O(1) whether its
complement (``target - num``) has shown up before.
"""
from __future__ import annotations

from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """Return the indices of the two numbers in ``nums`` that sum to ``target``.

    Time:  O(n) — single pass over ``nums``.
    Space: O(n) — hash map storing seen values.
    """
    seen: dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # problem guarantees one solution; defensive fallback


def _tests() -> None:
    # Canonical example: standard small input.
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

    # Target uses two non-adjacent elements.
    assert two_sum([3, 2, 4], 6) == [1, 2]

    # Two equal elements that together hit the target.
    assert two_sum([3, 3], 6) == [0, 1]

    # Negative numbers in the array.
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]

    # Solution involves the last element, forcing a full pass.
    assert two_sum([1, 5, 7, -1, 5], 10) == [2, 4]

    # Mix of negatives and positives that sum to a negative target.
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

    # Larger array — verify the hash-map lookup still works correctly.
    assert two_sum(list(range(1, 1001)), 1999) == [998, 999]


if __name__ == "__main__":
    _tests()
