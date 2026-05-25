"""House Robber.

Choose a subset of non-adjacent houses that maximizes total loot. Solved with
constant-space dynamic programming: at each house, the best is either skipping
it (carry previous best) or taking it plus the best two houses back.
"""

from typing import List


def rob(nums: List[int]) -> int:
    # Time: O(n), Space: O(1)
    prev_two = 0
    prev_one = 0
    for amount in nums:
        prev_two, prev_one = prev_one, max(prev_one, prev_two + amount)
    return prev_one


def _tests() -> None:
    assert rob([]) == 0
    assert rob([5]) == 5
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 1, 1, 2]) == 4
    assert rob([10, 10, 10]) == 20
    assert rob([0, 0, 0, 0]) == 0


if __name__ == "__main__":
    _tests()
