"""Kth Largest Element in an Array.

Approach: maintain a min-heap of size k while scanning the array. The root is
always the smallest of the k largest values seen so far, so after a full pass
the root is the kth largest element overall. Runs in O(n log k) time and
O(k) extra space.
"""
from __future__ import annotations

import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    if k <= 0 or k > len(nums):
        raise ValueError("k must satisfy 1 <= k <= len(nums)")
    heap: List[int] = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]


def _tests() -> None:
    # 1. Canonical example.
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

    # 2. Larger array with duplicates.
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    # 3. Single element, k=1.
    assert find_kth_largest([7], 1) == 7

    # 4. k equals length returns the minimum.
    assert find_kth_largest([3, 1, 2], 3) == 1

    # 5. k=1 returns the maximum.
    assert find_kth_largest([3, 1, 2, 9, 4], 1) == 9

    # 6. Negative numbers handled correctly.
    assert find_kth_largest([-1, -2, -3, -4], 2) == -2

    # 7. All duplicates: every kth largest is the same value.
    assert find_kth_largest([5, 5, 5, 5], 3) == 5

    print("kth-largest: all tests passed")


if __name__ == "__main__":
    _tests()
