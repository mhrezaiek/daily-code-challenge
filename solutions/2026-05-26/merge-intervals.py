"""Merge Intervals.

Given a list of ``[start, end]`` intervals, return the non-overlapping
intervals that cover the same ranges. Sort by start; sweep once, merging
each interval into the last result when it overlaps (touching counts as
overlap).
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    # Time: O(n log n) (sort), Space: O(n) for the output.
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda iv: iv[0])
    merged: List[List[int]] = [list(ordered[0])]
    for start, end in ordered[1:]:
        last = merged[-1]
        if start <= last[1]:
            if end > last[1]:
                last[1] = end
        else:
            merged.append([start, end])
    return merged


def _tests() -> None:
    assert merge([]) == []
    assert merge([[1, 4]]) == [[1, 4]]
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    # Touching intervals merge.
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    # Fully contained interval is absorbed.
    assert merge([[1, 10], [2, 3], [4, 5]]) == [[1, 10]]
    # Unsorted input.
    assert merge([[5, 6], [1, 3], [2, 4]]) == [[1, 4], [5, 6]]
    # Negative coordinates and duplicates.
    assert merge([[-3, -1], [-2, 0], [-3, -1]]) == [[-3, 0]]


if __name__ == "__main__":
    _tests()
