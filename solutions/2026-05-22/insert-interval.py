"""Insert Interval.

Insert a new interval into a list of non-overlapping, sorted intervals,
merging any that overlap with the new one. Approach: append all intervals
ending before the new one, merge any that overlap by widening the new
interval's bounds, then append the remainder.
"""

from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    # Time: O(n)  Space: O(n)
    result: List[List[int]] = []
    i, n = 0, len(intervals)
    start, end = new_interval

    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])

    while i < n:
        result.append(intervals[i])
        i += 1

    return result


def _tests() -> None:
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert(
        [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]
    ) == [[1, 2], [3, 10], [12, 16]]
    assert insert([], [5, 7]) == [[5, 7]]
    assert insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert insert([[1, 5]], [0, 0]) == [[0, 0], [1, 5]]
    assert insert([[3, 5], [12, 15]], [6, 6]) == [[3, 5], [6, 6], [12, 15]]


if __name__ == "__main__":
    _tests()
