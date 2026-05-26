"""Top K Frequent Elements.

Count occurrences with a hash map, then bucket sort by frequency: index i of
the bucket holds elements appearing exactly i times. Walking from the highest
bucket downward collects the k most frequent elements in O(n) time.
"""

from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    if k <= 0 or not nums:
        return []
    counts = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for value, freq in counts.items():
        buckets[freq].append(value)

    result: List[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        for value in buckets[freq]:
            result.append(value)
            if len(result) == k:
                return result
    return result


# Time: O(n). Space: O(n).


def _tests() -> None:
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert top_k_frequent([], 3) == []
    assert top_k_frequent([4, 4, 4], 0) == []
    assert sorted(top_k_frequent([-1, -1, -2, -2, -3], 2)) == [-2, -1]
    assert sorted(top_k_frequent([1, 2, 3, 4], 4)) == [1, 2, 3, 4]
    assert sorted(top_k_frequent([5, 5, 5, 6, 6, 7], 1)) == [5]


if __name__ == "__main__":
    _tests()
