"""Longest Increasing Subsequence.

Return the length of the longest strictly increasing subsequence of an
integer array. Uses patience-sorting / binary-search: maintain ``tails``
where ``tails[i]`` is the smallest possible tail of any increasing
subsequence of length ``i + 1``. For each value we replace the first
tail >= value (or append), giving O(n log n) time.
"""

from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    # Time: O(n log n), Space: O(n)
    tails: List[int] = []
    for x in nums:
        idx = bisect_left(tails, x)
        if idx == len(tails):
            tails.append(x)
        else:
            tails[idx] = x
    return len(tails)


def _tests() -> None:
    assert length_of_lis([]) == 0
    assert length_of_lis([5]) == 1
    assert length_of_lis([7, 7, 7, 7]) == 1
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([-5, -3, -4, -2, -1]) == 4
    assert length_of_lis([4, 3, 2, 1]) == 1


if __name__ == "__main__":
    _tests()
