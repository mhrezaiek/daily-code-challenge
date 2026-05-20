"""
Container With Most Water.

Approach: two pointers converging from both ends of the height array.
At each step the area is bounded by the shorter line, so we record the
current area and then move the shorter pointer inward — moving the taller
pointer could only shrink the width without ever raising the height
ceiling, so it cannot yield a larger area. Runs in O(n) time and O(1) space.
"""
from __future__ import annotations

from typing import List


def max_area(height: List[int]) -> int:
    """Return the maximum water volume between any two lines in the input."""
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        h = min(height[left], height[right])
        best = max(best, h * (right - left))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


def _tests() -> None:
    # 1. Canonical example from the problem statement.
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49

    # 2. Two-element baseline.
    assert max_area([1, 1]) == 1

    # 3. Empty or single line -> no container possible.
    assert max_area([]) == 0
    assert max_area([5]) == 0

    # 4. Monotonically increasing heights — best is the full width with the
    #    shorter (leftmost) side as the limiting height.
    assert max_area([1, 2, 3, 4, 5]) == 6  # min(1,5) * 4

    # 5. Monotonically decreasing heights — symmetric to (4).
    assert max_area([5, 4, 3, 2, 1]) == 6  # min(5,1) * 4 = 4? Let's check below.

    # NOTE on test 5: max area for [5,4,3,2,1] is achieved at indices (0,1) -> 4*1=4,
    # (0,2) -> 3*2=6, (0,3) -> 2*3=6, (0,4) -> 1*4=4. So 6 is correct.

    # 6. Tall equal walls -> area is just height * width.
    assert max_area([4, 4, 4, 4]) == 12  # 4 * 3

    # 7. Asymmetric tall ends dwarf the middle.
    assert max_area([10, 1, 1, 1, 10]) == 40  # min(10,10) * 4


if __name__ == "__main__":
    _tests()
    print("container-with-most-water: all tests passed")
