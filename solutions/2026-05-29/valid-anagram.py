"""Valid Anagram.

Approach: two strings are anagrams iff they have identical character multisets.
Compare lengths first, then tally character counts in a single dict and verify
all counts return to zero. Runs in O(n) time and O(k) space where k is the
alphabet size.
"""
from __future__ import annotations

from typing import Dict


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    counts: Dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    return True


def _tests() -> None:
    # 1. Classic anagram.
    assert is_anagram("anagram", "nagaram") is True

    # 2. Different letters, same length.
    assert is_anagram("rat", "car") is False

    # 3. Differing lengths cannot be anagrams.
    assert is_anagram("a", "ab") is False
    assert is_anagram("abc", "ab") is False

    # 4. Both empty strings are trivially anagrams.
    assert is_anagram("", "") is True

    # 5. Single character matches / mismatches.
    assert is_anagram("a", "a") is True
    assert is_anagram("a", "b") is False

    # 6. Duplicates handled correctly.
    assert is_anagram("aabbcc", "abcabc") is True
    assert is_anagram("aabbcc", "abccba") is True

    # 7. Same letters but different multiplicities.
    assert is_anagram("aaab", "abbb") is False

    print("valid-anagram: all tests passed")


if __name__ == "__main__":
    _tests()
