"""Climbing Stairs.

You can take 1 or 2 steps at a time; count the distinct ways to reach the
nth step. The number of ways follows the Fibonacci recurrence
f(n) = f(n-1) + f(n-2), since the last move is either a 1-step from n-1 or
a 2-step from n-2. We compute it bottom-up with two rolling integers for
O(1) space.
"""

from __future__ import annotations


def climb_stairs(n: int) -> int:
    """Return the number of distinct ways to climb a staircase of n steps.

    Time:  O(n)
    Space: O(1)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 1:
        return 1
    prev, curr = 1, 1  # ways(0), ways(1)
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def _tests() -> None:
    # Base cases.
    assert climb_stairs(0) == 1, "empty staircase has one (trivial) way"
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2  # (1+1), (2)
    assert climb_stairs(3) == 3  # (1+1+1), (1+2), (2+1)
    assert climb_stairs(4) == 5

    # Fibonacci-style growth: ways(n) == ways(n-1) + ways(n-2).
    assert climb_stairs(10) == climb_stairs(9) + climb_stairs(8)

    # Larger value matches the closed-form Fibonacci index F(31) = 1346269.
    assert climb_stairs(30) == 1346269

    # Negative input is rejected.
    try:
        climb_stairs(-1)
    except ValueError:
        pass
    else:  # pragma: no cover
        raise AssertionError("expected ValueError for negative n")


if __name__ == "__main__":
    _tests()
    print("climbing_stairs: all tests passed")
