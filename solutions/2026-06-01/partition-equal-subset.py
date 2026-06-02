"""Partition Equal Subset Sum.

Determine whether a list of positive integers can be split into two
subsets with equal sum. This reduces to a 0/1 subset-sum problem: does
some subset sum to total // 2? Solved with a 1-D boolean DP iterated
in reverse to avoid reusing items.
"""

from typing import List


def can_partition(nums: List[int]) -> bool:
    # Time O(n * target), space O(target) where target = sum(nums) // 2.
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2
    reachable = [False] * (target + 1)
    reachable[0] = True
    for num in nums:
        if num > target:
            return False
        for s in range(target, num - 1, -1):
            if reachable[s - num]:
                reachable[s] = True
        if reachable[target]:
            return True
    return reachable[target]


def _tests() -> None:
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([1, 1]) is True
    assert can_partition([2]) is False
    assert can_partition([1, 2, 5]) is False
    assert can_partition([3, 3, 3, 4, 5]) is True
    assert can_partition([100]) is False
    assert can_partition([2, 2, 2, 2]) is True


if __name__ == "__main__":
    _tests()
    print("partition-equal-subset: all tests passed")
