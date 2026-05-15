"""Daily Temperatures.

Given an array ``temperatures``, return an array ``answer`` such that
``answer[i]`` is the number of days you have to wait after day ``i`` to
see a warmer temperature (``0`` if there is no such day). We use a
monotonic decreasing stack of indices: when today's temperature breaks
the top of the stack, that index has finally found a warmer day and we
record the gap.
"""
from __future__ import annotations

from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    """Compute the wait-for-warmer-day array using a monotonic stack.

    Time:  O(n) — each index is pushed and popped at most once.
    Space: O(n) — stack and answer array.
    """
    n = len(temperatures)
    answer = [0] * n
    stack: list[int] = []  # indices with strictly decreasing temperatures

    for i, temp in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < temp:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer


def _tests() -> None:
    # Canonical example from the problem statement.
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

    # Strictly increasing — each day's answer is 1.
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]

    # Strictly decreasing — no warmer day ever, all zeros.
    assert daily_temperatures([60, 50, 40, 30]) == [0, 0, 0, 0]

    # All identical temperatures — no strictly warmer day.
    assert daily_temperatures([55, 55, 55, 55]) == [0, 0, 0, 0]

    # Single element — no future day exists.
    assert daily_temperatures([42]) == [0]

    # Empty input — return empty list.
    assert daily_temperatures([]) == []

    # Spike at the end resolves many pending indices at once.
    assert daily_temperatures([30, 38, 30, 36, 35, 40]) == [1, 4, 1, 2, 1, 0]


if __name__ == "__main__":
    _tests()
