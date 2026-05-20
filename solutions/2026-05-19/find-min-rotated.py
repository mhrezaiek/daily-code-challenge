"""
Find Minimum in Rotated Sorted Array.

Approach: a modified binary search. In a rotated sorted array with distinct
values, the minimum sits at the unique inflection point. Compare the
midpoint to the right boundary: if nums[mid] > nums[right], the inflection
lies strictly to the right of mid; otherwise it is at mid or to its left.
This runs in O(log n) time and O(1) extra space.
"""
from __future__ import annotations

from typing import List


def find_min(nums: List[int]) -> int:
    """Return the smallest value in a (possibly) rotated sorted array of distinct ints."""
    if not nums:
        raise ValueError("find_min requires a non-empty array")

    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            # Minimum is strictly right of mid.
            left = mid + 1
        else:
            # Minimum is at mid or to the left.
            right = mid
    return nums[left]


def _tests() -> None:
    # 1. Classic rotated array.
    assert find_min([3, 4, 5, 1, 2]) == 1

    # 2. Larger rotation example.
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0

    # 3. Not rotated at all -> min is the first element.
    assert find_min([1, 2, 3, 4, 5]) == 1

    # 4. Single element.
    assert find_min([42]) == 42

    # 5. Two elements, rotated.
    assert find_min([2, 1]) == 1

    # 6. Two elements, not rotated.
    assert find_min([1, 2]) == 1

    # 7. Rotation by exactly one position from the end.
    assert find_min([5, 1, 2, 3, 4]) == 1


if __name__ == "__main__":
    _tests()
    print("find-min-rotated: all tests passed")
