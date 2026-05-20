"""
Search in Rotated Sorted Array.

Approach: a single-pass modified binary search. At each step, exactly one
half of the window (left..mid or mid..right) is sorted; we decide which by
comparing nums[left] with nums[mid]. We then check whether the target lies
inside that sorted half — if so, recurse there; otherwise recurse the other
half. Runs in O(log n) time and O(1) space, assuming all values are distinct.
"""
from __future__ import annotations

from typing import List


def search(nums: List[int], target: int) -> int:
    """Return the index of target in a rotated sorted array of distinct ints, or -1."""
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:
            # Left half [left..mid] is sorted.
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half [mid..right] is sorted.
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def _tests() -> None:
    # 1. Target present in the rotated half.
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4

    # 2. Target absent.
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1

    # 3. Empty array.
    assert search([], 5) == -1

    # 4. Single element, present.
    assert search([1], 1) == 0

    # 5. Single element, absent.
    assert search([1], 0) == -1

    # 6. Not rotated at all, target at the end.
    assert search([1, 2, 3, 4, 5], 5) == 4

    # 7. Target equals pivot (left endpoint after rotation).
    assert search([6, 7, 0, 1, 2, 4, 5], 6) == 0


if __name__ == "__main__":
    _tests()
    print("search-rotated-sorted: all tests passed")
