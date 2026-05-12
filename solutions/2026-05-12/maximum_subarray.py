"""
Maximum Subarray (LC 53)
------------------------
Given an integer array nums, find the contiguous subarray (containing at
least one number) which has the largest sum and return its sum.

Approach: Kadane's algorithm.
    Maintain `cur` = best subarray sum ending at i.
    cur = max(nums[i], cur + nums[i])     # extend or restart
    best = max(best, cur)

Complexity: O(n) time, O(1) extra space.
"""
from __future__ import annotations
from typing import List


def max_sub_array(nums: List[int]) -> int:
    if not nums:
        raise ValueError("nums must be non-empty")
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


# Variant that also returns the (start, end) indices — useful in interviews
# when the follow-up is "which subarray?".
def max_sub_array_with_indices(nums: List[int]) -> tuple[int, int, int]:
    best = cur = nums[0]
    best_l = best_r = 0
    cur_l = 0
    for i in range(1, len(nums)):
        if cur + nums[i] < nums[i]:
            cur = nums[i]
            cur_l = i
        else:
            cur += nums[i]
        if cur > best:
            best = cur
            best_l, best_r = cur_l, i
    return best, best_l, best_r


def _tests() -> None:
    cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),   # subarray [4,-1,2,1]
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        ([-1, -2, -3], -1),                      # all negative → least negative
        ([0, 0, 0], 0),
        ([-2, -1], -1),
    ]
    for nums, expected in cases:
        got = max_sub_array(nums)
        assert got == expected, f"max_sub_array({nums}) = {got}, want {expected}"
    # Spot-check the indexed version against the simple version.
    s, l, r = max_sub_array_with_indices([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    assert s == 6 and (l, r) == (3, 6), (s, l, r)
    print("maximum_subarray: all tests passed")


if __name__ == "__main__":
    _tests()
