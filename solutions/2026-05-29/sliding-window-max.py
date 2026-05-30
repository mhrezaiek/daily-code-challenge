"""Sliding Window Maximum.

Approach: maintain a monotonic-decreasing deque of indices. For each new index
we pop smaller values from the back (they can never be the max while the new
value is in the window) and drop the front index if it has fallen out of the
window. The front of the deque is always the current window's maximum.
Runs in O(n) time and O(k) extra space.
"""
from __future__ import annotations

from collections import deque
from typing import Deque, List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    if k <= 0:
        raise ValueError("k must be positive")
    n = len(nums)
    if n == 0 or k > n:
        return []
    dq: Deque[int] = deque()
    out: List[int] = []
    for i, x in enumerate(nums):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out


def _tests() -> None:
    # 1. Canonical LeetCode example.
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]

    # 2. k == 1 returns the input.
    assert max_sliding_window([4, 2, 12, 1], 1) == [4, 2, 12, 1]

    # 3. k equals length: one window containing the global max.
    assert max_sliding_window([2, 1, 5, 3, 4], 5) == [5]

    # 4. Empty input.
    assert max_sliding_window([], 3) == []

    # 5. Single element.
    assert max_sliding_window([9], 1) == [9]

    # 6. Strictly decreasing array: each window's max is its first element.
    assert max_sliding_window([9, 8, 7, 6, 5], 3) == [9, 8, 7]

    # 7. Negatives and duplicates.
    assert max_sliding_window([-7, -8, -7, -5, -5, -6], 2) == [-7, -7, -5, -5, -5]

    print("sliding-window-max: all tests passed")


if __name__ == "__main__":
    _tests()
