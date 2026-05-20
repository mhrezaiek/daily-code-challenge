"""
Group Anagrams.

Approach: bucket each string by a canonical key derived from its character
counts. Two strings are anagrams iff their per-character counts are equal,
so a 26-length tuple of counts (over lowercase letters) is a stable,
hashable key. This runs in O(N * K) time where N is the number of strings
and K is the maximum string length, beating the O(N * K log K) sort-based
key while using O(N * K) extra space for the hash buckets.
"""
from __future__ import annotations

from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group anagrams together. Order within and across groups is unspecified."""
    buckets: dict[tuple[int, ...], list[str]] = defaultdict(list)
    for s in strs:
        counts = [0] * 26
        for ch in s:
            # Assume lowercase a-z per the canonical problem; fall back gracefully
            # for any other character by extending the alphabet via a separate map.
            idx = ord(ch) - ord("a")
            if 0 <= idx < 26:
                counts[idx] += 1
            else:
                # Robust fallback: append the raw codepoint so non a-z chars
                # still contribute to the bucket key without colliding with a-z.
                counts.append(ord(ch))
        buckets[tuple(counts)].append(s)
    return list(buckets.values())


def _normalize(groups: List[List[str]]) -> List[List[str]]:
    """Sort each group and then sort groups so equality checks are order-insensitive."""
    return sorted([sorted(g) for g in groups])


def _tests() -> None:
    # 1. Canonical example.
    assert _normalize(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        _normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])

    # 2. Empty input -> empty output.
    assert group_anagrams([]) == []

    # 3. Single empty string forms its own group.
    assert _normalize(group_anagrams([""])) == [[""]]

    # 4. All empty strings collapse into one group.
    assert _normalize(group_anagrams(["", "", ""])) == [["", "", ""]]

    # 5. No anagrams -> each string is its own group.
    assert _normalize(group_anagrams(["abc", "def", "ghi"])) == \
        _normalize([["abc"], ["def"], ["ghi"]])

    # 6. Duplicates within the same anagram group.
    assert _normalize(group_anagrams(["abc", "cba", "abc"])) == \
        _normalize([["abc", "cba", "abc"]])

    # 7. Different lengths never group together even if char sets overlap.
    assert _normalize(group_anagrams(["a", "aa", "aaa"])) == \
        _normalize([["a"], ["aa"], ["aaa"]])


if __name__ == "__main__":
    _tests()
    print("group-anagrams: all tests passed")
